import os
from pathlib import Path

from dotenv import load_dotenv

from api_utils import download_image, get_response


def fetch_apod_images(api_key):
    params = {'api_key': api_key, 'count': 30}
    response = get_response('https://api.nasa.gov/planetary/apod', params)
    apod_entries = response.json()
    directory_name = 'apod_images'
    Path(directory_name).mkdir(parents=True, exist_ok=True)
    url_images = [apod_entrie['url'] for apod_entrie in apod_entries]
    for index_url, url in enumerate(url_images):
        download_image(url, f'{directory_name}/apod_{index_url}.jpg')


if __name__ == '__main__':
    load_dotenv()
    apod_api_key = os.environ['APOD_NASA_API_KEY']
    fetch_apod_images(apod_api_key)
