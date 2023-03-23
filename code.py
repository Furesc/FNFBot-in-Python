import pyautogui
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

posy = 100

print("FnfBot By Furesc")
while True:
    if pyautogui.pixelMatchesColor(880, posy, (194, 75, 153)):
        keyboard.press("a")
        time.sleep(0.1)
        keyboard.release("a")

    if pyautogui.pixelMatchesColor(1000, posy, (0, 255, 255)):
        keyboard.press("s")
        time.sleep(0.1)
        keyboard.release("s")

    if pyautogui.pixelMatchesColor(1120, posy, (18, 250, 5)):
        keyboard.press("w")
        time.sleep(0.1)
        keyboard.release("w")

    if pyautogui.pixelMatchesColor(1240, posy, (249, 57, 63)):
        keyboard.press("d")
        time.sleep(0.1)
        keyboard.release("d")
        
#Before you need to install these apis:
#1.- pyautogui
#2.- pynput