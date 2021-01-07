import paramiko
import time
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = {'hostname': '10.1.1.10','port': '22','username': 'u1','password': 'cisco'}
print(f'Connection to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
shell = ssh_client.invoke_shell()

shell.send('enable\n')
shell.send('cisco\n')
shell.send('conf t\n')
shell.send('router ospf 1\n')
shell.send()
shell.send()
shell.send()
shell.send()
shell.send()
shell.send()
shell.send()



if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()