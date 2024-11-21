from concurrent.futures.thread import ThreadPoolExecutor
import time
import requests
from orca.orca import start

import exercise2

from urllib3 import request


urls = ["https://www.google.com",
"https://www.github.com",
"https://www.python.org",
"https://www.stackoverflow.com",
"https://www.yahoo.com",
"https://www.rediff.com",
"https://www.ibab.ac.in",
"https://www.iitb.ac.in",
"https://home.iitd.ac.in"
    ]

def fetch_url(url):
    try:
        response = requests.get(url)
        return f"{url}-{response.headers}"
    except Exception as err:
        return f"{url} - error{err}"

def get_time(func):
    def wrapper():
        start_time = time.time()
        print(f"Start time: {start_time}")
        func()
        end_time = time.time()
        print(f"End time:{end_time}")
        res= end_time-start_time
        print(f"Time taken: {res}")
        # log_time.append(res)
    return wrapper

@get_time
def perform_fetch():
    with ThreadPoolExecutor(max_workers=8)as executor1:
        results = executor1.map(fetch_url, urls)
    for result in results:
        print(result)



perform_fetch()