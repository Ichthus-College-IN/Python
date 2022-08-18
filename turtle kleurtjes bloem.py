import turtle

s = turtle.getscreen()
t = turtle.Turtle()

colors = ["red", "coral", "orange", "gold", "yellow", "yellow green", "green", "forest green", "spring green", "turquoise", "royal blue", "blue", "navy", "purple", "violet", "pink", "magenta", "violet red"]

def petal(r, ang):
    for _ in range(2):
        t.circle(r, ang)
        t.lt(180 - ang)

def flower(n, r, ang, use_colors):
    for i in range(n):
        if use_colors == True:
            t.pencolor(colors[i])
        else:
            t.pencolor("black")
        petal(r, ang)
        t.lt(360 / n)

t.speed(0)

flower(len(colors), 150, 50, use_colors = True)
flower(len(colors), 75, 50, use_colors = False)

turtle.mainloop()