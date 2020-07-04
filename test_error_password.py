import datetime
from netmiko import *
import re

########### raise exception ##########
with open('hosts.txt') as f:
    devices = f.read().splitlines()

for hosts in devices:
    try:
        connect=ConnectHandler(device_type='cisco_xr', host=hosts, username='xr', password='123456')
        output = connect.send_command('show ip int brief')
        print(output)
        connect.disconnect()
    except NetMikoAuthenticationException as E:
        print(E)
        pass
############################################################

### OR ###

########### deal with different password ###################
with open('hosts.txt') as f:
    devices = f.read().splitlines()

for hosts in devices:
    if hosts == '192.168.100.109':
        connect=ConnectHandler(device_type='cisco_xr', host=hosts, username='xr', password='123456')
        output = connect.send_command('show ip int brief')
        print(output)
        connect.disconnect()
    else:
        connect=ConnectHandler(device_type='cisco_xr', host=hosts, username='xr', password='xr')
        output = connect.send_command('show ip int brief')
        print(output)
        connect.disconnect()
 ##############################################################
