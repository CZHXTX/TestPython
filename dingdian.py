import requests
# from bs4 import BeautifulSoup
# from lxml import etree
# # 地址
# # mainurl = 'https://www.booktxt.net/1_1600/'
# # res = requests.get(mainurl)
# # res.encoding = 'gb2312'
# # soup = BeautifulSoup(res.text,'html.parser')
# # divs = soup.find_all('div',id='list')
# # divs = divs[0]
# # dds = divs.find_all('dd')
# # urlList = []
# # for dd in dds:
# #     href = dd.find_all('a')
# #     href = href[0]["href"]
# #     urlList.append(href)


# for url in urlList:
#     res = requests.get(mainurl+url)
#     res.encoding = 'gb2312'
#     soup = BeautifulSoup(res.text, 'html.parser')
#     textContent = soup.find_all("div", id="content")
#     print(textContent) //*[@id="content"]  //*[@id="wrapper"]/div[4]/div/div[2]/h1

r = requests.get("https://www.booktxt.net/1_1600/518665.html")
r.encoding = 'gb2312'
selector = etree.HTML(r.content)

title = selector.xpath('//*[@id="wrapper"]/div[4]/div/div[1]/a[1]/text()')

print(title)
