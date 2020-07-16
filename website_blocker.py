import time
from datetime import datetime as dt
temp_path = "hosts"
host_path="/private/etc/hosts"
redirect="127.0.0.1"
website_lists=["twitter.com","www.twitter.com","www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
        print("working hours...")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()
        print("fun hours......")
    time.sleep(5)
