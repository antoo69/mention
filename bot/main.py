from pyrogram import Client
from bot.modules import tag_module  # Import modul tag
from start import start_message     # Import handler start message
from config import API_ID, API_HASH, BOT_TOKEN  # Import konfigurasi

def run_bot():
    app = Client(
        "my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    # Tambahkan handler
    app.add_handler(start_message)               # Handler untuk perintah /start
    app.add_handler(tag_module.tag_admins)       # Handler untuk mention admin
    app.add_handler(tag_module.tag_all)          # Handler untuk mention semua anggota
    app.add_handler(tag_module.stop_tag_all)     # Handler untuk menghentikan mention

    # Jalankan bot
    print("Bot berjalan...")
    app.run()

if __name__ == "__main__":
    run_bot()
