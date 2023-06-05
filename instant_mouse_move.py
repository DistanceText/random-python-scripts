import win32api, random

x = random.randint(0, 1920)

y = random.randint(0, 1080)

win32api.SetCursorPos((x, y))