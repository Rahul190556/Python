import time
from datetime import datetime as dt
host_temp="WebsiteBlocker/hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):  #if current time is in b/w this 
        print("Working Hour")                                                                                           #then we will enter in if loop
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
            
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun Hours...")          
    
    time.sleep(5)

# if we are in working hour then website in website_list will not work else it work

# To grant Visual Studio Code (VS Code) permission to access the host file on Windows, you need to run VS Code with administrative privileges. Here's how you can do it:

# Close VS Code if it's currently running.

# Right-click on the VS Code icon or the shortcut you use to launch it.

# From the context menu, select "Run as administrator". If prompted by User Account Control (UAC), click "Yes" to grant administrative privileges.

# VS Code will now open with elevated permissions, allowing it to access system files and folders, including the host file.