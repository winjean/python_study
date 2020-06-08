#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import paramiko
import time

ip = "10.20.4.61"
username = "lsmsp"
password = "Lsmsp!234Abcd"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=password)

print(f"Sucessfully login to {ip}")


command = ssh_client.invoke_shell()
command.send("sudo su -\n")
command.send("cd /home/lsmsp/asc\n")
# command.send("cp nohup.out n.o  \n")


# time.sleep(1)
# output = command.recv(65535)
# print(f"return: {output} \n")
#
# time.sleep(1)
# output = command.recv(65535)
# print(f"return: {output} \n")

# command.send("ls \n")
time.sleep(1)
output = command.recv(65535)
# print(f"return: {output} \n")

ssh_client.close
print(f"Sucessfully logout from {ip}")
