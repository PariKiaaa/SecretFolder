#This program creates a folder in any directory (=C:\ as default) that you can put all your secret files into it
#Whenever you enter the password (="PariKia" as default) the status of the folder will change
#In secret status, it is shown as Recycle Bin and also its content
#Once you enter the password again, the status will change and you have access to your secret files!
#MADE BY PARIKIA

import base64
import os
import time
import sys
with open('PASSWORD.txt') as f:
    password = f.read()
with open('LOCATION.txt') as f:
    location = f.read()
for x in location:
    if x=='\\':
        location=location.replace(x,'/')

pw = password
def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    pw = str(input("Enter the password to convert the folder to recycle bin or recycle bin to folder:\n"))
    if pw == password:
    # Change dir Path where you have Recycle bin Folder
        os.chdir(location)
    # If Recycle bin folder or Recycle bin does not exist then we will create Recycle bin Folder 
        if not os.path.exists("Recycle bin"):
            if not os.path.exists("Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Recycle bin")
                print('Recycle bin folder created successfully!')
                time.sleep(0.5)
                print('Now you can drop your secret files and folders to this "Recycle bin folder"')
                time.sleep(0.5)
                print("ATTENTION: You must NOT change the folder name")
                sys.exit()
            else:
                os.popen('attrib -h Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}')
                os.rename("Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}","Recycle bin")
                print('The state of the secret folder has changed successfully')
                time.sleep(0.5)
                print('Check it out!')
                sys.exit()
        else:
            os.rename("Recycle bin","Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}')
            print('The state of the secret folder has changed successfully')
            time.sleep(0.5)
            print('Check it out!')
            sys.exit()
        
    else:
        print("Wrong password! Please try again")
        time.sleep(2)
        goto(1)
