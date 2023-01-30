# Import
import win32clipboard
from pynput import keyboard
import time

def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def on_press(key):
    if key == keyboard.Key.ctrl_r:
        typing = keyboard.Controller()
        text = get_clipboard()
        print(text)
        time.sleep(0.3)
        typing.type(text)
    

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()