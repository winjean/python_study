#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import threading
from time import sleep
import datetime

loops = (15, 2, 8)


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
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i + 1, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()


if __name__ == '__main__':
    main()
