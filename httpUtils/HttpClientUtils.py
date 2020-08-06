#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import json
import urllib


class HttpClientUtils:
    def __init__(self):
        self.url = ''
        self.params = ''
        self.type = 'post'
        # 默认post请求
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
        # 默认请求头
        self.addheader = ''
        self.run_res = ''
        self.cookies = []

    # get请求
    def get(self, url, token=None, headers={}, params_obj={}):
        if token is not None:
            headers['Authorization'] = 'Bearer ' + token
        params = urllib.parse.urlencode(params_obj).encode('utf-8')
        response = requests.get(url + "?" + str(params, 'utf-8'), headers=headers)
        return self.to_response(response)

    # post请求 入参为application/json这种情况
    def post(self, url, token=None,
             headers={'Content-type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain'},
             params={}):
        if token is not None:
            headers['Authorization'] = 'Bearer ' + token
        response = requests.post(url, data=json.dumps(params),headers=headers)
        return self.to_response(response)

    # 将get post请求的结果(byte[])转成对象
    def to_response(self, response):
        # 得到的是byte[]
        byte_content = response.content
        # 转成字符串
        content = str(byte_content, 'utf-8')
        # 转成对象
        return json.loads(content)


def main():
    url = 'http://www.baidu.com'
    data = {'key': 'value', 'aaa': 'bbb'}
    response = requests.get(url, data)
    print(response.text)

    url = 'http://httpbin.org/post'
    data = {'key': 'value', 'aaa': 'bbb'}
    response = requests.post(url, data)
    print(response.json())


if __name__ == "__main__":
    main()
