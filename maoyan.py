import requests
from requests.exceptions import RequestException
import re
def get_one_page(url):
    try:
      response = requests.get(url)
      if(response.status_code ==200):
          return  response.text
      return None
    except RequestException:
        return  None
def parser_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?(\d+)</i>.*?data-src="(.*?)".*?name')

def main():
    url = 'http://maoyan.com/board/4?'
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()


