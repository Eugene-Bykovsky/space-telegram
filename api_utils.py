import logging
from os.path import splitext
from urllib.parse import unquote, urlsplit

import requests


def get_response(url, params=None):
    response = requests.get(url, params)
    response.raise_for_status()
    return response


def download_image(url, save_path, params=None):
    try:
        response = get_response(url, params)

        if 'image' not in response.headers['Content-Type']:
            if 'error' in response.content.decode('utf-8',
                                                  errors='ignore').lower():
                raise requests.exceptions.HTTPError('Есть ошибка '
                                                    'в ответе от сервера')
            logging.warning('Ответ не является изображением')

        with open(save_path, 'wb') as f:
            f.write(response.content)
    except requests.exceptions.RequestException as e:
        logging.error(f'Ошибка при загрузке изображения: {e}')
        raise


def get_file_extension(url):
    url = urlsplit(url)
    _, extension = splitext(unquote(url.path))
    return extension
