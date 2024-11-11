import os
from pathlib import Path

from dotenv import load_dotenv

from downoload_tools import download_image
from requests_tools import get_response


def fetch_epic_images(api_key):
    params = {'api_key': api_key}
    response = get_response('https://api.nasa.gov/EPIC/api/natural/images',
                            params)
    date_image_pairs = [(entrie['image'],
                         entrie['date'].split()[0].replace('-', '/'))
                        for entrie in response.json()]
    directory_name = 'epic_images'
    Path(directory_name).mkdir(parents=True, exist_ok=True)

    for index_url, date_image in enumerate(date_image_pairs):
        url = (f'https://api.nasa.gov/EPIC/archive/natural/'
               f'{date_image[1]}/png/{date_image[0]}.png')
        download_image(url,
                       f'{directory_name}/epic_{index_url}.jpg',
                       params)


if __name__ == '__main__':
    load_dotenv()
    epic_nasa_api_key = os.environ['EPIC_NASA_API_KEY']
    fetch_epic_images(epic_nasa_api_key)
