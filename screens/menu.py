from screens import game
from ttkbootstrap import Button, Label, Frame, Style
from utils.utils import sound_path, icon_path
from PIL import Image, ImageTk
import tkinter as tk
import sys 
import pygame


pygame.mixer.init()
pygame.mixer.set_num_channels(32)

is_music_on = True
hover_channel = pygame.mixer.Channel(1)
hover_sound =  pygame.mixer.Sound(sound_path("hover.wav"))
hover_sound.set_volume(0.5)

click_channel = pygame.mixer.Channel(2)
click_sound = pygame.mixer.Sound(sound_path("click.wav"))
click_sound.set_volume(0.5)

musicC_channel = pygame.mixer.Channel(2)
musicC_sound = pygame.mixer.Sound(sound_path("musicbutton.wav"))
musicC_sound.set_volume(0.5)


def play_Music():
    
    pygame.mixer.music.load(sound_path("lobby.wav"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def stop_Music():
    pygame.mixer.music.stop()

def toggle_Music(music_btn):
    global is_music_on
    if is_music_on:
        stop_Music()
        music_btn.config(image=music_btn.icon_off)   
    else:
        play_Music()
        music_btn.config(image=music_btn.icon_on)
    
    is_music_on = not is_music_on

def on_enter(e, style):
    e.widget.config(bootstyle="info", style=style)
    hover_channel.play(hover_sound)

def on_leave(e, style):
    e.widget.config(bootstyle="danger", style=style)

def on_click(e):
    click_channel.play(click_sound)

def on_clickMusic(e):
    musicC_channel.play(musicC_sound)

def show_Menu(root):
   
    for widget in root.winfo_children():
        widget.destroy()


    if is_music_on:
        play_Music() 

    frame = Frame(root)
    frame.pack(expand=True)


    musicOnicon = ImageTk.PhotoImage(Image.open(icon_path("music.png")).resize((24, 24)))
    musicOfficon = ImageTk.PhotoImage(Image.open(icon_path("mute.png")).resize((24, 24)))

    music_btn = Button(
        root,
        image= musicOnicon if is_music_on else musicOfficon,
        bootstyle="secondary",
        width=3,
        command=lambda: toggle_Music(music_btn)
    )
    music_btn.icon_on = musicOnicon
    music_btn.icon_off = musicOfficon
    music_btn.place(relx=1.0, x=-10, y=10, anchor="ne")
    music_btn.bind("<Button-1>", on_clickMusic)
    
    title = Label(frame, text="Main Menu", font=("Richis Stiller", 64),  bootstyle="primary")
    title.pack(pady=(0,30))

    style = Style()
    style.configure(
    "Custom.TButton",
    font=("Richis Stiller", 20),
    foreground="white",
    background="#d9534f",  # warna normal (danger)
    bordercolor="#d43f3a",
    )

    style.map(
    "Custom.TButton",
    background=[
        ("active", "#5bc0de"),   # hover warna biru (info)
        ("!active", "#d9534f"),  # warna default (danger)
    ],
    foreground=[
        ("active", "white"),
        ("!active", "white")
    ]
    )


    customStyle = "Custom.TButton"
    startBtn = Button(
        frame, 
        text = "Start Game", 
        style= customStyle,
        width="20",
        padding="10",
        command=lambda: game.showGame(root)
        )
    startBtn.pack(pady=10)
    startBtn.bind("<Enter>", lambda e: on_enter(e, customStyle))
    startBtn.bind("<Leave>", lambda e: on_enter(e, customStyle))
    startBtn.bind("<Button-1>", on_click)

    exitBtn = Button(
        frame, 
        text = "Exit Game", 
        style=customStyle,
        width="20",
        padding="10",
        command=lambda: sys.exit()
        )
    exitBtn.pack(pady=10)
    exitBtn.bind("<Enter>", lambda e: on_enter(e, customStyle))
    exitBtn.bind("<Leave>", lambda e: on_enter(e, customStyle))
    exitBtn.bind("<Button-1>", on_click)

