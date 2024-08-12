"""
This module defines Pydantic schemas for item-related operations.

Schemas include:
- ItemBase: Base schema for item attributes.
- ItemCreate: Schema for creating new items.
- Item: Schema for item details including ID and timestamp.
"""

from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from uuid import UUID
from typing import Optional

class ItemBase(BaseModel):
    """
    Base schema representing the core attributes of an item.
    
    Attributes:
        title (str): The title of the item, with a minimum length of 1 and maximum length of 100.
        link (HttpUrl): The URL link associated with the item.
    """
    title: str = Field(..., min_length=1, max_length=100)
    link: HttpUrl

    class Config:
        """
        Configuration for the Pydantic model.
        """
        str_strip_whitespace = True

class ItemCreate(ItemBase):
    """
    Schema representing the fields required to create a new item.
    Inherits from ItemBase, which includes the title and link attributes.
    """
    pass

class Item(ItemBase):
    """
    Schema representing an item with additional attributes for database records.
    
    Attributes:
        items_id (UUID): Unique identifier for the item.
        timestamp (datetime): Timestamp of creation or last update.
    """
    items_id: UUID
    timestamp: datetime

    class Config:
        """
        Configuration for the Pydantic model.
        """
        from_attributes = True
        str_strip_whitespace = True
        json_encoders = {
            UUID: str,
            datetime: lambda v: v.isoformat()
        }
