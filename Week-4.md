## Week 4.1
We laten de grafieken achter ons! Volgende halte: Turtle; we gaan een schildpad laten tekenen door te programmeren!

Installatie:
```powershell
py -m pip install turtle
```

Importeren:
```python
import turtle
```
Deze keer geen afkorting: we hebben de naam `turtle` weinig nodig.

### REPL
Waar we tot nu toe elke keer scripts hebben gebruikt, gaan we dit keer aan de slag in de REPL. REPL staat voor *Read-Eval-Print Loop*, oftewel: elk regeltje wordt gelezen, uitgevoerd en het resultaat (als dat er is) direct geprint. 

---

<details>
<summary>Opdracht</summary>

Open de REPL: ga naar de Terminal en typ:
```powershell
py
```

Er komen twee regeltjes tekst in beeld en vervolgens staat eronder:
```powershell
>>> 
```

Test de werking van de REPL:
```python
>>> print(5 + 3)
```

**Let op**: de `>>>` moet je niet mee-kopieren; ze geven aan dat het in de REPL uitgevoerd wordt. De symbolen staan er nog een paar keer voor de duidelijkheid bij, daarna wordt het normaal geacht.

Test vervolgens deze regel:
```python
>>> 5 + 3
```

Dit print ook een resultaat, zonder dat `print()` is gebruikt! Dat komt vanwege de P in REPL: alles wat een resultaat produceert wordt automatisch geprint. Ideaal :)

</details>

---

### De basisomgeving
Werken met `turtle` is eigenlijk tekenen met een pen op papier. Met de volgende regel komen we aan 'papier':
```python
>>> s = turtle.getscreen()
```

Het papier zit opgeslagen onder de variabele `s` van *screen*.

Met de volgende regel komen we aan een pen:
```python
>>> t = turtle.Turtle()
```

De pen zit nu opgeslagen onder de variabele `t` van *turtle*.

---

<details>
<summary>Opdracht</summary>

Ga aan de slag in de REPL: importeert Turtle en open een scherm onder de variabele `s`. Maak vervolgens een pen met de naam `t`.

Tip: gebruik splitscreen om VS Code, de opdrachten en het Turtle scherm allemaal in beeld te houden.

</details>

---

Nu kunnen we gaan tekenen!

### Simpele tekenfuncties
Een lijstje van eenvoudige commando's om te gaan tekenen:
```python
t.forward(100)  # 100 units vooruit
t.forward(-25)  # 25 units achteruit
t.backward(50)  # 50 units achteruit
t.left(90)      # 90 graden naar links draaien
t.left(-45)     # 45 graden naar rechts draaien
t.right(180)    # 180 graden naar rechts draaien
```

Makkelijke afkortingen:
```python
t.fd()
t.bk()
t.lt()
t.rt()
```

---

<details>
<summary>Opdracht</summary>

Maak een rechthoek van het formaat 100 bij 250 units. Probeer daarbij ook negatieve getallen uit.

</details>

---

Om naar een specifieke plek op het scherm te gaan, is de volgende functie beschikbaar:
```python
t.goto(x, y)        # ga naar het punt (x, y)
t.goto(-50, 10)     # ga naar het punt (-50, 10)
t.home()            # ga naar het punt (0, 0)
```

Zolang je pen op het papier staat, wordt er ook een lijn naar die plek getekend. Als je wilt voorkomen dat er een lijn komt te staan, kun je de pen optillen en later weer neerzetten:
```python
t.up()
t.down()
```

En dan is er nog een verzameling aan handige functies:
```python
t.undo()            # laatste actie ongedaan maken
t.position()        # huidige (x, y)-coordinaten weergeven
t.pos()             # korte alias van .position()
t.clear()           # alle strepen verwijderen
t.reset()           # helemaal opnieuw beginnen
t.hideturtle()      # turtle onzichtbaar maken
t.showturtle()      # turtle zichtbaar maken

turtle.hideturtle()     # de start-turtle onzichtbaar maken
turtle.title(title)     # de titel in de balk bovenin instellen
turtle.bgcolor(color)   # de achtergrondkleur van het scherm instellen
```

---

<details>
<summary>Opdracht</summary>

Test bovenstaande commando's uit. Probeer vooral een titel en achtergrondkleur aan te brengen!

</details>

---

### Punten en cirkels
Een punt maak je zo:
```python
t.dot(radius, color)
t.dot(10)           # een punt met straal 10
t.dot(20, "blue")   # een blauwe punt met straal 20
t.dot(5, "#15F204") # een (hexadecimaal) groene punt met straal 5
```

