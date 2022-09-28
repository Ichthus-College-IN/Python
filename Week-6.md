## Week 6.1
Als laatste nieuwe onderwerp gaan we aan de slag met iets wat standaard ingebouwd is in Python: een `class`. Een `class` kan het programmeerleven heel wat simpeler maken!

### `class`: introductie
Een voorbeeld van een 'class' is bijvoorbeeld 'persoon'. Een persoon heeft een naam, leeftijd, haarkleur etc. Er zijn heel veel verschillende mensen, maar iedereen heeft die eigenschappen.

Het simpelste voorbeeld van een class:
```python
class person:
    age = 17

p1 = person()   # p1 is een nieuw persoon
print(p1.age)
p2 = person()   # p2 is ander persoon
print(p2.age)
```
`age` is een eigenschap van elk persoon dat er gemaakt wordt. Maar dat heeft nu nog wel voor elk persoon altijd de waarde 17.

---

<details>
<summary>Opdracht</summary>

Test eerst bovenstaand voorbeeld. Maak vervolgens een persoon met jouw leeftijd, naam en haarkleur door het voorbeeld uit te breiden. Print ook al die eigenschappen. Tip: voeg niet teveel dingen extra toe, want we gaan het zometeen op een betere manier doen.

</details>

---

Als je verschillende personen wilt maken, gaat het bovenstaande niet veel helpen. Je zou handmatig voor elke persoon een nieuwe class moeten maken om te voorkomen dat iedereen dezelfde leeftijd heeft bijvoorbeeld (17 in het voorbeeld). We gaan gebruik maken van ```__init__()``` functie: dat is een functie die *altijd* uitgevoerd wordt bij het maken van een nieuw *object* - een variabele die de class aanroept (zoals `p1` en `p2`).
```python
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Boonstoppel", 20)      # nieuw persoon met naam Boonstoppel en leeftijd 20
print(p1.name)
print(p1.age)
p2 = person("Kieskamp", 64)         # nieuw persoon met naam Kieskamp en leeftijd 64
print(p2.name)
print(p2.age)
```
Je ziet hier ook het woordje `self` tevoorschijn komen. Dat gaat later meer nut hebben, maar geeft alvast extra duidelijk aan dat `name` en `age` specifiek bij `self` oftewel `person` horen.

---

<details>
<summary>Opdracht</summary>

Test eerst bovenstaand voorbeeld. Maak vervolgens een persoon met jouw leeftijd, naam en haarkleur en eventuele andere eigenschappen door het voorbeeld uit te breiden.

</details>

---

Een class kan behalve 'eigenschappen' ook functies implementeren ('bezitten'):
```python
class person:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print("Mijn naam is", self.name)

p1 = person("Boonstoppel")
p1.print_name()
```
Hier wordt het nut van `self` iets duidelijker. In de functie `print_name()` hebben we de eigen naam nodig van de persoon. Door `self` aan de functie mee te geven, komt automatisch ook alles wat bij `self` hoort mee, zoals `name`. Je hoeft het niet als argument mee te geven aan de functie.

**Let op**: je hoeft (mag) `self` niet als *argument* meegeven als je de functie aanroept. Misschien zou je verwachten dat de laatste regel `p1.print_name(self)` moet zijn, maar dat hoort niet. Python voegt automatisch `self` in.

---

<details>
<summary>Opdracht</summary>

Test eerst bovenstaand voorbeeld. Voeg weer jouw leeftijd, naam en haarkleur toe. Zorg ervoor dat de functie `print_name()` al de eigenschappen van de persoon print.

</details>

---

## Week 6.2
### Een `turtle` class
We komen weer terug bij de schildpadden! Dit keer om er een spelletje mee te maken nu we extra dingen hebben geleerd.

