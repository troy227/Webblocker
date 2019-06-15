##########################
""" WEBSITE BLOCKER      
MADE BY: TUSHAR ROY     
TROY2271999@GMAIL.COM"""
##########################
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
weblist=["www.facebook.com","facebook.com"]
from datetime import datetime as dt
import time


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,21):
        print("Working Hours")
        with open(host_path,'r+') as file:
            content=file.read()
            
            for w in weblist:
                if w not in content:
                    file.write("\n")
                    file.write(redirect+' '+w)
        time.sleep(60)

    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in weblist):
                    file.write(line)
            file.truncate()
                        
        print("Fun Time")
        time.sleep(60)
    
