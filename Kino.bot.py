import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import yt_dlp

BOT_TOKEN = "8478801034:AAGZfXDb9_Vv1MczaZaOW5_hXyXZkk0Og0Q"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("🎬 Instagram / TikTok / YouTube link yuboring")

@dp.message()
async def download_video(message: types.Message):
    url = message.text.strip()
    msg = await message.answer("⏳ Yuklanmoqda...")

    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "format": "mp4/best",
      "format": "mp3/best audio",
        "quiet": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await bot.send_video(
            chat_id=message.chat.id,
            video=types.FSInputFile(filename),
            caption="✅ Tayyor"
        )
        os.remove(filename)

    except Exception as e:
        await msg.edit_text(f"❌ Xatolik: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
