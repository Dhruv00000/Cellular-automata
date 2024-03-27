from turtle import Screen, Turtle

window = Screen()
window.bgcolor('black')
window.screensize(1024, 1024)

grid: dict = {}

ant: Turtle = Turtle()
ant.shape('square')
ant.shapesize(0.5)
ant.speed(1000)

position: tuple = (round(ant.xcor()), round(ant.ycor()))
while True:

    if position not in grid or grid[position] == "black":

        ant.fillcolor('#fff')
        ant.stamp()
        grid[(round(ant.xcor()), round(ant.ycor()))] = "white"
        ant.right(90)

    else:

        ant.fillcolor('#000')
        ant.stamp()
        grid[(round(ant.xcor()), round(ant.ycor()))] = "black"
        ant.left(90)
        
    ant.forward(10)
    position = (round(ant.xcor()), round(ant.ycor()))