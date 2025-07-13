# https://test.rebex.net/
import paramiko

# pip install paramiko

# połaczenia sftp, ssh  z serwerami

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# sftp demo@test.rebex.net - sprawdzenie poączenia
client.connect('test.rebex.net',
               port=22,
               username='demo',
               password='password',
               look_for_keys=False,
               allow_agent=False
               )
# może być wymagane na linux/unix
#   look_for_keys=False,
#   allow_agent=False
sftp = client.open_sftp()
file_list = sftp.listdir()
print(file_list)  # ['pub', 'readme.txt']

# sftp.get('readme.txt', 'readme.txt')
sftp.get('readme.txt', '../readme.txt')

with open('kg.png', 'wb') as local_file:
    sftp.getfo('pub/example/KeyGenerator.png', local_file)

sftp.close()
client.close()
