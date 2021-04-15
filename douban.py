import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?start={}&count=18&loc_id=108288"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)
        print(dict_ret)
        content_list = dict_ret["subject_collection_items"]
        return content_list

    def save_content(self, content_list):
        with open("douban.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii="False"))
                f.write("\n")

    def run(self):
        # 实现主要逻辑
        num = 0
        while True:
            # 1.start_url
            url = self.url_temp.format(num)
            # 2.发送请求
            json_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(json_str)
            # 4.保存数据
            self.save_content(content_list)
            if len(content_list) < 18:
                break
            # 5.构造下一页的rul
            num += 18


if __name__ == "__main__":
    douban_spider = DoubanSpider()
    douban_spider.run()
