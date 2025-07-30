import tkinter as tk
from tkinter import font

root = tk.Tk()
fonts = font.families()

for f in fonts:
    if "rich" in f.lower() or "stiller" in f.lower():
        print(f)

root.destroy()
