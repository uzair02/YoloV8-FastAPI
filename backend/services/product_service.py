"""
Service functions for handling product-related operations such as image processing,
Google search, and database interactions.
"""
from typing import List, Dict
from datetime import datetime, timezone
import os
import mimetypes
import requests
from PIL import Image
import numpy as np
from loguru import logger
from ultralytics import YOLO
from sqlalchemy.orm import Session
from models.product_model import Item
from utils.config import config

def is_image_file(filename: str) -> bool:
    """Check if the file is an image based on its MIME type."""
    mime_type, _ = mimetypes.guess_type(filename)
    return mime_type is not None and mime_type.startswith('image')

def load_model_path() -> str:
    """Load the path to the YOLO model file."""
    try:
        current_script_path = os.path.abspath(__file__)
        logger.info(f"Current script path: {current_script_path}")

        project_root_path = os.path.abspath(os.path.join(current_script_path, '../..'))
        logger.info(f"Project root path: {project_root_path}")

        model_path = os.path.join(project_root_path, 'best.pt')
        logger.info(f"YOLO model path: {model_path}")

        return model_path
    except Exception as e:
        logger.error(f"Error loading model path: {e}")
        raise

def predict_product_name(image: Image.Image) -> str:
    """Predict product name using the YOLO model."""
    try:
        image_np = np.array(image)
        model_path = load_model_path()
        logger.info("Loading YOLO model...")
        yolo_model = YOLO(model_path)
        logger.info("YOLO model loaded successfully.")

        logger.info("Performing object detection...")
        results = yolo_model.predict(image_np, verbose=False)[0]
        names = yolo_model.names

        object_detected = names[int(results.boxes.cls[0])]
        logger.info(f"Object Detected: {object_detected}")
        return object_detected
    except Exception as e:
        logger.error(f"Error predicting product name: {e}")
        raise

def perform_google_search(product_name: str, db: Session) -> None:
    """Perform Google search and store results in the database."""
    API_KEY = config.GOOGLE_API_KEY
    SEARCH_ENGINE_ID = config.SEARCH_ENGINE_ID

    search_query = f"{product_name} buy OR shop OR store OR online"
    num_results = 10
    endpoint = "https://www.googleapis.com/customsearch/v1"

    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'num': num_results,
    }

    try:
        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            logger.error(f"Error in search: {response.status_code} - {response.text}")
            raise Exception(f"Error in search: {response.text}")

        data = response.json()
        delete_existing_results(db)
        store_search_results(data, db)
    except Exception as e:
        logger.error(f"Error performing Google search: {e}")
        raise

def delete_existing_results(db: Session) -> None:
    """Delete existing search results from the database."""
    try:
        db.query(Item).delete()
        db.commit()
    except Exception as e:
        logger.error(f"Error deleting existing results: {e}")
        db.rollback()
        raise

def store_search_results(data: Dict, db: Session) -> None:
    """Store search results in the database."""
    try:
        for item in data.get('items', []):
            link = item.get('link', '')
            description = item.get('title', '')
            timestamp = datetime.now(timezone.utc)

            item_record = Item(title=description, link=link, timestamp=timestamp)
            db.add(item_record)
        db.commit()
        logger.info("Search results stored successfully.")
    except Exception as e:
        logger.error(f"Error storing search results: {e}")
        db.rollback()
        raise

def get_stored_results(db: Session) -> List[Item]:
    """Retrieve stored search results from the database."""
    try:
        stored_results = db.query(Item).all()
        return stored_results
    except Exception as e:
        logger.error(f"Error retrieving stored results: {e}")
        raise
