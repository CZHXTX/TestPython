import requests
import re
import time

response = requests.get('http://www.yoka.com/dna/d/453/636.html')
html = response.text

urls = re.findall('<img src=".*?" _src="(.*?)" />',html)

for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(response.content)
