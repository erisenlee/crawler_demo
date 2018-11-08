from bs4 import BeautifulSoup
import requests
import urllib.parse

def fetch(url):
    print(f'start fetching {url}...')
    try:
        resp = requests.get(url)
    except Exception as identifier:
        print(f'{identifier}')
        raise
    if resp.status_code==200:
        print(f'end fetching {url} succeed...')
        return resp


def parse(resp):
    print(f'parsing {resp.request.url}')
    html = resp.content
    if html is None:
        raise ValueError(f'none parse page')
    bs4obj = BeautifulSoup(html, 'lxml')
    div = bs4obj.find('div',{'class':'div-col'})
    if div is None:
        return None
    a_tags = div.find_all('a')

    return ( a.attrs['href'] for a in a_tags)

def get_domain(url):
    parse_result = urllib.parse.urlparse(url)
    return '://'.join((parse_result.scheme,parse_result.netloc))

def main():
    start_url = 'https://en.wikipedia.org/wiki/Algorithm'
    domain = get_domain(start_url)
    url_pool = set()
    url_pool.add(start_url)
    while True:
        if len(url_pool)==0:
            break
        url = url_pool.pop()
        resp = fetch(url)
        if parse(resp) is None:
            continue
        for href in parse(resp):
            print(f'find link {href}')
            url_pool.add(urllib.parse.urljoin(domain, href))


if __name__ == '__main__':
    main()