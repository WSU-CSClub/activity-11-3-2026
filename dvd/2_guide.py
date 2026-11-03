import tkinter

WIDTH, HEIGHT = 800, 500        #size of the window
BOX_WIDTH, BOX_HEIGHT = 100, 50 #size of the box

root = tkinter.Tk() #window
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack() #places the canvas inside the window

x, y = 100, 100 #starting point or position
x_change, y_change = 3, 3 #SPEED, how many pixels it moves
box = canvas.create_rectangle(x, y, x + BOX_WIDTH, y + BOX_HEIGHT) #top left to bottom right

def step():
    global x, y, x_change, y_change #function can change these variables
    #how to move the box
    x = x + x_change
    y = y + y_change
    #bounce off the left or right edge
    if x <= 0 or x + BOX_WIDTH >= WIDTH:
        x_change = -x_change
    #bounce off the top or bottom edge
    if y <= 0 or y + BOX_HEIGHT >= HEIGHT:
        y_change = -y_change
    canvas.coords(box, x, y, x + BOX_WIDTH, y + BOX_HEIGHT) #actually moves the box
    root.after(16, step) #after 16 milliseconds, run step again

step() #starts program
root.mainloop() #keeps window open
