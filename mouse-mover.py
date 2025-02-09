import pyautogui
import time
import random

def move_mouse():
    while True:
        x, y = pyautogui.position()
        new_x = x + random.randint(-10, 10)
        new_y = y + random.randint(-10, 10)
        pyautogui.moveTo(new_x, new_y, duration=0.2)
        time.sleep(2)

if __name__ == "__main__":
    move_mouse()