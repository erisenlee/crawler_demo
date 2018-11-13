import grequests
import asyncio


async def fetch(url):
    print(f'start fetching {url}...')
    try:
        resp =  grequests.get(url)
    except Exception as e:
        print(f'{e}')
        raise
    if resp.status_code==200:
        print(f'end fetching {url} succeed...')
        return resp
urls = [
    'https://en.wikipedia.org/wiki/Algorithm',
    'https://docs.python.org/3/genindex.html',
    'https://ebookfoundation.github.io/free-programming-books/free-programming-books.html#go'
]

def main():
    reqs = ( grequests.get(url) for url in urls)
    res = reqs.send()

if __name__ == '__main__':
    main()