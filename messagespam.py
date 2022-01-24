import pyautogui
import time

# the 5 seconds for you to escape from spamming yourself lol
time.sleep(5)

# enter the name of the file which contains the spamming text
f = open("puli-script.txt", 'r')
for vaarthai in f:
    pyautogui.typewrite(vaarthai)
    pyautogui.press("enter")
