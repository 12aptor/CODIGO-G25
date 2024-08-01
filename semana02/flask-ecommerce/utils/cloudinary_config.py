import cloudinary
from dotenv import load_dotenv
import os

load_dotenv()

cloudinary.config(
    cloud_name = os.getenv('CLOUD_NAME'),
    api_key = os.getenv('CLOUD_API_KEY'),
    api_secret = os.getenv('CLOUD_API_SECRET'),
    secure = True
)