"""
Module for defining the SQLAlchemy model for the 'items' table.
"""

import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from utils.database import Base

class Item(Base):
    """
    Represents an item in the database.

    Attributes:
        items_id (UUID): Unique identifier for the item.
        title (str): Title of the item.
        link (str): URL link associated with the item.
        timestamp (DateTime): The time when the item was created or last updated.
    """
    __tablename__ = 'items'
    items_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False, index=True)
    link = Column(String, nullable=False)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        """
        Provides a string representation of the Item object.

        Returns:
            str: A string representation of the item, including its id, title, link, and timestamp.
        """
        return f"<Item(id={self.items_id}, title={self.title}, link={self.link}, timestamp={self.timestamp})>"
