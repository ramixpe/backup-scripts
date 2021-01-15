import os
from datetime import datetime
from netmiko import ConnectHandler, NetMikoTimeoutException

if not os.path.exists('Output-Configs'):
    os.makedirs('Output-Configs')

now = datetime.now()
dt_string = now.strftime("%m-%d-%Y_%H-%M")

def get_saved_config(host, username, password):
    cisco_ios = {
        'device_type': 'cisco_xr',
        'host': host,
        'username': username,
        'password': password,
    }
    # Creates the connection to the device.
    net_connect = ConnectHandler(**cisco_ios)
    # Gets the running configuration.
    output = net_connect.send_command("show running-config")
    # Gets and splits the hostname for the output file name.
    hostname = net_connect.find_prompt()
    hostname = hostname.split(':')
    hostname = hostname[1].replace('#','')
    # # Creates the file name, which is the hostname, and the date and time.
    fileName = 'Device'+'_' + hostname + "_" + dt_string
    # # Creates the text file in the Output-Configs folder with the special name, and writes to it.
    backupFile = open("Output-Configs/" + fileName + ".txt", "w+")
    backupFile.write(output)
    print("Outputted to " + fileName + ".txt!")


for line in open('hosts.txt'):
    try:
        get_saved_config(line,'xr','123456')
    except NetMikoTimeoutException as e:
            print(line + 'is not online')
