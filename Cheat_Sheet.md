# Cheat Sheet

## General Python cheat sheet

| Code | Description |
|------|-------------|
| `def function():`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Method stuff` | Create a method, no brackets only a colon and indents |
| `variable1, variable2 = value1, value2` | Variables do not need datatypes and can be set in one line, no semicolon needed |
| `if condition == this or other >= this:` | Conditionals don’t need parenthesis |

## Turtle cheat sheet

| Code | Description |
|------|-------------|
| `turtle.forward(int)` | Move **forward** this many pixels |
| `turtle.back(int)` | Move **backward** this many pixels |
| `turtle.right(float)` | Turn this many degrees **right** |
| `turtle.left(float)` | Turn this many degrees **left** |
| `turtle.penup()` | **Stops** turtle from drawing lines as it moves |
| `turtle.pendown()` | **Starts** turtle drawing as it moves |
| `turtle.goto(x, y)` | Turtle goes to a **set coordinate** |
| `turtle.done()` | **Stops** turtle program |
| `turtle.speed(int)` | Sets the **speed** of drawing (0 is the fastest) |

## DVD Logo cheat sheet

| Code | Description |
|------|-------------|
| `root = tkinter.Tk()` | Tell the program it will open a **window**. Needs to be set to a variable, usually **root** |
| `tkinter.Canvas(root, width=800, height=500, bg="black")` | Set up a **canvas** to draw on inside the window. Also needs to be assigned to a variable, usually **canvas** |
| `canvas.pack()` | Places the **canvas** inside the window |
| `canvas.create_rectangle(x1, y1, x2, y2)` | Makes a **box** on screen between two given points |
| `global x` | Needed inside a function for any variables (x) the function needs to **change** the value of |
| `canvas.coords(box, x1, y1, x2, y2)` | Moves your **box** in the window |
| `root.after(int, function)` | Runs the **function** again after a certain amount of milliseconds (**int**) |
