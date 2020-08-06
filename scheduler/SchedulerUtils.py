#!/usr/bin/python3
# -*- coding: UTF-8 -*-


# from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_SCHEDULER_SHUTDOWN, EVENT_SCHEDULER_STARTED, JobExecutionEvent
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
# import logging
import datetime
import time

# jobstores = {
#     'mongo': MongoDBJobStore(),
#     'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
# }
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(5)
# }
# job_defaults = {
#     'coalesce': False,
#     'max_instances': 3
# }


"""
    BlockingScheduler 阻塞式调度器：适用于只跑调度器的程序。
    BackgroundScheduler 后台调度器：适用于非阻塞的情况，调度器会在后台独立运行。
    AsyncIOScheduler AsyncIO调度器，适用于应用使用AsnycIO的情况。
    GeventScheduler Gevent调度器，适用于应用通过Gevent的情况。
    TornadoScheduler Tornado调度器，适用于构建Tornado应用。
    TwistedScheduler Twisted调度器，适用于构建Twisted应用。
    QtScheduler Qt调度器，适用于构建Qt应用。
"""


class SchedulerUtils:

    def __init__(self, scheduler=BackgroundScheduler()):
        self.scheduler = scheduler


def main():

    # 定义事件监听
    def job_exception_listener(event):

        if event.code == EVENT_SCHEDULER_STARTED:
            print("SCHEDULER_STARTED")

        elif event.code == EVENT_SCHEDULER_SHUTDOWN:
            print("SCHEDULER_SHUTDOWN")

        elif isinstance(event, JobExecutionEvent) and event.exception:
            # todo：异常处理, 告警等
            print('The job crashed :(' + event.traceback)

        elif isinstance(event, JobExecutionEvent):
            print('The job worked :)')

        else:
            print('uncheck event')

    # 定义调度器
    # scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
    scheduler = BackgroundScheduler()

    # 定义任务
    def job_func(job_id):
        print('job %s is runed at %s' % (job_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    # 添加任务
    scheduler.add_job(job_func, id='job_id', name='a test job', args=['winjean_test_job'],
                      trigger='interval', start_date='2020-08-01 09:30:00', end_date='2020-10-15 11:00:00', seconds=3,
                      max_instances=10,
                      jobstore='default',
                      executor='default')

    # 增加监听事件
    scheduler.add_listener(job_exception_listener,
                           EVENT_JOB_EXECUTED | EVENT_JOB_ERROR |
                           EVENT_SCHEDULER_SHUTDOWN | EVENT_SCHEDULER_STARTED)

    # 启动调度器
    scheduler.start()

    time.sleep(10)

    # 关闭调度器
    scheduler.shutdown()


if __name__ == "__main__":
    main()



