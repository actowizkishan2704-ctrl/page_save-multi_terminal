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
    

    for ter in range(terminal):

        try:
            subprocess.Popen(["start","cmd","/k",current_path,file_name],shell=True)
        except Exception as e:
            print(str(e))
