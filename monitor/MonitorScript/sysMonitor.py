import psycopg2
import sys, os

import status
import MyThread
import Ping

con = None
max_thread = 100

# wm = MyThread.WorkManager(50)
#     for ip_port in xml1.ipcreate("iplist.xml"):
#         ip = str(ip_port[0])
#         port = int(ip_port[1])
#         wm.add_job(epoll_register, ip=ip, port=port, timeout=5)
#         wm.start_thread_pool()


def isAlive(ip):
    ping_res = os.popen("ping -c4 " + ip)
    return True

    res = [info.strip() for info in ping_res.readlines()[-2].split(',') if "packet loss" in info ]
    if int(res[0].split(' ')[0].strip("%")) == 100:
        return False
    else:
        return True


# def isAlive(ip):
#     ping_res = Ping.verbose_ping(ip)
#     return True

def setStutus(args):
    ip = args['ip']
    stat = args['stat']
    print ip, stat
    # print ip, stat
    # print con
    # print cur
    # h = status.GetStatus(ip)
    # print h
    if isAlive(ip):
        if stat != 1:
            sql = """UPDATE monapp_host SET "Status" = 1 WHERE "Pri_IP" = '%s'""" %(ip)
            cur.execute(sql)
            con.commit()
            print sql

try:
    con = psycopg2.connect(database='monitordb', host="localhost", user='monitoradmin',password="hqth")
    cur = con.cursor()
    cur.execute("""SELECT "Pri_IP", "Status" from monapp_host""")

    rows = cur.fetchall()
    wm = MyThread.WorkManager(2)

    for row in rows:
        print row
        ip, stat = row
        # # setStutus({'ip':ip})
        wm.add_job(setStutus, ip=ip, stat=stat)
        wm.start_thread_pool()
        wm.wait_allcomplete()

except psycopg2.DatabaseError, e:
    print 'Error %s' % e   
    sys.exit(1)

# import time
# time.sleep(10)
# finally:

#     if con:
#         con.close()