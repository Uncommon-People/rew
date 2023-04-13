from aiogram.utils import executor
from create_bot import dp
from handlers import client
from media.base import *


async def on_startup(_):
    print('online!')
    if cards.get():
        print('database connected')

client.register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)