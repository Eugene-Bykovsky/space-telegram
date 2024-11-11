import os
import random
import time
from argparse import ArgumentParser
from pathlib import Path

import telegram
from dotenv import load_dotenv
from PIL import Image

from telegram_tools import publish_photo


def compress_image(image_path, max_size=20 * 1024 * 1024):
    with Image.open(image_path) as img:
        if os.path.getsize(image_path) > max_size:
            img = img.convert('RGB')
            img.save(image_path, 'JPEG', quality=85)
    return image_path


def send_random_photo_on_schedule(directory, bot, chat_id, delay_hours):
    photo_paths = list(Path(directory).glob('*'))
    random.shuffle(photo_paths)

    while True:
        for photo_path in photo_paths:
            if photo_path.is_file():
                compressed_photo_path = compress_image(photo_path)
                publish_photo(bot, chat_id, compressed_photo_path)
                time.sleep(delay_hours * 3600)

        random.shuffle(photo_paths)


def main():
    load_dotenv()

    parser = ArgumentParser(description='Скрипт для публикации фотографий в '
                                        'Telegram канал') 
    parser.add_argument('directory', help='Директория с фотографиями')
    parser.add_argument('--delay', type=int,
                        default=int(os.getenv('PUBLISH_DELAY_HOURS', 4)),
                        help='Часы между публикациями (по умолчанию 4 часа)')
    args = parser.parse_args()

    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    bot = telegram.Bot(token)
    send_random_photo_on_schedule(args.directory, bot, chat_id, args.delay)


if __name__ == '__main__':
    main()
