import requests
from bs4 import BeautifulSoup
import random
# url = "https://www.ivsky.com/tupian/ziranfengguang/"
# res = requests.get(url)
# soup = BeautifulSoup(res.text,"html.parser")
# divs = soup.find_all("div",class_="il_img")
# list1 = []
# for div in divs:
#     img = div.find_all("img")
#     img = img[0]
#     list1.append(img["src"])
# n = 0
# for x in list1:
#     res = requests.get("https:"+x)
#     n += 1
#     print(res)
#     # with open("index"+str(n)+".jpg","wb+") as file:
#     #     file.write(res.content)
#     #     print("已下载第%d"%(n))
# def _getfirsthtml_(url):
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     divs = soup.find_all("div", class_="il_img")

# 1.定义初始url 获取图片链接
def _mainpage_():
    url = 'https://www.ivsky.com/tupian/ziranfengguang/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    divs = soup.find_all("div",class_="il_img")
    for div in divs:
        img = div.find_all("a")
        img = img[0]
        maiurl = img["href"]
        # print(maiurl)
        _firstpage_(maiurl)


def _firstpage_(url):

    res = requests.get("https://www.ivsky.com" + url)
    soup = BeautifulSoup(res.text, "html.parser")
    divs = soup.find_all("div", class_="il_img")

    for div in divs:
        img = div.find_all("a")
        img = img[0]
        maiurl = img["href"]
        _secondpage_(maiurl)

def _secondpage_(url):
    n = random.randint(1,1000000000)
    res = requests.get("https://www.ivsky.com" + url)
    soup = BeautifulSoup(res.text, "html.parser")
    divs = soup.find_all("div", class_="pic")
    for div in divs:
        img = div.find_all("img")
        img = img[0]
        maiurl = img["src"]
        res = requests.get("https:" + maiurl)
        with open("F:/Images/index" + str(n) + ".jpg", "wb+") as file:
            file.write(res.content)
            print("已下载第%d" % (n))
            n += 1





def _main_():
    _mainpage_()

_main_()