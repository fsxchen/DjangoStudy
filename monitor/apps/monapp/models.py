from django.db import models

# Create your models here.

class HostGroup(models.Model):
    GroupName = models.CharField(max_length=50,default='IZPGroup')
    GroupID = models.IntegerField(max_length=5,default=0,primary_key=True)
    Description = models.TextField()

    def __unicode__(self):
        return unicode(self.GroupName)


class Host(models.Model):
    GroupID = models.ForeignKey(HostGroup)
    HostName = models.CharField(max_length=50)
    Pri_IP = models.IPAddressField(blank = True)
    Pub_IP = models.IPAddressField(blank = True)
    Serial = models.CharField(max_length=25,primary_key=True)
    OsType = models.CharField(default='CentOS6',max_length=10)
    UserName = models.CharField(default='root',max_length=15)
    Password = models.CharField(max_length=50,blank = True)
    Region = models.CharField(default='Beijing',max_length=20)
    Status = models.SmallIntegerField(default=1,choices=((0,u'OFF'),(1,u'ON')),)

    def __unicode__(self):
        return unicode(self.HostName)