Een spelletje is veel leuker met twee spelers. Daarom maken we een class die voor beide spelers gebruikt kan worden. Een basis daarvoor is als volgt:
```python
import turtle

class player:
    def __init__(self, x, y, color):
        self.t = turtle.Turtle()    # nieuwe turtle
        self.t.up()                 # pen van papier halen
        self.t.goto(x, y)           # naar startpositie gaan
        self.t.down()               # pen weer op papier zetten
        self.t.pencolor(color)      # penkleur instellen

    def fd(self):                   # functie om vooruit te gaan
        self.t.forward(10)

    def bk(self):                   # functie om achteruit te gaan
        self.t.backward(10)

s = turtle.getscreen()

p1 = player(-200, 0, "blue")

turtle.mainloop()
```

---

<details>
<summary>Opdracht</summary>

Test bovenstaand voorbeeld. Voeg vervolgens een functie toe aan de `player` class om linksom te draaien en om rechtsom te draaien.

Controleer ook of alle vier de functies om te bewegen werken!

</details>

---

Een spel is eigenlijk altijd afhankelijk van het toetsenbord en/of de muis. Via het volgende voorbeeld kunnen we daar gebruik van maken:
```python
s.onkey(lambda : p1.fd(), "w")     # player 1 vooruit bij 'w'
s.onkey(lambda : p1.bk(), "s")     # player 1 achteruit bij 's'
s.listen()              # het scherm laten 'luisteren' naar toetsaanslagen
```
Je ziet ook hier weer de `lambda` tevoorschijn komen, terwijl dat niet altijd nodig is of op internet bij voorbeelden staat, net als bij TKinter. Maar voor de handigheid wordt het alvast gebruikt.

---

<details>
<summary>Opdracht</summary>

Test bovenstaand voorbeeld. Wat gebeurt er als het scherm wel of niet 'actief' is? Je kunt dit testen door in split-screen te werken en juist een _ander_ scherm aan te klikken dan het turtle scherm. Druk vervolgens op de toetsen ('w' en 's').

Voeg vervolgens de functies toe die nodig zijn voor naar links en naar rechts bewegen. Maak daarbij de keuze: draai je de turtle alleen met 90 graden, beweeg je ook een stukje in die richting, en draai je daarna misschien weer terug? Zorg in ieder geval dat je er makkelijk mee kan 'spelen' als in een spelletje.

</details>

---

### Functies revisited
We keren kort terug naar functies (`def`). Bekijk het volgende voorbeeld:
```python
def Pythagoras(a, b):
    c = (a**2 + b**2)**0.5  # bereken de lange zijde
    return c

x = 3
y = 4
z = Pythagoras(x, y)
print(z)
```

Hier komt opeens het woord `return` om de hoek kijken. Wat er gebeurt: in de regel `z = Pythagoras(x, y)` staat dat `z` de waarde van `Pythagoras(x, y)` krijgt; dit betekent dat de functie `Pythagoras` een waarde heeft. De waarde van `z` is dan wat de functie 'teruggeeft', namelijk de waarde van `c`.

---

<details>
<summary>Opdracht</summary>

In de slotopdracht van hoofdstuk 1 maakte je een berekening van Fahrenheit naar graden Celsius. De formule daarvoor is:
```python
C = 5/9 * (F - 32)
```
Schrijf een functie met de naam `Celsius`, die de temperatuur omrekent van Fahrenheit naar Celsius met bovenstaande regel. De functie moet zo werken dat je onderstaande regels kunt kopieren en plakken in je script:
```python
F = 50
C = Celsius(F)
print(C)
```

</details>

---

## Week 6.3

### Een spel maken
Onderdeel van een spel is vaak het gebruik van 'collisions': je kunt ergens wel of niet mee botsen en verliest dan best wel eens spel-levens.

