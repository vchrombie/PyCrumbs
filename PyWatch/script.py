import pyautogui
import os, datetime
import getpass

global access

def main():
    global pwd
    pwd = getpass.getpass('Password:')
    print("The device is LOCKED\n"),
    global pswd
    pswd = ''
    while True:
        lock()
        pswd = input("Enter the password\n")
        access =  check(pswd)
        if access==True:
            break
        mousecheck()
    return

def mousecheck():
    x, y = pyautogui.position()
    if (x == 400 and y == 400):
        print('3')
    else:
        os.system('python2 simplecam.py')

def lock():
    pyautogui.moveTo(400, 400, duration=0.1)

def check(cpwd):
    if (cpwd == pwd):
        return True
    else:
        return False

pyautogui.PAUSE = 1
pyautogui.FAILSAFE=False

try:
    main()
except KeyboardInterrupt:
    print('/nDone.')
