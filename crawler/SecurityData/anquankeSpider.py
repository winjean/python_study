#!/usr/bin/env python3
# encoding=utf-8

from bs4 import BeautifulSoup
import requests
import json


BASE_URL = 'https://www.anquanke.com'
DOWNLOAD_URL = BASE_URL + '/knowledge'
LIST_URL = 'https://api.anquanke.com/data/v1/posts?size=10&page=2&category=knowledge'
ARTICLE_URL = 'https://www.anquanke.com/post/id/'


# 请求地址
def get_html(url, param):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    return requests.get(url, params=param, headers=header).content


# 获取文章列表
def get_list(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    article_list = soup.find_all("div", attrs={'class': 'article-item'})
    return article_list


# 获取文章
def get_article(url):
    html = get_html(url, None)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.text)
    ol = soup.find(class_='content')
    return ol.text


# 获取分页数
def get_page_count(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    next_page = soup.find("li", attrs={'title': '下一页'})
    last_page = next_page.previous_element
    print(last_page)
    return last_page


def main():
    for m in range(10):
        param = {
            "category": "knowledge",
            "size": 10,
            "page": m + 1
        }

        json_str = get_html(LIST_URL, param)
        data = json.loads(json_str)
        article_list = data["data"]
        for article in article_list:
            article_url = ARTICLE_URL + str(article["id"])
            print(article_url)
            article_text = get_article(article_url)
            print(article_text)
            print("print finish")


if __name__ == '__main__':
    main()

