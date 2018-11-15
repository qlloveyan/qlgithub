#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : scheduler_example.py
# @Author: QUANLI
# @Date  : 2018/11/15 15:29
# @Desc  : 调度器框架APScheduler学习

import threading
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

class Timer(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.name = name

    def run(self):
        if not scheduler.running:
            try:
                scheduler.print_jobs()
                scheduler.start()
            except Exception as e:
                scheduler.shutdown()

    def stop(self):
        self.thread_stop = True

@scheduler.scheduled_job('cron', id='timer', second='*/30', minute="*", hour='*')
def execute():
    print("开始处理轮训任务……")


if __name__ == "__main__":
    timer = Timer("scheduler_test")
    timer.start()
