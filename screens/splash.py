from ttkbootstrap import Label
from screens import menu
from utils.utils import sound_path
import tkinter as tk
import pygame
from ttkbootstrap.style import Style

def show_Splash(root):
    root.configure(background=Style().colors.bg)

    full_text = "Tic-Tac-Bim"
    current_text = tk.StringVar()

    splash = Label(root, textvariable=current_text, font=("Richis Stiller", 100), bootstyle="info")
    splash.pack(expand=True)

    def playsound(path):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(path)
        sound.play()


    def anime(index = 0):
        if index <= len(full_text):
            current_text.set(full_text[:index])      
            root.after(500, lambda: anime(index + 1))
            playsound(sound_path("type.wav"))

    def fade_Text(steps=20, current=0):
        brightness = int(255 * current / steps)
        hex_color = f"#{brightness:02x}{brightness:02x}{brightness:02x}"
        splash.configure(foreground=hex_color)

        if current < steps:
            root.after(100, lambda: fade_Text(steps, current + 1))
        else:
            splash.destroy()
            menu.show_Menu(root)
    
    anime()

    root.after(6500, fade_Text)