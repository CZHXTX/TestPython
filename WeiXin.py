import requests
from urllib.parse import urlencode

base_url = 'http://weixin.sougou.com/weixin?'

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return  response.text
        if response.status_code == 302:
            pass
    except ConnectionError:
        return get_html(url)
def get_index(keyword,page):
    data ={
        'query':keyword,
        'type':2,
        'page':page
    }
    queries = urlencode(data)
    url = base_url + queries