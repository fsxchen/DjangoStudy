#!/usr/bin/env python2.7
#coding:utf-8

import os, sys
sys.path.append("/home/hqth/fsxchen/python/DjangoStudy/monitor")
class GetStatus(object):
    def __init__(self, host):
        self.host = host

    def isAlive(self):
        ping_res = os.popen("ping -c4 " + self.host)
        res = [info.strip() for info in ping_res.readlines()[-2].split(',') if "packet loss" in info ]
        if int(res[0].split(' ')[0].strip("%")) == 100:
            return False
        else:
            return True

if __name__ == '__main__':
    h1 = GetStatus("192.168.1.201")
    h1.isAlive()