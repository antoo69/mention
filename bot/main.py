from pyrogram import Client
from bot.modules import tag_module
from start import start_message

def run_bot():
    app = Client(
        "my_bot",
        api_id="YOUR_API_ID",  # Ganti dengan API ID Anda
        api_hash="YOUR_API_HASH",  # Ganti dengan API Hash Anda
        bot_token="YOUR_BOT_TOKEN"  # Ganti dengan token bot Anda
    )

    # Tambahkan handler
    app.add_handler(start_message)
    app.add_handler(tag_module.tag_admins)
    app.add_handler(tag_module.tag_all)
    app.add_handler(tag_module.stop_tag_all)

    # Jalankan bot
    print("Bot berjalan...")
    app.run()
