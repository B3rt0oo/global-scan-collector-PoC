from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Read environment variables
DB_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("COLLECTOR_API_KEY")

# DEBUG: print the API key so we know FastAPI sees it
print("DEBUG: COLLECTOR_API_KEY =", API_KEY)
