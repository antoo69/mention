from pyrogram import Client
from bot.modules import tag_module
from start import start_message
from config import API_ID, API_HASH, BOT_TOKEN

def run_bot():
    app = Client(
        "my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    @app.on_message(filters.command("ping"))
    async def ping_handler(client, message):
        await message.reply("Pong!")

    print("Menghubungkan ke Telegram...")
    try:
        app.start()
        print("Bot berhasil terhubung!")
        app.stop()
    except Exception as e:
        print(f"Error saat menghubungkan: {e}")
        return

    print("Bot berjalan...")
    app.run()

if __name__ == "__main__":
    run_bot()
