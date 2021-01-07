import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

router = {'hostname': '10.1.1.10','port': '22','username': 'u1','password': 'cisco'}
print(F'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
sheel.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(10000)
print(type(output))
output = output.decode("utf-8")
print(output)


#sending commands

if ssh_client.get_transport().is_active() == True:
    print("Closing connection")
    ssh_client.close()