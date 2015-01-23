#!/usr/bin/python
#coding:utf-8
import threading
import Queue

class WorkManager(object):
    def __init__(self, thread_num=100):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.thread_num = thread_num

    def start_thread_pool(self):
        for i in range(self.thread_num):

            worker = WorkThread(self.work_queue)
            worker.setDaemon(True)
            worker.start()
            self.threads.append(worker)

    def add_job(self, func, **kwargs):
        self.work_queue.put((func, kwargs))#任务入队，Queue内部实现了同步机制

    def check_queue(self):
        return self.work_queue.qsize()

    def check_thread(self):
        counter = 0
        for thread in self.threads:
            if thread.isAlive():
                counter += 1
        if counter*10 < self.work_queue.qsize and counter < self.thread_num:
            worker = Work(self.work_queue)
            worker.setDaemon(True)
            worker.start()
            self.threads.append(worker)
        return counter


    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()

    def quit_thread(self):
        for item in self.threads:
            item.join(1)
        sys.exit()

class WorkThread(threading.Thread):
    """docstring for WorkThread"""
    def __init__(self, work_queue):
        super(WorkThread, self).__init__()
        self.work_queue = work_queue

    def run(self):
        #死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                if self.work_queue.qsize() < 1:
                    break
                do, kwargs = self.work_queue.get(block=False)#任务异步出队，Queue内部实现了同步机制
                do(kwargs)
                # self.work_queue.task_done()#通知系统任务完成

            except Exception,e:
                continue
