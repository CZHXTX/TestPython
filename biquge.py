import requests
from lxml import etree
#获取想要爬取的链接
urls = ['http://www.biquge.info/59_59318/{}.html'.format(i) for i in range (9195174,18792818)]
#测试是否获取成功
#for url in urls:
#print(url)

#设置保持的路径
path = r'D:\\xiaoshuo\\'
#获取小说内容并保存
def get_text(url):
 r = requests.get (url)
 r.encoding = 'UTF-8'
 selector = etree.HTML(r.text)
#获取文章标题
 title = selector.xpath('/html/head/title/text()')
#获取小说正文内容
 text = selector.xpath('//*【@id="content"】/text()')
 with open(path + title[0], 'w', encoding = 'UTF-8') as f:
  for i in text:
   f.write(i)

if __name__ == '__main__':
 for url in urls:
  get_text(url)