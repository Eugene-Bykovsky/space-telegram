import logging

import requests

from requests_tools import get_response


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
