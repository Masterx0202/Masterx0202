import os
import time
import pyautogui
import save


def name():
    firmname = input("namen:")
    street = input("Strassen namen 1:")
    street2 = input("Strassen namen 2:")
    return firmname, street, street2

name()
os.startfile("C:/Users/User/Documents/berufswahl/Bewerbungsdossier/Bewerbungschreiben/Informatiker/Bewerbungsschreiben Vorlage.docx")
time.sleep(8)
str = pyautogui.locateOnScreen('str.jpg', grayscale=False, confidence=.7)
str = pyautogui.center(str)
pyautogui.click(str)
time.sleep(0.5)
pyautogui.doubleClick(str)
pyautogui.press("del")

pyautogui.write(firmname)
pyautogui.keyDown("shiftleft")
pyautogui.press("enter")
pyautogui.keyUp("shiftleft")
pyautogui.write(street)
pyautogui.keyDown("shiftleft")
pyautogui.press("enter")
pyautogui.keyUp("shiftleft")
pyautogui.write(street2)

nme = pyautogui.locateOnScreen('name.jpg', grayscale=False, confidence=.7)
nme = pyautogui.center(nme)
pyautogui.click(nme)
time.sleep(0.5)
pyautogui.doubleClick(nme)
pyautogui.press("del")
pyautogui.write(firmname)

save.save(firmname)