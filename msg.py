import time
import pyautogui

count = 5
for i in range(count):
    print(count)
    time.sleep(1)
    count= count-1

for i in range(48):
    pyautogui.typewrite('Error 404')
    pyautogui.press('enter')
    time.sleep(1)

