"""
Controller for handling HTTP requests related to product operations.
"""
from io import BytesIO
from typing import List, Dict, Any
from fastapi import APIRouter, File, UploadFile, HTTPException, status, Depends
from sqlalchemy.orm import Session
from PIL import Image
from loguru import logger
from schemas.product_schema import ItemCreate, Item
from services import product_service
from utils.database import get_db

router = APIRouter()

@router.post("/upload/", response_model=List[Item])
async def upload_image(file: UploadFile = File(...),
                       db: Session = Depends(get_db)) -> List[ItemCreate]:
    """Handle image upload, predict product name, perform Google search, and return search results."""
    if not file.filename or not product_service.is_image_file(file.filename):
        logger.error(f"Invalid file type: {file.filename}")
        raise HTTPException(status_code=400, detail="Uploaded file is not an image")

    try:
        image = Image.open(BytesIO(await file.read()))
        product_name = product_service.predict_product_name(image)
        product_service.perform_google_search(product_name, db)

        results = product_service.get_stored_results(db)
        if not results:
            logger.warning(f'No results found for query: {product_name}')
            return []

        return results

    except Exception as e:
        logger.error(f'Error in uploading and search process: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Error in upload and search process') from e


@router.get("/items/", response_model=List[Item])
def get_results(db: Session = Depends(get_db)) -> List[Item]:
    """Retrieve all stored results from the database."""
    try:
        results = product_service.get_stored_results(db)
        if not results:
            raise HTTPException(status_code=404, detail="No results found")
        return results

    except Exception as e:
        logger.error(f"Error retrieving results: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error retrieving results") from e
