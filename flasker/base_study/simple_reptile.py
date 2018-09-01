#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : simple_reptile.py
# @Author: QUANLI
# @Date  : 2018/8/17 19:14
# @Desc  : 简要爬虫获取

# import re, urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.piaohua.com/html/lianxuju/2018/0619/33842.html"
# html = urllib.request.urlopen(url).read()
# html = html.decode('utf-8')     #python3版本中需要加入
# print(html)
#
# links = re.findall('<a target="_blank" href="(.+?)" title',html)
# titles = re.findall('<a target="_blank" .+? title="(.+?)">',html)
# tags = re.findall('<a target="_blank" .+? title=.+?>(.+?)</a>',html)
# for link,title,tag in zip(links,titles,tags):
#     print(tag,url+link,title)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('user-agent="User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"')
chrome_options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
driver = webdriver.Chrome(executable_path="E:/chromedriver.exe", chrome_options=chrome_options)

driver.get(url)
a_list = driver.find_element_by_tag_name("a")
driver.quit()