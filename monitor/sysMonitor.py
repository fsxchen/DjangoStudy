#!/usr/bin/env python2.7
#coding:utf-8

import os

class GetStatus(object):
    def __init__(self, host):
        self.host = host

    def isAlive(self):
        ping_res = os.popen("ping -c4 " + self.host)
        res = [info.strip() for info in ping_res.readlines()[-2].split(',') if "packet loss" in info ]
        print res

h1 = GetStatus("192.168.1.201")
h1.isAlive()