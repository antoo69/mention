from dotenv import load_dotenv
import os

# Memuat variabel dari file .env
load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))  # Nilai default 0 jika tidak ditemukan
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
