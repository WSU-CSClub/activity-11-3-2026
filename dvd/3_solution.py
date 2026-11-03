import random
import tkinter

#customize here!
WIDTH, HEIGHT = 640, 400
BOX_WIDTH, BOX_HEIGHT = 100, 50
SPEED = 3
COLOR = "#4dc3ff"
BACKGROUND_COLOR = "black"
TEXT_IN_BOX = "DVD"
TEXT_COLOR = "black"
FONT = "Helvetica"
FONT_SIZE = 22
FONT_STYLE = "bold"

root = tkinter.Tk() #window
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack() #places the canvas inside the window

#start the box at a random spot
x = random.randint(0, WIDTH - BOX_WIDTH)
y = random.randint(0, HEIGHT - BOX_HEIGHT)
x_change, y_change = SPEED, SPEED

box = canvas.create_rectangle(x, y, x + BOX_WIDTH, y + BOX_HEIGHT, fill=COLOR, outline="")
label = canvas.create_text(x + BOX_WIDTH / 2, y + BOX_HEIGHT / 2, text=TEXT_IN_BOX,
                           font=(FONT, FONT_SIZE, FONT_STYLE), fill=TEXT_COLOR)

def step():
    global x, y, x_change, y_change
    x = x + x_change
    y = y + y_change

    #bounce off the left or right edge, and keep the box inside the window
    if x <= 0 or x + BOX_WIDTH >= WIDTH:
        x_change = -x_change
        x = max(0, min(x, WIDTH - BOX_WIDTH))
    #bounce off the top or bottom edge, and keep the box inside the window
    if y <= 0 or y + BOX_HEIGHT >= HEIGHT:
        y_change = -y_change
        y = max(0, min(y, HEIGHT - BOX_HEIGHT))

    #move the box and the text together
    canvas.coords(box, x, y, x + BOX_WIDTH, y + BOX_HEIGHT)
    canvas.coords(label, x + BOX_WIDTH / 2, y + BOX_HEIGHT / 2)
    root.after(16, step) #after 16 milliseconds, run step again

step() #starts program
root.mainloop() #keeps window open
