from netmiko import ConnectHandler
import json

with open('hosts.txt') as f:
    device = f.read().splitlines()

try:
    for router in device:
        c = ConnectHandler(device_type='cisco_xr', host=router, username='xr', password='xr')
        interfaces = c.send_command('show interface', use_textfsm=True)
        # print(json.dumps(interfaces, indent=4))
        print(f" connecting to router  {c.find_prompt()}")
        for link in interfaces:
            if link['link_status'] == 'up':
                print(f" {link['interface']}  is UP!")
            else:
                print(f" {link['interface']}  is Down!")
except Exception as e:
    print(e)
