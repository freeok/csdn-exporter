import os
import sys

import requests
from bs4 import BeautifulSoup

user_name = sys.argv[1]

url = "https://blog.csdn.net/{}".format(user_name)
# 构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
# 发送 get 请求
r = requests.get(url=url, headers=headers, timeout=5)
# 解析 HTML
soup = BeautifulSoup(r.text, 'html.parser')

# 获取用户名
div = soup.find("div", class_="user-profile-head-name")
username = div.text.split(" ")[0]

# 获取专栏链接
divs = soup.find_all("div", class_="aside-common-box-content")
div = divs[1]
lis = div.find_all("li")

file_name = f"category_links_{user_name}.txt"
# 爬取专栏链接及链接名
if os.path.isfile(file_name):
    # 如果文件存在，删除文件
    os.remove(file_name)

titles = []
infos = {}
for li in lis:
    url = li.find("a").attrs['href']
    title = li.find("span").attrs['title']
    titles.append(title)
    infos[title] = {"url": url}
    # 设置文件对象
    with open(file_name, 'a+') as f1:
        f1.write(url)
        f1.write('\n')