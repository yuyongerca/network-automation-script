
import sys
import os
from netmiko import ConnectHandler
import time
from netmiko import redispatch



while True:
    jumpserver = {
        "device_type": "terminal_server",
        "ip": "170.132.129.49",
        "username": "lc5544359",
        "password": input("please enter password:"),
        "global_delay_factor": 5}
    net_connect = ConnectHandler(**jumpserver)
    output = net_connect.find_prompt()
    print (output)

    net_connect.write_channel("ssh -l lc5544359 hopusbcr2\r\n")
    time.sleep(1)

    max_loops = 3
    i = 1
    while i <= max_loops:
        output = net_connect.read_channel()

        if 'password' in output:
            net_connect.write_channel("Bixinj0523lon((" + '\r\n')
            time.sleep(.5)
            output = net_connect.read_channel()
            print (output)
        # Did we successfully login
        if '>' in output or '#' in output:
            break

    net_connect.write_channel('\r\n')
    time.sleep(.5)
    redispatch(net_connect, device_type='cisco_ios')

    # Now just do your normal Netmiko operations
    new_output = net_connect.send_command("show ip accounting")
    print (new_output)
    with open("ip_accounting.txt", "a") as file1:
        file1.write(new_output +"\n")
        file1.close()

    new_output = net_connect.send_command("clear ip accounting")
    print (new_output)
    redispatch(net_connect, device_type="terminal_server")
   # output = net_connect.read_channel()
    output_1 = net_connect.find_prompt()
   # print (output)
    print (output_1)
   # net_connect.disconnect()
    time.sleep(3600)















