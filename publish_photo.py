import argparse
import os
import random
from pathlib import Path

import telegram
from dotenv import load_dotenv


def publish_photo(bot, chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)
    print(f'Фото опубликовано: {photo_path}')


def get_random_photo(directory):
    photos = list(Path(directory).glob('*'))
    if not photos:
        raise ValueError('В указанной директории нет фотографий.')
    return random.choice(photos)


def main():
    load_dotenv()

    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    bot = telegram.Bot(token)

    parser = argparse.ArgumentParser(
        description='Публикация фотографии в Telegram-канал.'
    )
    parser.add_argument(
        '--photo_path',
        help='Путь к фотографии для публикации. Если не указан, будет '
             'выбрана случайная фотография.',
        type=str,
        default=None
    )
    parser.add_argument(
        '--directory',
        help='Директория для поиска случайной фотографии, если `photo_path` '
             'не указан.',
        type=str,
        default='apod_images'
    )
    args = parser.parse_args()

    photo_path = args.photo_path if args.photo_path else get_random_photo(
        args.directory)

    publish_photo(bot, chat_id, photo_path)


if __name__ == '__main__':
    main()
