import argparse
from pathlib import Path

from api_utils import download_image, get_response


def fetch_spacex_images(launch_id):
    response = get_response(f'https://api.spacexdata.com/v5/launches/'
                            f'{launch_id}')
    data = response.json()
    directory_name = 'spacex_launch_images'
    Path(directory_name).mkdir(parents=True, exist_ok=True)
    url_images = data.get('links', {}).get('flickr', {}).get('original', [])
    for index_url, url_image in enumerate(url_images):
        download_image(url_image, f'{directory_name}/spacex_{index_url}.jpg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Скрипт для скачивания фото запусков SpaceX')
    parser.add_argument('--launch_id', type=str, default='latest',
                        help='ID запуска')
    args = parser.parse_args()
    fetch_spacex_images(args.launch_id)
