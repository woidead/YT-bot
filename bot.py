from aiogram import *
from config import TOKEN
from pytube import *
import os

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'привет, я скачаю видео с YouTube, лишь по ссылке')

@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url= message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://www.youtube.com/' or 'https://www.youtu.be/':
        await bot.send_message(chat_id, f'*загрузка видео начата*: *{yt.title}*\n'
                                        f'*С канала*: {yt.author}', parse_mode='Markdown')
        await download_youtube_vidio(url, message, bot)



async def download_youtube_vidio(url, message, bot):
    yt=YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f"{message.chat.id}_{yt.title}")
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption='*вot ваше видео*', parse_mode='Markdown')
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')


if __name__ == '__main__':
    executor.start_polling(dp)