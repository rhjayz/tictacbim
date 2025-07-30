import tkinter as tk
import pygame
from utils.utils import sound_path
from screens import splash
from ttkbootstrap.style import Style
from PIL import Image, ImageTk, ImageDraw, ImageColor

pygame.mixer.init()
pygame.mixer.set_num_channels(32)

def show_Image(root, image_path):

    root.configure(background="black")

    img = Image.open(image_path).convert("RGBA")

    min_dim = min(img.size)
    img = img.crop((
        (img.width - min_dim) // 2,
        (img.height - min_dim) // 2,
        (img.width + min_dim) // 2,
        (img.height + min_dim) // 2
    ))
    img = img.resize((500, 500))

    def playsound(path):
        intro = pygame.mixer.Channel(1)
        sound = pygame.mixer.Sound(path)
        intro.stop()
        intro.play(sound)

    def make_circle(img):
        size = img.size
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)

        draw.ellipse((0, 0, size[0], size[1]), fill=255)

        result = Image.new('RGBA', size)
        result.paste(img, (0, 0), mask = mask )
        border = ImageDraw.Draw(result)
        border.ellipse((0, 0, size[0]-1, size[1]-1), outline='white', width=4)
        
        return result
    
    canvas = tk.Canvas(root, width=img.width, height=img.height, bg = "black", highlightthickness=0)
    canvas.pack(expand=True)

    img_id = None
    delay = 8
    
    def fade_in(alpha = 0.0):
        nonlocal img_id

        if alpha == 0.0:
            playsound(sound_path("intro.wav")) 
        
        if alpha <= 1.0:
            faded = Image.new("RGBA", img.size, (0, 0, 0, 0))
            overlay = make_circle(img.copy())
            overlay.putalpha(int(alpha * 255))
            faded.paste(overlay, (0,0), overlay)

            photo = ImageTk.PhotoImage(faded)
            if img_id is not None:
                canvas.delete(img_id)
            img_id = canvas.create_image(img.width // 2, img.height // 2, image = photo)
            canvas.image = photo
            root.after(delay, lambda: fade_in(alpha + 0.05))
        else :
            root.after(2000, fade_out)

    def fade_out(alpha = 1.0):
        nonlocal img_id

        r1, g1, b1 = 0, 0, 0

        r2, g2, b2 = ImageColor.getrgb(Style().colors.bg)

        if alpha >= 0.0:
            faded = Image.new("RGBA", img.size, (0, 0, 0, 0))
            overlay = make_circle(img.copy())
            overlay.putalpha(int(alpha * 255))
            faded.paste(overlay, (0,0), overlay)

            photo = ImageTk.PhotoImage(faded)
            if img_id is not None:
                canvas.delete(img_id)
            img_id = canvas.create_image(img.width // 2, img.height // 2, image = photo)
            canvas.image = photo
            
            ratio = 1.19 - alpha
            r = int(r1 + (r2 - r1)* ratio)
            g = int(g1 + (g2 - g1)* ratio)
            b = int(b1 + (b2 - b1)* ratio)

            bg_hex =  f'#{r:02x}{g:02x}{b:02x}'
            root.configure(background = bg_hex)
            root.after(delay, lambda: fade_out(alpha - 0.05))
        else:
            canvas.destroy()
            root.configure(background=Style().colors.bg)
            splash.show_Splash(root)

    fade_in()