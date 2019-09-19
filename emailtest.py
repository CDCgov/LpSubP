# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:31:02 2019

@author: nej1
"""

import smtplib
import mimetypes
from email.message import EmailMessage
import os
import sys

base_dir=sys.argv[1]
os.chdir(base_dir+"/outputfiles")

msg=EmailMessage()
msg['Subject']="LpsubP result files"
msg['From'] = "nej1@cdc.gov"
msg['To'] = "nej1@cdc.gov"
msg.preamble="LpsubP result files for"+str(sys.argv[1].split("/")[::-1][0])

message = """
Attached are the outputfiles from LpSubP.
The general explanation for each file is also attached("output_explanation.txt").
Let me know if you have any questions.
Thanks,
Subin
"""

msg.set_content(message)

for file in os.listdir("."):
    path=os.path.join(".",file)
    if not os.path.isfile(path):
        continue
    ctype,encoding = mimetypes.guess_type(path)
    if ctype is None or encoding is not None:
        ctype="application/octet-stream"
    maintype,subtype=ctype.split('/',1)
    with open(path,'rb') as fp:
        msg.add_attachment(fp.read(),maintype=maintype,subtype=subtype,filename=file)
        #msg.attach(fp.read())
    
with smtplib.SMTP('localhost')as s:
     s.send_message(msg)

    
     
     