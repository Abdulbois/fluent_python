from concurrent import futures
from flags import main
from flags_threadpool import download_one

MAX_WORKERS = 4


def download_many(cc_list):
    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)

