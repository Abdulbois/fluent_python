import os
import time
import sys
import requests

POP20_CC = 'Afghanistan Uzbekistan United-States-of-America Russia Iran Iraq Germany Italy France Belgium ' \
           'Austria China Canada Mexico Argentina Brazil Turkey Denmark Vietnam Greece'.split()

BASE_URL = 'https://www.countries-ofthe-world.com/flags-normal/'

DEST_DIR = '/Users/macmini2/Downloads/flags/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}flag-of-{cc}.png'.format(BASE_URL, cc=cc)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.68'}
    resp = requests.get(url, headers=headers)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.png')
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)