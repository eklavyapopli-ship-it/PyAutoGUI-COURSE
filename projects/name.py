import pyautogui
import time


time.sleep(3)
def lettter_E():
    pyautogui.dragRel(0,-50,1,button="left")
    pyautogui.dragRel(30,0,1, button="left")
    pyautogui.moveRel(0,25)
    pyautogui.dragRel(-30,0,1, button="left")
    pyautogui.moveRel(0,25)
    pyautogui.dragRel(30,0,1, button="left")

def letter_K():
    pyautogui.moveRel(20,-50)
    pyautogui.dragRel(0,50,1,button="left")
    pyautogui.moveRel(0,-25)
    pyautogui.dragRel(20,-25, button="left")
    pyautogui.moveRel(-20,25)
    pyautogui.dragRel(20,25, button="left")

lettter_E()
letter_K()
pyautogui.moveTo(26,65,3)
pyautogui.click()