import datetime
from netmiko import *
import re


#getting the commands from the file
with open("commands.txt") as cmd_file:
    commands = cmd_file.readlines()
#getting the hosts IPs
with open('hosts.txt') as f:
    devices = f.read().splitlines()

for hosts in devices:
    for cmd in commands:
        connect = ConnectHandler(device_type='cisco_xr', host=hosts, username='xr', password='xr')
        output = connect.send_config_set(cmd)
        print("writing the command : " + str(cmd), "to router" +str(hosts))
        print ("commiting the change" + connect.commit())
        connect.disconnect()
        
        
        
###### push commands from File #######
# for hosts in devices:
#     connect = ConnectHandler(device_type='cisco_xr', host=hosts, username='xr', password='xr')
#     output = connect.send_config_from_file("commands.txt")
#     # print("writing the command : " + str(cmd), "to router" +str(hosts))
#     connect.commit()
#     connect.disconnect()
