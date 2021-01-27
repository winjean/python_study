#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import threading
from time import sleep
import datetime

loops = (4, 2, 8)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    ''' rewrite run() '''

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    while True:
        print(f'start loop {nloop} at: { datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") }')

        sleep(nsec)


def main():
    threads = []

    # 获取一个数组[0,1,2]
    nloops = range(len(loops))

    for i in nloops:
        # 构建线程
        t = MyThread(loop, (i + 1, loops[i]))

        # 增加到线程数组中
        threads.append(t)

    for i in nloops:
        # 遍历启动线程
        threads[i].start()


if __name__ == '__main__':
    main()
