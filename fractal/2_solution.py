import turtle

TRIANGLE_SIDE = 380 #side length of the biggest triangles
RUNS = 6            #how many levels deep the fractal goes

#draws one triangle and ends where it started, facing the same way
def triangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)

def fractal(length, depth):
    #base case: stop once we've gone deep enough
    if depth == 0:
        return

    #bottom left triangle, then a smaller fractal inside it
    triangle(length)
    fractal(length / 2, depth - 1)

    #bottom right triangle, then a smaller fractal inside it
    turtle.forward(length)
    triangle(length)
    fractal(length / 2, depth - 1)

    #move up to the top triangle and turn to face right
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.right(180)
    fractal(length / 2, depth - 1)

    #go back to where we started, facing the same way
    turtle.right(120)
    turtle.forward(length)
    turtle.left(120)

def main():
    turtle.speed(0) #fastest drawing speed
    turtle.penup()
    turtle.goto(-190, -180) #bottom left of the drawing
    turtle.pendown()
    fractal(TRIANGLE_SIDE, RUNS)
    turtle.done()

main()
