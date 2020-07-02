
import datetime
from netmiko import *
import re


#getting the commands from the file
with open("commands.txt") as cmd_file:
    commands = cmd_file.readlines()
#getting the hosts IPs
with open('hosts.txt') as f:
    devices = f.read().splitlines()

#starting the job
for data in devices:
    #simple connect
    connect = ConnectHandler(device_type='cisco_xr', host=data, username='xr', password='xr')
    #getting the host name
    txt = connect.find_prompt()
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '(?:[a-z][a-z]*[0-9]+[a-z0-9]*)'  # Uninteresting: alphanum
    re3 = '.*?'  # Non-greedy match on filler
    re4 = '((?:[a-z][a-z]*[0-9]+[a-z0-9]*))'  # Alphanum 1
    rg = re.compile(re1 + re2 + re3 + re4, re.IGNORECASE | re.DOTALL)
    m = rg.search(txt)
    host_name = m.group(1)
    ##constructing the file name
    today = datetime.datetime.today()
    today_date = str(getattr(today, 'year')) + str(getattr(today, 'month')).zfill(2) + str(getattr(today, 'day')).zfill(2)
    today_time = str(getattr(today, 'hour')).zfill(2) + str(getattr(today, 'minute')).zfill(2) + str(getattr(today, 'second')).zfill(2)
    myfilename_out_ext = 'txt'
    myfilename_out_suffix = today_date + '_' + today_time
    ##generating the file
    output_file =  host_name+"_" + myfilename_out_suffix + '.' + myfilename_out_ext
    ##pulling the commands outout
    print("connecting to device: " + str(data))
    with open(output_file, 'w') as file:
        for i in commands:
            output = connect.send_command(i)
            print("getting the command : " + str(i))
            file.write(output + '\n')
    connect.disconnect()
