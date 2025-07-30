import sys
import os

def resource_path(relative_path):
    try:
        return os.path.join(sys._MEIPASS, relative_path)
    except AttributeError:
        return os.path.join(os.path.abspath("."), relative_path)

def sound_path(name):
    return resource_path(f"assets/sound/{name}")

def image_path(name):
    return resource_path(f"assets/image/{name}")

def icon_path(name):
    return resource_path(f"assets/icon/{name}")

def font_path(name):
    return resource_path(f"assets/font/{name}")
