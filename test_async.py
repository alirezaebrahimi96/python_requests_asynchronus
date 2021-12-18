import requests
import time
import concurrent
import futures

links = [
    
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/wiki/Python',
    'https://en.wikipedia.org/wiki/ronaldo',
    'https://en.wikipedia.org/wiki/fifa',
    'https://en.wikipedia.org/wiki/messi',
    'https://en.wikipedia.org/wiki/mango',
    'https://en.wikipedia.org/wiki/panda',
    'https://en.wikipedia.org/wiki/bmw',
    'https://en.wikipedia.org/wiki/programming',
    'https://en.wikipedia.org/wiki/physics',
    
    ]


def asynchronous():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
        response = pool.map(res, links)

def res(url):
    response = requests.get(url)
    return response

start_time = time.time()
for url in links:
    res(url)
print(time.time()-start_time)


start_time = time.time()
asynchronous()
print(time.time()-start_time)