#This program creates a folder in any directory (=C:\ as default) that you can put all your secret files into it
#Whenever you enter the password (="Password" as default) the status of the folder will change
#In secret status, it is shown as Recycle Bin and also its content
#Once you enter the password again, the status will change and you have access to your secret files!
#PARIKIA
# Import required modules
import base64
import os
import time
import sys

# Read the password from the file "PASSWORD.txt"
with open('PASSWORD.txt') as f:
    password = f.read()

# Read the location where the "Recycle bin" folder should be created from the file "LOCATION.txt"
with open('LOCATION.txt') as f:
    location = f.read()

# Replace backslashes with forward slashes in the location path
for x in location:
    if x == '\\':
        location = location.replace(x, '/')

# Store the password in the 'pw' variable for later comparison
pw = password

# Function to mimic the behavior of 'goto' in the script (not recommended in general)
def goto(linenum):
    global line
    line = linenum

# Starting point of the script
line = 1
while True:
    # Prompt the user to enter the password to convert the folder to Recycle Bin or vice versa
    pw = str(input("Enter the password to convert the folder to Recycle Bin or Recycle Bin to folder:\n"))

    # Check if the entered password matches the stored password
    if pw == password:
        # Change the current working directory to the specified location where the "Recycle bin" folder should be created
        os.chdir(location)

        # Check if the "Recycle bin" folder or its hidden counterpart exists
        if not os.path.exists("Recycle bin"):
            if not os.path.exists("Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}"):
                # If neither exists, create the "Recycle bin" folder and inform the user
                os.mkdir("Recycle bin")
                print('Recycle bin folder created successfully!')
                time.sleep(0.5)
                print('Now you can drop your secret files and folders into this "Recycle bin" folder')
                time.sleep(0.5)
                print("ATTENTION: You must NOT change the folder name")
                sys.exit()
            else:
                # If the hidden "Recycle bin" exists, make it visible and rename it to "Recycle bin"
                os.popen('attrib -h Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}')
                os.rename("Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}", "Recycle bin")
                print('The state of the secret folder has changed successfully')
                time.sleep(0.5)
                print('Check it out!')
                sys.exit()
        else:
            # If the visible "Recycle bin" exists, hide it and rename it to its hidden counterpart
            os.rename("Recycle bin", "Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h Recycle bin.{645ff040-5081-101b-9f08-00aa002f954e}')
            print('The state of the secret folder has changed successfully')
            time.sleep(0.5)
            print('Check it out!')
            sys.exit()
    else:
        # If the entered password is incorrect, inform the user and prompt for the password again
        print("Wrong password! Please try again")
        time.sleep(2)
        goto(1)  # Go back to the password input prompt
