from django.contrib import admin

from apps.monapp.models import Host, HostGroup

# class HostGroupAdmin(admin.ModelAdmin):
#     fields = ['GroupName', 'GroupID']

# class HostAdmin(admin.ModelAdmin):
#     fields = ['HostName', 'Pri_IP']

admin.site.register(HostGroup)
admin.site.register(Host)