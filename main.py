import pyautogui
import pyperclip
import time
import platform
import win32gui

from Launcher import WindowsLauncher
from Bundle import Bundle

launcher = WindowsLauncher()
bundle = Bundle()

launcher.launch(bundle)
