# Week 4.1
Na een poos bezig geweest te zijn met letters en teksten, gaan we nog even terug naar het tekenen met de schildpad. We hebben meer dingen geleerd waardoor het makkelijker wordt om figuurtjes te tekenen.

Importeren:
```python
import turtle
```


## De basisomgeving
Werken met `turtle` is eigenlijk tekenen met een pen op papier. Met de volgende regel komen we aan 'papier':
```python
s = turtle.getscreen()
```

Het papier zit opgeslagen onder de variabele `s` van *screen*. Let op: er opent een extra scherm (in de achtergrond).

Met de volgende regel komen we aan een pen:
```python
t = turtle.Turtle()
```

De pen zit nu opgeslagen onder de variabele `t` van *turtle*. Nu kunnen we gaan tekenen!

## Overzicht van basis-tekenfuncties
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

Als je fouten hebt gemaakt kun je de volgende commando's gebruiken:
```python
t.undo()        # laatste actie ongedaan maken
t.clear()       # alle strepen verwijderen
t.reset()       # helemaal opnieuw beginnen
```

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

En dan is er nog een verzameling aan (minder) handige functies:
```python
t.position()        # huidige (x, y)-coordinaten weergeven
t.pos()             # korte alias van .position()
t.hideturtle()      # turtle onzichtbaar maken
t.showturtle()      # turtle zichtbaar maken
t.stamp()           # een stempel op de huidige plek van de turtle
```

En een aantal verschillende looks voor je turtle:
```python
t.shape("turtle")
t.shape("arrow")
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("classic")
```

Je kunt ook achtergrondkleuren instellen:
```python
turtle.bgcolor(color)   # de achtergrondkleur van het scherm instellen
turtle.bgcolor("red")
turtle.bgcolor("green")
turtle.bgcolor("magenta")
```

**Let op**: als je `turtle` in een script wilt gebruiken in plaats van via de REPL, moet je altijd aan het einde van je script zetten:
```python
turtle.mainloop()
```


## Punten en cirkels
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

**Let op**! Het startpunt van de cirkel is de huidige positie, waarna de pen linksom de cirkel maakt. Je kunt de cirkel ook rechtsom maken door een negatieve straal in te vullen, bijvoorbeeld `t.circle(-20)`.

---

<details>
<summary>Opdracht</summary>

Maak een smiley: een grote cirkel, met twee dots voor ogen. De mond moet een deel van een cirkel zijn.

</details>

---


## Lijndiktes
Voor het wijzigen van de lijndikte kan de `pensize` aangepast worden:
```python
t.pensize(width)        # default is 1
t.width(width)          # alias voor .pensize(), kun je dus ook gebruiken
```

Je kunt de pendikte wijzigen tussen elk lijnstuk.

---

<details>
<summary>Opdracht</summary>

Maak een vierkant met een dikke buitenrand. Voeg vervolgens de twee diagonalen toe, maar maak die lijnen veel dunner. Zet vervolgens vier verschillend gekleurde stippen in de vier delen tussen de diagonalen.

</details>

---


## Kleuren met de schildpad
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

Maak het logo van de Olympische spelen.

</details>

---

Naast lijnen kleuren is het ook mogelijk om vlakken te vullen met een kleur. Zie de volgende regels:
```python
t.fillcolor(color)  # string, RGB 0..1, RGB 0..255, hex
t.begin_fill()  	# alles wat tussen begin_fill en end_fill staat, wordt opgevuld
t.circle(50)
t.end_fill()        # de cirkel vullen met een kleur
```

`pencolor` en `fillcolor` zijn ook allebei in een keer in te stellen of op te vragen:
```python
t.color(color)      # pen- en vulkleur allebei hetzelfde
t.color(pencolor, fillcolor)    # pen- en vulkleur apart instellen
```

---

<details>
<summary>Opdracht</summary>

Maak het logo van Mitsubishi maar gebruik een gouden rand en vul de drie ruiten met verschillende kleuren. Tip: gebruik hoeken van 45 graden en 135 graden.

</details>

---


## `turtle` en loops
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
of:
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

**Herinnering**: als je `turtle` in een script gebruikt, moet je altijd aan het einde van je script zetten:
```python
turtle.mainloop()
```

---

<details>
<summary>Opdracht</summary>

Maak met behulp van een aantal `for`-loops een driehoek, vierhoek, zeshoek en achthoek. Hint: als je *n* hoeken gebruikt, moet je de turtle met *360/n* graden draaien.

</details>

---

<details>
<summary>Opdracht</summary>

Maak een vijfpuntige ster uit één lijn door een `for`-loop te gebruiken.

</details>

---

## Een bestand inlezen
Stel: iemand heeft een tekening opgeslagen als commando's in een bestand. Je kunt dan met de hand alle commando's gaan overtypen, maar dat duurt natuurlijk uren als het een grote tekening is. Daarom gaan we kijken hoe Python een bestand kan inlezen, waarna we alle commando's automatisch laten gebeuren.

