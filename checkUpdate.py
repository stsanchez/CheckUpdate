from smb.SMBConnection import SMBConnection
import os, sys
import time
import datetime
from datetime import timedelta
import os
import functions

#SET PARAMETERS AND MAKE THE CONNECTION WITH THE SMB PROTOCOL
userId = 'USER'
password = 'PASSWORD'
client_machine_name = 'MYMACHINE'
server_name = 'SERVER'
server_ip ='1.1.1.1'
path = 'PATH'
domain_name = 'LOCAL'

conn = SMBConnection(userId, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
conn.connect(server_ip, 445)

#LIST ALL FILES IN THE DIRECTORY
filelist = conn.listPath(path,'/')

#SET DATE FORMATS
now = datetime.datetime.now()
date_time = now.strftime("%Y%m%d%H")
minute = now.strftime("%M")
date_time_2 = (now - timedelta(hours=1)).strftime("%Y%m%d%H")

#ASSIGN THE LAST FILE TO THE VARIABLE TO COMPARE
last_file = (filelist[-3].filename[0:10])

#COMPARE IF THE MINUTE IS LESS THAN 30
if int(minute) < 30:
    if date_time_2 != (filelist[-3].filename[0:10]):
       functions.sendMail(last_file)
    else:
        pass
        
#I COMPARE IF THE MINUTE IS GREATER THAN 30
elif date_time != (filelist[-3].filename[0:10]):
    functions.sendMail(last_file)
else:
    pass
        
conn.close()
