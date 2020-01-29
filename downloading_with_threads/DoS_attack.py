import sys
import time
from concurrent import futures

import requests


def get_request(worker):
    request = requests.get("https://mobi.uz/upload/rk/836/mobi%20110%20banner%20uz.jpg", verify=False)
    return worker + " response_code: " + str(request.status_code)


def download_many():
    workers = ["thread {}".format(i) for i in range(1, 5)]

    with futures.ThreadPoolExecutor(len(workers)) as executor:
        res = executor.map(get_request, workers)

    total_success_workers = 0
    for worker in list(res):
        print(worker)
        total_success_workers += 1

    return total_success_workers


def main():
    t0 = time.time()
    count = download_many()
    elapsed = time.time() - t0
    msg = '{} threads done in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main()
# Test comment
