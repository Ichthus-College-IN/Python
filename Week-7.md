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
Je kunt maximaal vier van de volgende sterren halen:
* ⭐ er is een invoerveld voor hoe ver je voor/achteruit wilt en hoeveel graden je wilt draaien, met de bijbehorende knoppen die het uitvoeren.
* ⭐ er zijn knoppen voor pen omhoog en omlaag, een invoerveld om naar een (x, y)-positie te gaan, en een resetknop.
* ⭐ er zijn knoppen om de pen en/of vulkleur aan te passen (een paar standaardkleuren, of een RGB-invoerveld).
* ⭐ er zijn knoppen voor het maken van punten en cirkels (en delen van cirkels via een invoerveld, bijvoorbeeld 90 graden).
* ⭐ er zijn knoppen om een paar standaardfiguren te maken: een driehoek, vierkant, zeshoek en achthoek.

---

## Opdracht B
In hoofdstuk 6 maakte je twee losse plaatjes met twee lijnen erin. Maar dat kan natuurlijk een uitgebreider: meerdere grafiekjes in één figuur, waardoor je goed verschillen of samenhang tussen metingen kunt zien, en ook meerdere sensoren in dezelfde grafiek. Het is bijvoorbeeld zo dat de PM2.5 en PM10 waarden erg op elkaar lijken - logisch, want ze meten allebei fijnstof maar dan in een ander formaat (2.5 micrometer en 10 micrometer). Als de ene een piek heeft, zal de andere dat ook snel laten zien. In deze opdracht maak je een mooi overzicht van (bijna) alle data van een sensorkastje van Meet je Leefomgeving. 

Je maakt in totaal zes grafieken, in één figuur (drie naast elkaar, twee onder elkaar):
- linksboven de temperatuur
- linksonder de luchtvochtigheid
- middenboven het CO2-gehalte
- middenonder fijnstof (PM2.5 én PM10)
- rechtsboven lichtintensiteit
- rechtsonder accuspanning (voltage) en UV-sterkte

Je laat de data van één dag zien: kies zelf of je de eerste of tweede dag selecteert. Je mag er bij deze opdracht voor kiezen om de helft van de regels gewoon uit het bestand `Uplinks.csv` te verwijderen.  
Geef met behulp van commentaar bovenin in je script aan waarom je voor de eerste dan wel tweede dag gekozen hebt.

Het volgende stuk code helpt je vast op weg:
```python
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 3)

x = np.linspace(0, 2 * np.pi, 100)  # 2 rijen, 3 kolommen
y = np.sin(x)

def plot_format(ax_x, ax_y, label_x, label_y):  # voeg extra argumenten toe zoals nodig
    ax[ax_x, ax_y].grid()
    ax[ax_x, ax_y].set_xlabel(label_x)
    ax[ax_x, ax_y].set_ylabel(label_y)

ax[0,1].plot(x, y, label = 'sinus') # rij 0, kolom 1
ax[0,1].legend()
plot_format(0, 1, "x", "y")
```
Zoals je ziet, gebruik je nu een index `[rij, kolom]` om aan te geven in welk grafiek je iets wilt doen. Je kunt verder alle functies uitvoeren zoals je gewend bent.

### Beoordeling
Je kunt maximaal vier van de volgende sterren halen:
* ⭐ in alle zes de grafieken staat de juiste data.
* ⭐ alle assen zijn goed gelabeld wat betreft naam en waarden (tijd in uren).
* ⭐ de grafieken zijn goed af te lezen wat betreft legenda, kleur, grootte, grid etc.
* ⭐ je gebruikt de `plot_format`-functie om automatisch de opmaak voor elke grafiek te regelen.
* ⭐ voor de grafiek rechtsonder gebruik je twee y-assen: de y-as links voor de accuspanning; de y-as rechts voor de uv-index.

Een tip voor de laatste ster: om beide y-assen in de grafiek te gebruiken, bestaat de functie `twinx()`:
```python
fig, ax = plt.subplots(2, 3)

x = np.linspace(0, 2 * np.pi, 100)  # 2 rijen, 3 kolommen
y = np.sin(x)
y2 = np.cos(x)

ax[1,2].plot(x, y)
ax_2 = ax[1,2].twinx()  # maak een 'tweeling'grafiek op dezelfde x-as
ax_2.plot(x, y2)
```