import random, pyautogui

x = random.randint(0, 1920)

y = random.randint(0, 1080)

duration = random.randint(1, 10) * 0.1
 
pyautogui.moveTo(x, y, duration)