from logic.gamePlay import GameLogic
from screens import menu
from utils.utils import sound_path
from ttkbootstrap.widgets import Button, Label, Frame
from ttkbootstrap import Style
import tkinter as tk
import pygame


game = GameLogic()
buttons = []
status_label = None
pygame.mixer.init()
pygame.mixer.set_num_channels(32)


click_channel = pygame.mixer.Channel(2)
click_sound = pygame.mixer.Sound(sound_path("click.wav"))
click_sound.set_volume(0.5)

Gclick_channel = pygame.mixer.Channel(1)
Gclick_sound = pygame.mixer.Sound(sound_path("gameClick.wav"))
Gclick_sound.set_volume(0.5)

winning_channel = pygame.mixer.Channel(3)
winning_sound = pygame.mixer.Sound(sound_path("winning.wav"))
winning_sound.set_volume(0.5)

draw_channel = pygame.mixer.Channel(4)
draw_sound = pygame.mixer.Sound(sound_path("draw.wav"))
draw_sound.set_volume(0.5)

def soundTrackGame():
    pygame.mixer.music.load(sound_path("game.wav"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def onGameClick(e):
    Gclick_channel.play(Gclick_sound)

def on_click(e):
    click_channel.play(click_sound)

def onButtonClick(row, col):
    if game.make_move(row,col):
        buttons[row][col].config(text=game.board[row][col])
        if game.winner:
            status_label.config(text=f"{game.winner}'s Wins!", bootstyle="success")
            winning_channel.play(winning_sound)
        elif game.is_draw():
            status_label.config(text="Draw!", bootstyle="warning")
            draw_channel.play(draw_sound)
        else:
            status_label.config(text=f"{game.current_player}'s Turn", bootstyle="info")

def resetGame():
    global buttons, status_label
    game.reset()
    for row in range(3):
        for col in range(3):
            buttons [row][col].config(text="")
        status_label.config(text=f"{game.current_player}'s Turn", bootstyle="info")


def showGame(root):
    
    for widget in root.winfo_children():
        widget.destroy()

    global buttons, status_label

    soundTrackGame()

    frame = Frame(root)
    frame.pack(expand=True, fill="both")

    style = Style()

    style.configure("Back.TButton",
    font=("Arial", 14),
    background="#dc3545",  
    borderwidth=2,
    relief="solid"
    )

    style.map("Back.TButton",
    foreground=[("active", "#fff")],
    background=[("active", "#0d6efd")],
    relief=[("active", "solid")]
    )

    style.configure("Reset.TButton",
    font=("Arial", 20),
    background="#dc3545",  
    borderwidth=2,
    relief="solid"
    )

    style.map("Reset.TButton",
    foreground=[("active", "#fff")],
    background=[("active", "#0d6efd")],
    relief=[("active", "solid")]
    )

    style.configure("Game.TButton",
    font=("Arial", 25),
    foreground="#9f6eff",
    relief="solid"
    )

    back_btn = Button(root, text="⟵", bootstyle="info-outline", style="Back.TButton" ,command=lambda: menu.show_Menu(root))
    back_btn.place(x=10, y=10, width=40, height=40, anchor="nw")
    back_btn.bind("<Button-1>",on_click)

    label_frame = Frame(frame)
    label_frame.pack(pady=(30, 10), anchor="center")

    status_label = Label(frame, text="X's Turn", font=("Richis Stiller", 30), bootstyle="info")
    status_label.pack(pady=10, anchor="center")

    board_frame = Frame(frame)
    board_frame.pack(pady=30, anchor="center")

    cell_size = 150
    buttons = [[None for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            cell = tk.Frame(board_frame, width=cell_size, height=cell_size)
            cell.grid(row=row, column=col, padx=10, pady=10)
            cell.pack_propagate(False)

            btn = Button(
                cell,
                text="",
                style="Game.TButton",
                command=lambda r=row, c=col: onButtonClick(r, c)
            )
            btn.pack(fill="both", expand=True)
            btn.bind("<Button-1>",onGameClick)
            buttons[row][col] = btn

    control_frame = Frame(frame, width=80, height=80)
    control_frame.pack(pady=5, anchor="center")
    control_frame.pack_propagate(False) 

    reset_btn = Button(control_frame, text="⭯",style="Reset.TButton", bootstyle="danger-outline", command=resetGame)
    reset_btn.pack(fill="both", expand=True)
    reset_btn.bind("<Button-1>",on_click)

    