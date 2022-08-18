import turtle

class player:
    def __init__(self, x, y, color):
        self.t = turtle.Turtle()    # nieuwe turtle
        self.t.up()                 # pen van papier halen
        self.t.goto(x, y)           # naar startpositie gaan
        self.t.down()               # pen weer op papier zetten
        self.t.pencolor(color)      # penkleur instellen
        self.levens = 3             # je start met drie levens

    def fd(self, p1, p2):           # functie om vooruit te gaan
        self.t.forward(10)
        if collision(p1, p2) == True:       # controlleer botsing
            self.levens = self.levens - 1   # bij botsing: -1 leven
            print(p1.levens, p2.levens)

    def bk(self, p1, p2):           # functie om achteruit te gaan
        self.t.backward(10)
        if collision(p1, p2) == True:       # controlleer botsing
            self.levens = self.levens - 1   # bij botsing: -1 leven
            print(p1.levens, p2.levens)

    def pos(self):
        return self.t.pos()         # geef de huidige positie van de turtle

def collision(player1, player2):
    pos1 = player1.pos()        # positie van turtle van speler 1
    pos2 = player2.pos()        # positie van turtle van speler 2
    a = (pos1[0] - pos2[0])**2  # (verschil in x-richting)^2
    b = (pos1[1] - pos2[1])**2  # (verschil in y-richting)^2
    diff = (a + b)**0.5         # Pythagoras: c = wortel(a^2 + b^2)
    if diff < 20:
        return True             # als afstand < 20, dan is er een botsing
    else:
        return False            # als afstand >= 20, dan is er geen botsing

s = turtle.getscreen()
turtle.hideturtle()

p1 = player(-200, 0, "blue")
p2 = player(200, 0, "red")

s.onkey(lambda : p1.fd(p1, p2), "w")     # p1 vooruit bij 'w'
s.onkey(lambda : p1.bk(p1, p2), "s")     # p1 achteruit bij 's'

s.onkey(lambda : p2.fd(p1, p2), "Up")    # p2 vooruit bij 'Up'
s.onkey(lambda : p2.bk(p1, p2), "Down")  # p2 achteruit bij 'Down'

s.listen()              # het scherm laten 'luisteren' naar toetsaanslagen

turtle.mainloop()