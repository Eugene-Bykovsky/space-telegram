from os.path import splitext
from urllib.parse import unquote, urlsplit


def get_file_extension(url):
    url = urlsplit(url)
    _, extension = splitext(unquote(url.path))
    return extension
