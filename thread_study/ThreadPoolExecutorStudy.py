#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, as_completed, ALL_COMPLETED
import time


def spider(page):
    time.sleep(page)
    print(f"crawl task{page} finished")
    return page


def main():
    # 创建一个最大容纳数量为5的线程池
    with ThreadPoolExecutor(max_workers=5, thread_name_prefix='thread_') as t:
        # 通过submit提交执行的函数到线程池中
        # task1 = t.submit(spider, 1)
        # task2 = t.submit(spider, 2)
        # task3 = t.submit(spider, 3)
        #
        # # 通过done来判断线程是否完成
        # print(f"task1: {task1.done()}")
        # print(f"task2: {task2.done()}")
        # print(f"task3: {task3.done()}")
        #
        # time.sleep(2.5)
        # print(f"task1: {task1.done()}")
        # print(f"task2: {task2.done()}")
        # print(f"task3: {task3.done()}")
        #
        # # 通过result来获取返回值
        # print(task1.result())

        # 提交线程池
        all_task = [t.submit(spider, page) for page in range(1, 5)]
        # wait(all_task, return_when=FIRST_COMPLETED)
        # print('finished')
        # print(wait(all_task, timeout=1.5))

        # 按输入顺序输出结果
        # i = 1
        # for result in t.map(spider, [2, 3, 1, 4]):
        #     print("task{}:{}".format(i, result))
        #     i += 1

        # 按完成顺序输出结果
        for future in as_completed(all_task):
            data = future.result()
            print(f"main: {data}")


if __name__ == '__main__':
    main()
