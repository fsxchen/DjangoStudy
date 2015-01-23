from django.db import models

# Create your models here.

class OsCtag(models.Model):
    CtagName = models.CharField(default="ubuntu12.04", max_length=20)
    CtagType = models.SmallIntegerField(default=0,choices=((0,u'64'),(1,u'32'), (2, "OTHER")),)
    Description = models.TextField()
    def __unicode__(self):
        return unicode(self.CtagName)


class HostGroup(models.Model):
    GroupName = models.CharField(max_length=50,default='YXC')
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
    CtagID = models.ForeignKey(OsCtag)
    UserName = models.CharField(default='root',max_length=15)
    Password = models.CharField(max_length=50,blank = True)
    Region = models.CharField(default='Beijing',max_length=20)
    Status = models.SmallIntegerField(default=0,choices=((0,u'OFF'),(1,u'ON')),)

    def __unicode__(self):
        return unicode(self.HostName)

