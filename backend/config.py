import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change_this_secret")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/saferoute_ai")
    MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN", "YOUR_MAPBOX_TOKEN")
    OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY", "YOUR_OPENWEATHER_KEY")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    BENGALURU_DATA = os.path.join(BASE_DIR, "data", "crime_bengaluru.csv")
    DELHI_DATA = os.path.join(BASE_DIR, "data", "crime_delhi.csv")