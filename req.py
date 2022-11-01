import requests as r
from time import time, sleep


def get_page(url='', time_out=5):
    before = time()
    while True:
        try:
            page = r.get(url)
            return page
        except:
            if time() - before > time_out:
                return None
            continue
