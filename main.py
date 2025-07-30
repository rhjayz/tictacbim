import ttkbootstrap as tb
from screens import prod
from utils.utils import image_path

if __name__ == "__main__":
    app = tb.Window(themename="vapor")
    app.attributes('-fullscreen', True)
    prod.show_Image(app, image_path("rjstudio.png"))
    app.mainloop()