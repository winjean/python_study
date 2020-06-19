from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
# import logging
import datetime

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


def job_exception_listener(event):
    if event.exception:
        # todo：异常处理, 告警等
        print('The job crashed :(')
    else:
        print('The job worked :)')


# 定义调度器
# scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
scheduler = BackgroundScheduler()


def job_func(job_id):
    print('job %s is runed at %s' % (job_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


# 添加任务
scheduler.add_job(job_func, id='job_id', name='a test job', args=[2],
                  trigger='interval', start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00', seconds=5,
                  max_instances=10,
                  jobstore='default',
                  executor='default')

scheduler.add_listener(job_exception_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# 启动调度器
scheduler.start()
