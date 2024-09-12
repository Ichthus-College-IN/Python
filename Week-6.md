# Week 6
Deze week geen nieuwe stof (hoera!), maar alleen een afsluitende opdracht. Met behulp van Tkinter en Turtle bouw je als afsluitende opdracht je eigen tekenprogramma! Tot nu toe moest je bij het tekenen met Turtle zelf alles handmatig invoeren (denk aan `t.forward(100)` of `t.right(45)`). Met behulp van Tkinter kunnen we een soort 'tekenprogramma' maken: je maakt knoppen om vooruit, achteruit, links of rechts te gaan, voor een bepaalde kleur, of het maken van een cirkel e.d.

Je kunt een _turtle_ scherm in een TKinter app invoegen. Hier volgt een aanzet, waarbij je zelf de afmetingen kan aanpassen, knoppen en invoervelden kan toevoegen en wat je verder wilt of nodig hebt:
```python
import tkinter as tk
import turtle

def draw():
    # iets tekenen...
    pass

root = tk.Tk()
root.title("Turtle in Tkinter")
root.geometry("600x500")

canvas = tk.Canvas(root)
canvas.place(x = 0, y = 0, width = 600, height = 400)

screen = turtle.ScrolledCanvas(canvas)
screen.place(x = 0, y = 0, width = 600, height = 400)

t = turtle.RawTurtle(screen._canvas)

draw_button = tk.Button(root, text = "Draw something", command = lambda : draw())
draw_button.place(x = 250, y = 440, width = 100, height = 20)

root.mainloop()
```

## Slotopdracht ⭐⭐⭐
Je tekenprogramma beschikt over de volgende functies:
* er is een invoerveld voor hoe ver je voor/achteruit wilt en hoeveel graden je wilt draaien, met de bijbehorende knoppen die het uitvoeren.
* er zijn knoppen voor pen omhoog en omlaag, een invoerveld om naar een (x, y)-positie te gaan, en een resetknop.
* er zijn knoppen om de pen en/of vulkleur aan te passen (een paar standaardkleuren, of een RGB-invoerveld).
* er zijn knoppen voor het maken van punten en cirkels (en delen van cirkels via een invoerveld, bijvoorbeeld 90 graden).
* er zijn knoppen om een paar standaardfiguren te maken: een driehoek, vierkant, zeshoek en achthoek.

## Bonus 6 ⭐

> [!CAUTION]
> Deze opdracht is **erg** moeilijk! Alleen voor leerlingen met ervaring / veel tijd over.

In week 4 heb je een programma geschreven waarmee je tekeningen kunt 'importeren'. Maar dan moet je natuurlijk wel eerst een geëxporteerde tekening hebben. Voor de laatste punt is de uitdaging hier om alles wat je turtle tekent, op te slaan in een bestand. Die kun je dan vervolgens weer importeren.

De mooiste oplossing gebruikt een `class`: iets wat je in het lesmateriaal niet gezien hebt. Daarom een kleine head-start:
```python
class TurtleLogger:
    t = turtle.Turtle()
    def __init__(self, filename):
        self.t.speed(10)
        self.file = open(filename, "w")
```

Verder: heel veel succes gewenst. En vergeet niet de knoppen voor het exporteren/opslaan en importeren/openen in je app!