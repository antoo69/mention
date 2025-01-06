import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait

SPAM_CHATS = []

# Fungsi untuk men-tag admin saja
@Client.on_message(filters.command(["atag"]) & filters.group, group=31)
async def tag_admins(client, message):
    chat_id = message.chat.id

    try:
        # Ambil daftar admin
        admins = [
            admin.user.id
            async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
        ]

        if message.from_user.id not in admins:
            return await message.reply("Kamu bukan admin!")

        # Ambil teks tambahan dari perintah
        text = message.text.split(None, 1)[1] if len(message.command) > 1 else "Halo Admin!"

        # Pisahkan teks dan link
        links = "\n".join([word for word in text.split() if word.startswith("http")])
        text = " ".join([word for word in text.split() if not word.startswith("http")])

        # Format pesan
        header = f"✧ ·({text})· ✧\n\n"
        links_section = f"{links}\n\n" if links else ""
        admin_list = []

        # Menandai semua admin
        async for member in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if member.user.is_bot:
                continue
            admin_list.append(f"┇・[{member.user.first_name}](tg://user?id={member.user.id})")

        output_message = header + links_section + "╭✦ ⎯⎯⎯⎯˗\n" + "\n".join(admin_list) + "\n╰ ✦ ⎯⎯⎯⎯"
        await message.reply_text(output_message, disable_web_page_preview=True)

    except Exception as e:
        print(f"Error in tag_admins: {e}")


# Fungsi Tag Semua Anggota
@Client.on_message(filters.command(["utag"]) & filters.group, group=30)
async def tag_all(client, message):
    chat_id = message.chat.id

    try:
        admins = [
            admin.user.id
            async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
        ]
        if message.from_user.id not in admins:
            return await message.reply("Kamu bukan admin.")

        if chat_id in SPAM_CHATS:
            return await message.reply_text(
                "Tagall sedang dalam proses di grup ini. Ketik /cancel untuk menghentikan proses!"
            )

        SPAM_CHATS.append(chat_id)
        replied = message.reply_to_message
        user_list = []

        if replied:
            text = replied.text
        else:
            text = message.text.split(None, 1)[1] if len(message.command) > 1 else None

        if not text:
            return await message.reply_text("**Berikan teks atau balas pesan untuk mulai tagall.**")

        # Pisahkan teks dan link
        links = "\n".join([word for word in text.split() if word.startswith("http")])
        text = " ".join([word for word in text.split() if not word.startswith("http")])

        header = f"✧ ·({text})· ✧\n\n"
        links_section = f"{links}\n\n" if links else ""

        async for member in client.get_chat_members(chat_id):
            if chat_id not in SPAM_CHATS:
                break
            if member.user.is_deleted or member.user.is_bot:
                continue

            user_list.append(f"┇・[{member.user.first_name}](tg://user?id={member.user.id})")

            if len(user_list) == 10:
                output_message = header + links_section + "╭✦ ⎯⎯⎯⎯˗\n" + "\n".join(user_list) + "\n╰ ✦ ⎯⎯⎯⎯"
                if replied:
                    await replied.reply_text(output_message, disable_web_page_preview=True)
                else:
                    await message.reply_text(output_message, disable_web_page_preview=True)
                user_list = []
                await asyncio.sleep(2)

        if user_list:
            output_message = header + links_section + "╭✦ ⎯⎯⎯⎯˗\n" + "\n".join(user_list) + "\n╰ ✦ ⎯⎯⎯⎯"
            if replied:
                await replied.reply_text(output_message, disable_web_page_preview=True)
            else:
                await message.reply_text(output_message, disable_web_page_preview=True)

    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        print(f"Error in tag_all: {e}")
    finally:
        if chat_id in SPAM_CHATS:
            SPAM_CHATS.remove(chat_id)


# Fungsi untuk membatalkan proses tagall atau tagadmin
@Client.on_message(filters.command(["stopmention", "cancel", "cancelmention", "offmention", "mentionoff", "cancelall"]) & filters.group, group=29)
async def stop_tag_all(client, message):
    chat_id = message.chat.id

    try:
        admins = [
            admin.user.id
            async for admin in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
        ]
        if message.from_user.id not in admins:
            return await message.reply("Kamu bukan admin!")

        if chat_id in SPAM_CHATS:
            SPAM_CHATS.remove(chat_id)
            return await message.reply_text("**Proses tagall berhasil dihentikan!**")
        else:
            return await message.reply_text("**Tidak ada proses tagall yang berjalan!**")
    except Exception as e:
        print(f"Error in stop_tag_all: {e}")