Voor een cirkel zijn er de volgende opties:
```python
t.circle(radius, extent, steps)
t.circle(50)                # cirkel met r = 50
t.circle(30.5, 180)         # halve cirkel met r = 30.5
t.circle(100, steps = 5)    # cirkel met r = 100 en 5 lijnstukken
t.circle(40, 270, 50)       # driekwart cirkel met r = 40 en 50 lijnstukken
```

**Let op**! Het startpunt van de cirkel is de huidige positie, waarna het pen linksom de cirkel maakt. Je kunt de cirkel ook rechtsom maken door een negatieve straal in te vullen, bijvoorbeeld `t.circle(-20)`.

---

<details>
<summary>Opdracht</summary>

Maak een hartje! De makkelijkste manier: begin met de turtle op 45 graden, dan een lijnstuk, vervolgens twee halve cirkels, en dan weer een lijnstuk. Vogel zelf uit hoe het precies moet! (Maak zo nodig gebruik van `t.undo()`.)

</details>

---

## Week 4.2
### Lijndiktes
Voor het wijzigen van de lijndikte kan de `pensize` (officieel is het een pen, geen pen) aangepast worden:
```python
t.pensize(width)        # default is 1
t.width(width)          # alias van .pensize()
```

Je kunt de pendikte wijzigen tussen elk lijnstuk.

### Kleuren met de schildpad
Het tekenen van een punt kon al met een kleur, maar tot nu toe is de rest saai zwart. Maar natuurlijk kan dat zwart ook veranderd worden.

Om de penkleur te wijzigen, kan het volgende gebruikt worden:
```python
t.pencolor('brown')     # string
t.pencolor(0.8, 0, 0.2) # RGB 0..1
t.pencolor(0, 100, 255) # RGB 0..255
t.pencolor('##8F438F')  # hexadecimaal
t.pencolor()            # geeft de huidige kleur weer
```

Ook de penkleur kun je tussen elk lijnstuk wijzigen, en zo dus elke volgende lijn of cirkel in een andere kleur maken.

---

<details>
<summary>Opdracht</summary>

Maak een regenboog. Gebruik wisselende pendiktes en -kleuren. Het liefst gebeurt dat natuurlijk door allemaal kleine stukken cirkels te gebruiken zodat de regenboog mooi rondloopt.

</details>

---

Naast lijnen kleuren is het ook mogelijk om vlakken te vullen met een kleur. Zie de volgende regels:
```python
t.fillcolor(color)  # string, RGB 0..1, RGB 0..255, hex
t.begin_fill()
t.circle(50)
t.end_fill()
```

`pencolor` en `fillcolor` zijn ook allebei in een keer in te stellen of op te vragen:
```python
t.color()           # geeft huidige kleuren weer
t.color(color)      # pen- en vulkleur allebei hetzelfde
t.color(pencolor, fillcolor)    # pen- en vulkleur apart instellen
```

---

<details>
<summary>Opdracht</summary>

Maak een smiley! Start met een gele cirkel met daarin twee zwarte of andersgekleurde ogen, en maak een mond of ander soort smiley.

Tip: maak gebruik van `.up()`, `.down()` en `.goto()` om naar andere plekken op het scherm te gaan zonder lijnen te tekenen.

</details>

---

## Week 4.3
### `turtle` en loops
Waar er tot nu toe veel handwerk nodig was om iets moois te maken, kunnen we uiteraard ook hier weer automatisering toepassen.

Vergelijk de volgende twee methoden om een vierkant te maken:
```python
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
```
```python
for i in range(4):  # i = 0, 1, 2, 3
    t.fd(100)
    t.rt(90)
```

Of in een keer een paar cirkels van verschillend formaat:
```python
for i in range(10, 50, 10): # i = 10, 20, 30, 40
    t.circle(i)             # cirkel met straal i
```

Een ander leuk voorbeeld:
```python
for i in range(10, 250, 5): # i = 10, 15, 20 .. 240, 245
    t.fd(i)
    t.lt(90)
```

---

<details>
<summary>Opdracht</summary>

Maak met behulp van een `for`-loop een dartbord na. Een dartbord heeft ringen in bepaalde kleuren: die horen er natuurlijk ook bij! Een kleine hint daarvoor:
```python
colors = ["red", "white", "blue"]
for i in range(len(colors)):    # i = 0, 1, 2 (want len(colors) = 3)
    t.fillcolor(colors[i])      # gebruik colors[i] als vulkleur
```

</details>

---

<details>
<summary>Bonusopdracht</summary>

Maak het Ichthuslogo zo goed mogelijk na. Een website zal gebruikt worden om de plaatjes te vergelijken: hoe beter de match, hoe hoger het cijfer. Maak je script zo netjes mogelijk met alle dingen die je geleerd hebt (of online kunt vinden)! Denk hierbij ook zeker aan de lijst functies in het eerste deel van het hoofdstuk.

</details>

---