Hieronder is een uitgewerkt voorbeeld waarbij gekeken wordt of twee spelers met elkaar botsen. Een botsing vindt plaats als de afstand tussen de twee turtles kleiner is dan 50 units (best groot, maar makkelijker te testen).
```python
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

    def bk(self, other):            # functie om achteruit te gaan
        self.t.backward(10)
        if collision(self, other) == True:  # controlleer botsing
            self.levens = self.levens - 1   # bij botsing: -1 leven
            print(self.levens, other.levens)

    def pos(self):
        return self.t.pos()         # geef de huidige positie van de turtle

def collision(player1, player2):
    pos1 = player1.pos()            # positie van turtle van speler 1
    pos2 = player2.pos()            # positie van turtle van speler 2
    a = (pos1[0] - pos2[0])**2      # (verschil in x-richting)^2
    b = (pos1[1] - pos2[1])**2      # (verschil in y-richting)^2
    diff = (a + b)**0.5             # Pythagoras: c = wortel(a^2 + b^2)
    if diff < 50:
        return True                 # als afstand < 20, dan is er een botsing
    else:
        return False                # als afstand >= 20, dan is er geen botsing

s = turtle.getscreen()
turtle.hideturtle()

p1 = player(-200, 0, "blue")
p2 = player(200, 0, "red")

s.onkey(lambda : p1.fd(p2), "w")     # p1 vooruit bij 'w'
s.onkey(lambda : p1.bk(p2), "s")     # p1 achteruit bij 's'

s.onkey(lambda : p2.fd(p1), "Up")    # p2 vooruit bij pijltje omhoog 'Up'
s.onkey(lambda : p2.bk(p1), "Down")  # p2 achteruit bij pijltje naar beneden 'Down'

s.listen()              # het scherm laten 'luisteren' naar toetsaanslagen

turtle.mainloop()
```

---

<details>
<summary>Opdracht</summary>

Test bovenstaand voorbeeld.

Zorg dat de turtle weer naar links en naar rechts kan bewegen! Je kunt daarvoor onderdelen uit de vorige opdracht(en) hergebruiken, en dingen kopieren en plakken uit het huidige voorbeeld. Test uiteraard of het werkt!

</details>

---

<details>
<summary>(Bonus)opdracht</summary>

De levens zijn nog nergens zichtbaar.. dat maakt het een saai spelletje. Zorg dat je op een of andere manier de levens in beeld krijgt!
* Standaard opdracht: print de levens (altijd, of alleen bij een werkelijke collision) in de Terminal
* Bonusopdracht: gebruik een derde (onzichtbare) turtle en `t.write` om de levens als tekst in het scherm te schrijven. Zorg ook dat deze levens aangepast worden als er een leven verwijderd wordt!

Zorg als laatste nog dat er iets gebeurt als het aantal levens 0 of minder dan 0 is. Dat mag iets printen zijn, of iets op het scherm doen!

**Beoordeling:**
* 0.00pt: niet ingeleverd / werkt totaal niet
* 0.25pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 0.50pt: ingeleverd en (zo goed als) correct
</details>

---

<details>
<summary>Bonusopdracht</summary>

Let op: om echt wat moois van deze opdracht te maken zul je flink wat moeten rondneuzen op internet; het is zeker geen makkelijke opdracht.

Maak een werkend, leuk speelbaar spel! Het liefst is daarbij alleen het scherm met de turtles nodig, maar voor iets minder bonuspunten mag je ook de Terminal gebruiken om dingen te printen. Je kunt ook om input vragen via de Terminal. Het liefst maak je een spelletje dat je met twee spelers kunt spelen!

P.S. kopieer geen spel van internet om dat in te leveren. Gebruik het eventueel als basis die je zelf flink aanpast, maar bedenk het liefst zoveel mogelijk zelf. Er wordt gecontroleerd!

**Beoordeling:**
* 0.0pt: niet ingeleverd / werkt totaal niet
* 0.5pt: ingeleverd en simpele oplossing om werkend te krijgen / klein beetje aangepast van kopie
* 1.0pt: ingeleverd, werkend en zelfgemaakte clone van bestaand spel
* 1.5pt: ingeleverd, werkend en helemaal origineel
</details>

---