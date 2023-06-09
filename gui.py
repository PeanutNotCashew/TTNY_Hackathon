
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, customtkinter, Canvas, Entry, Text, Button, PhotoImage # custom gives us more functionality, better reflecting the original wireframe

customtkinter.set_appearance_mode("System") # nothing i hate more than a screen suddenly nuking my retinas when i'm on dark mode
                                            # note that this does nothing on non macOS systems

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("375x667")
window.configure(bg = "#F1D9B5")

canvas = Canvas(
    window,
    bg = "#F1D9B5",
    height = 667,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    50.0,
    60.0,
    anchor="nw",
    text="welcome to a new way to budget!",
    fill="#000080",
    font=("IBMPlexMono Regular", 35 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    192.5,
    323.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=55.0,
    y=308.0,
    width=275.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    192.5,
    253.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=55.0,
    y=238.0,
    width=275.0,
    height=28.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=122.0,
    y=378.0,
    width=130.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=138.0,
    y=440.0,
    width=98.0,
    height=23.0
)
window.resizable(True, True)
window.mainloop()
