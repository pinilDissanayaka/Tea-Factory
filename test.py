from dotenv import load_dotenv, find_dotenv
import os

# Load .env file
dotenv_path = find_dotenv()


if dotenv_path:
    load_dotenv(dotenv_path)
    print(os.getenv('DATABASE_URL'))
else:
    print("No .env file found")