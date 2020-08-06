#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import json
import urllib
from loggingUtils.LoggingUtils import get_logger, setup_logger
import os


# 将get post请求的结果(byte[])转成对象
def response_to_json(response):
    # 得到的是byte[]
    byte_content = response.content
    # 转成字符串
    content = str(byte_content, 'utf-8')
    # 转成对象
    return json.loads(content)


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
    def get(self, url, token=None, headers={}, params={}):
        if token is not None:
            headers['Authorization'] = 'Bearer ' + token
        params = urllib.parse.urlencode(params).encode('utf-8')
        response = requests.get(url + "?" + str(params, 'utf-8'), headers=headers)
        return response_to_json(response)

    # post请求 入参为application/json这种情况
    def post(self, url, token=None,
             headers={'Content-type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain'},
             params={}):
        if token is not None:
            headers['Authorization'] = 'Bearer ' + token
        response = requests.post(url, data=json.dumps(params), headers=headers)
        return response_to_json(response)


def main():
    # with open(file="../loggingUtils/logging.yaml", mode='r', encoding="utf-8")as file:
    #     logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
    #     # print(logging_yaml)
    #     # 配置logging日志：主要从文件中读取handler的配置、formatter（格式化日志样式）、logger记录器的配置
    #     logging.config.dictConfig(config=logging_yaml)
    # # 获取根记录器：配置信息从yaml文件中获取
    # root = logging.getLogger()
    # # 子记录器的名字与配置文件中loggers字段内的保持一致
    # my_module = logging.getLogger("my_module")
    # print("rootlogger:", root.handlers)
    # print("selflogger", my_module.handlers)
    # # print("子记录器与根记录器的handler是否相同：", root.handlers[0] == my_module.handlers[0])
    #
    # my_module.error("DUBUG")
    # root.info("INFO -- " + __file__  + __name__ )
    # root.error('ERROR')
    # root.debug("rootDEBUG")

    APP_DIR = os.path.dirname(os.path.abspath(__file__))
    setup_logger(output_file=os.path.join(APP_DIR, 'logs', 'server.log'))
    log = get_logger()
    log.info("ssssssssssss")


    # data = {'key': 'value', 'aaa': 'bbb'}
    #
    # url = 'http://httpbin.org/get'
    # hcu = HttpClientUtils()
    # response = hcu.get(url=url, params=data)
    # print(response)
    #
    # url = 'http://httpbin.org/post'
    # hcu = HttpClientUtils()
    # response = hcu.post(url=url, params=data)
    # print(response)


if __name__ == "__main__":
    main()