```python
# open het bestand 'tekening.txt' in 'r'(ead) modus
file = open("tekening.txt", "r")

# ..iets doen met de inhoud van het bestand

# sluit het bestand
file.close()
```

---

<details>
<summary>Opdracht</summary>

Maak in je map van deze week een nieuw bestand met de naam `tekening.txt`. Op GitHub staat een bestand met dezelfde naam bij de lesstof. Kopieer de inhoud van dat bestand naar je eigen computer. Test vervolgens bovenstaand stukje script. Je kunt het beste in een leeg script (nieuw Python bestand) beginnen **in dezelfde map als het tekstbestand**.

Tip: als je een error krijgt bij bovenstaande code, doe dan het volgende: ga in Visual Studio Code naar `File > Open Folder` en open dan specifiek de map waarin je Python script én tekstbestand zijn opgeslagen.

</details>

---

We kunnen alle regels in het bestand uitlezen:
```python
# .. open het bestand zoals eerder
regels = file.readlines()
# .. sluit het bestand zoals eerder
```

Alle regels worden als een _list_ ingelezen: elke regel is een item in de lijst.

---

<details>
<summary>Opdracht</summary>

Print de eerste regel. Reminder: de computer begint met tellen bij 0.

</details>

---

We kunnen door alle regels heen met een `for`-loop.

---

<details>
<summary>Opdracht</summary>

Print elke regel in `regels`, door middel van een `for`-loop. Weet je niet meer hoe? Zoek dan terug in het einde van week 2.

</details>

---

De eerste letter van elke regel is het commando dat uitgevoerd moet worden. De mogelijke opties:
|Afkorting|Commando|
|:--|:-----------|
|`f`|`forward`   |
|`b`|`backward`  |
|`l`|`left`      |
|`r`|`right`     |
|`o`|`dot`       |
|`s`|`start_fill`|
|`e`|`end_fill`  |
|`p`|`pencolor`  |
|`i`|`fillcolor` |
|`c`|`circle`    |
|`u`|`up`        |
|`d`|`down`      |
|`g`|`goto`      |


## Match-case
Python heeft ingebouwd een mooi trucje om met opties overweg te kunnen: de `match-case` constructie.

```python
stoplicht = "groen"

match stoplicht:
    case "rood":
        print("Stilstaan")
    case "oranje":
        print("Afremmen")
    case "groen":
        print("Rijden")
    case _:
        print("Dat kan niet")
```

In dit voorbeeld gaan we een stuk code _matchen_ op de variabele `stoplicht`. In het geval (in `case`) dat de waarde `"rood"` is, dan print de code dat je moet stilstaan; bij `"oranje"` dat je moet afremmen, en bij `"groen"` dat je mag rijden. In alle andere gevallen (`_`) wordt geprint dat een stoplicht die kleur niet kan hebben.

---

<details>
<summary>Opdracht</summary>

Maak een functie `uitvoeren`, met één argument: `regel`. Zet de volgende twee regels bovenaan in de functie:
```python
commando = regel[0]
argument = regel[1:]
```
Bouw in de functie een `match-case` constructie. Match op `commando`, met een `case` voor alle opties in de tabel met commando's. Voor nu print je in elke case het commando dat straks uitgevoerd moet worden. Vergeet niet de laatste case, voor alle andere opties.

Tip: let op alle dubbele punten en tabs die je moet gebruiken!
</details>

---

Een paar cases krijg je cadeau - de andere schrijf je zometeen zelf.
```python
case 'i':
    t.fillcolor(argument)
case 'c':
    (rad, deg) = argument.split(',')
    t.circle(int(rad), int(deg))
case 'u':
    t.up()
case 'd':
    t.down()
case 'g':
    (x, y) = argument.split(',')
    t.goto(int(x), int(y))
```

---

<details>
<summary>Opdracht</summary>

Kopieer bovenstaande cases, en maak de andere cases compleet! Stel dat een regel `"f100"` is, dan is het commando `"f"` en het argument `"100"`. Je turtle moet dan met 100 vooruit.

Tip: je moet het argument nog omzetten van een string in een int (geheel getal). Dat kan met `int(argument)`.

</details>

---

<details>
<summary>Opdracht</summary>

Op GitHub staat een bestand genaamd `tekening.txt`. Maak in de map met je script een bestand met dezelfde naam. Kopieer de inhoud van het GitHub bestand en sla het op in je eigen bestand.

Open vervolgens in het script het bestand, en voer voor elke regel in het bestand de functie `uitvoeren` uit. Als je alles goed hebt gedaan krijg je een plaatje in beeld. Lukt het niet? Kijk dan of je een error ziet die je begrijpt. Werkt je script / zie je een goed plaatje? Probeer dan ook `tekening2.txt`. 

Tip: stel vóór het tekenen de snelheid van je turtle in op maximaal: `t.speed(10)`. Anders ben je (zeker met het laatste bestand) lang aan het wachten...

</details>

---

