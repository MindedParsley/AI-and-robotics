import os
from guizero import App, PushButton, Text, Box, Picture
from playsound import playsound
import random

Base_DIR = os.path.dirname(os.path.abspath(__file__))

app = App(title="3x3 Button Grid", width=500, height=400, layout="grid", bg= "#00ffff")
sounds = [
    os.path.join(Base_DIR, "Arnie", "sound1.wav"),
    os.path.join(Base_DIR, "Arnie", "sound2.wav"),
    os.path.join(Base_DIR, "Arnie", "sound3.wav"),
    os.path.join(Base_DIR, "Arnie", "sound4.wav"),
    os.path.join(Base_DIR, "Arnie", "sound5.wav"),
    os.path.join(Base_DIR, "Arnie", "exit.wav"),]
photo = os.path.join(Base_DIR, "Arnie", "picture.png")

def play(num):
    playsound(sounds[num])

def grow(button):
    button.width = 15
    button.height = 3

def shrink(button):
    button.width = 12
    button.height = 2

box = Box(app,grid=[0,0,1,3],width=100,height="fill")
box = Box(app,grid=[1,0,3,1],width=300,height=75,border=0)
text = Text(box, text="Arnie Sound Board",underline=True,bold=True,size=25)


for row in range(2):
    for col in range(3):
        hexColour = hex(random.randint(0,2**24))
        button = PushButton(
            app,
            command= play,
            args= [(row * 3 + col)],
            text=f"Button {row * 3 + col + 1}",
            grid=[col+1, row+1],
            width=12,
            height=2,
            pady=1,
            padx=1,
        )
        button.bg = f"#{hexColour[2:]}"

        button.tk.bind(
            "<Enter>",
            lambda event, b=button: grow(b)
        )

        button.tk.bind(
            "<Leave>",
            lambda event, b=button: shrink(b)
        )

button = PushButton(
    app,
    command= play,
    args=[5],
    text=f"Button {row * 3 + col + 1}",
    grid=[2,3],
    width=12,
    height=2,
    pady=1,
    padx=1,
)
button.bg = f"#{hexColour[2:]}"

button.tk.bind(
    "<Enter>",
    lambda event, b=button: grow(b)
)

button.tk.bind(
    "<Leave>",
    lambda event, b=button: shrink(b)
)

picture = Picture(
    app,
    grid = [1,4,3,3],
    image= photo
)

app.display()