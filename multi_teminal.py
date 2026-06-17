import os
import sys
import subprocess

terminal=int(input("number of terminal:"))
current_path=sys.executable
print(current_path)
file_name=input("enter the file name:")
if not file_name in os.listdir():
    print("file not exists.....")
else:
    
    user_ip=[]
    for ter in range(terminal):
        start,end=input("enter how much data pass in your teminal:").split("-")
        user_ip.append((start,end))
        

    for ip in user_ip:
        subprocess.Popen(["start","cmd","/k",current_path,file_name,ip[0],ip[1]],shell=True)
       