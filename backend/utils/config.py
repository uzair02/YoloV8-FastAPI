import os
from dotenv import load_dotenv

class Config:
    """Config class to handle loading environment variables."""

    def __init__(self):
        load_dotenv()
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable is not set")
        if not self.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        if not self.SEARCH_ENGINE_ID:
            raise ValueError("SEARCH_ENGINE_ID environment variable is not set")

config = Config()
