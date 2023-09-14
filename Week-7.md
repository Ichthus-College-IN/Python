# Week 7
Deze week geen nieuwe stof (hoera!), maar alleen een afsluitende opdracht. Hierbij heb je keuze uit twee, waarbij je zelf kan kiezen welke je leuker vindt.

## Opdracht A
Je bouwt een combinatie tussen Tkinter en Turtle. Tot nu toe moest je bij het tekenen met Turtle zelf alles handmatig invoeren (denk aan `t.forward(100)` of `t.right(45)`). Met behulp van Tkinter kunnen we een soort 'tekenprogramma' maken: je maakt knoppen om vooruit, achteruit, links of rechts te gaan, voor een bepaalde kleur, of het maken van een cirkel e.d.

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

### Beoordeling
Je kunt vier van de volgende sterren halen:
* ⭐ er is een invoerveld voor hoe ver je voor/achteruit wilt en hoeveel graden je wilt draaien, met de bijbehorende knoppen die het uitvoeren.
* ⭐ er zijn knoppen voor pen omhoog en omlaag, een invoerveld om naar een (x, y)-positie te gaan, en een resetknop.
* ⭐ er zijn knoppen om de pen en/of vulkleur aan te passen (een paar standaardkleuren, of een RGB-invoerveld).
* ⭐ er zijn knoppen voor het maken van punten en cirkels (en delen van cirkels via een invoerveld, bijvoorbeeld 90 graden).
* ⭐ er zijn knoppen om een paar standaardfiguren te maken: een driehoek, vierkant, zeshoek en achthoek.

## Opdracht B
Je maakt een mooi overzicht van alle data van een sensorkastje van Meet je Leefomgeving. In de vorige opdracht maakte je een twee losse plaatjes met een of twee lijnen erin, maar dat kan natuurlijk een stukje uitgebreider: meerdere grafiekjes in één figuur, waardoor je goed verschillen of samenhang tussen metingen kunt zien.

---

<details>
<summary>Opdracht</summary>

Zorg dat alle grafieken niet in losse figuren staan, maar in een heel erg grote figuur door meerdere plots in één `plt.subplots()` te maken. Zoek op internet op hoe je daarmee aan de slag kunt! Regel dat de grafieken goed leesbaar zijn: groot genoeg met onderlinge ruimte, legenda's etc.

**Let op**: dit is een pittige opdracht om netjes te maken.

**Beoordeling:**
* 0.0pt: niet ingeleverd / werkt totaal niet
* 0.5pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 1.0pt: ingeleverd en (zo goed als) correct
</details>

---
