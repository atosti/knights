import ctypes  # Used for mouse movements
# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details

# For cross-platform mouse and keyboard commands: https://github.com/asweigart/pyautogui
#   -Though I've read this is significantly slower than PyUserInput
# For a faster alternative: https://github.com/SavinaRoja/PyUserInput
#   -This actually looks better and is cross-platform as well

def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up