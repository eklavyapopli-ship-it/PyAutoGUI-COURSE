import pyautogui
import time
time.sleep(3)
# like Point(x=1237, y=725)
a=0
while a<10:
    pyautogui.moveTo(1237,725,1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.scroll(-10)
    a=a+1
