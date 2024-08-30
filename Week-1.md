# Week 1

## Deel 1: de allereerste basis
Welkom in de boeiende wereld van programmeren als middelbare scholier! Als je op zoek bent naar een toegankelijke en waardevolle programmeertaal om te leren, dan is Python de perfecte keuze. Python heeft zich bewezen als een uitstekende taal voor beginners vanwege zijn leesbaarheid en eenvoudige syntaxis. Dit betekent dat je snel resultaten kunt behalen en je vaardigheden kunt opbouwen zonder overweldigd te raken door complexe regels.

Wat Python echt opmerkelijk maakt, is zijn veelzijdigheid. Of je nu geïnteresseerd bent in het maken van websites, games, apps of zelfs het verkennen van datascience en kunstmatige intelligentie, Python biedt de benodigde hulpmiddelen en bibliotheken. Bovendien gaat het leren van Python verder dan alleen coderen; het bevordert ook logisch denken en probleemoplossende vaardigheden die waardevol zijn in diverse domeinen.

Kortom, Python is de ideale springplank om je eerste stappen te zetten in de programmeerwereld. Of je nu technologie wilt verkennen, je creativiteit wilt uiten of je denkvermogen wilt versterken, Python staat klaar om je reis boeiend en lonend te maken. Dus ga aan de slag en ontdek hoe Python deuren opent naar een wereld van mogelijkheden! Spelletjes, apps, automatisering, robots.. alles kan!

## Een eenvoudige start: rekenen met `ints`: hele getallen
We beginnen klein en gaan de mogelijkheden de komende weken steeds verder uitbreiden. In een notendop is een programmeertaal een _heel_ erg sterke en slimme (grafische) rekenmachine - zoals eigenlijk de hele computer een GR is, gebaseerd op nullen en enen. Maar wees gerust: dit wordt geen wiskunde-blok. Er komt hier en daar een sommetje als voorbeeld, maar die mag je de computer laten uitvoeren; je hoeft het niet zelf te doen.

Python staat alvast geïnstalleerd op de schoolcomputers. Als je dit programma (eigenlijk is het een _console_) opent, komt het volgende in beeld:

```
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

De drie pijltjes (`>>>`) geven een regel aan waarin jij kunt typen.

---

<details>
<summary>Opdracht</summary>

Open Python op de computer: via `Start` kun je zoeken naar `Python`.

</details>

---

<details>
<summary>Opdracht</summary>

Reken de volgende som uit: `137 * 6` door op de regel met de `>>>` te gaan typen en vervolgens op <kbd>Enter</kbd> te drukken. Wat is het resultaat?

</details>

---

Net als bij wiskunde kun je een _variabele_ gebruiken, bijvoorbeeld `x`. We kunnen `x` een waarde geven, en vervolgens ook 'opvragen' welke waarde `x` heeft. Een voorbeeld:
```python
>>> x = 137 * 6 * 5
>>> x
4110
```

*Let op!* De eerste regel (`x = 137 * 6 * 5`) geeft geen 'tussenresultaat': je ziet niet direct wat de uitkomst van de som is. Die zit opgeslagen in de variabele `x`. Als je `x` typt en vervolgens op <kbd>Enter</kbd> drukt, dan vertelt de computer je welke waarde daarbij hoort.

(Je bent niet verplicht om de spaties te typen voor tekens als `=` en `*`, maar dat maakt het wel beter leesbaar.)

---

<details>
<summary>Opdracht</summary>

Maak een variabele `y` met de volgende waarde: `x * 3 + 15`. Wat is de waarde van `y`?

</details>

---

Je moet in Python specifiek alle _operators_ (+, -, *, /) aangeven. Kijk maar:
```
>>> 5y
  File "<stdin>", line 1
    5y
    ^
SyntaxError: invalid decimal literal
>>> 5*y
61725
```

Je moet het keer-teken er echt tussenzetten, anders snapt Python niet wat je bedoelt. En Python is ook hoofdletter-gevoelig:
```
>>> x + y
16455
>>> x + Y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Y' is not defined. Did you mean: 'y'?
```

Python is dan wel weer zo aardig om in de laatste regel de suggestie te geven dat je `y` moet invoeren in plaats van `Y` - vertrouw er niet op dat je altijd zo'n suggestie krijgt! **Lees je code altijd nog eens goed door als je een foutmelding krijgt!**

---

<details>
<summary>Opdracht</summary>

Bereken de volgende som: x^3. *Let op!* In Python is het 'tot de macht'-teken _niet_ `^`, maar `**`.

</details>

---


## Rekenen met `floats`: kommagetallen
Om te werken met kommagetallen, wordt het helaas wennen: ongeveer elke programmeertaal gebruikt de 'normale' Engelse notatie: een `.` in plaats van de `,`. Hieronder een voorbeeld:
```python
>>> 3*0.5
1.5
```

---

<details>
<summary>Opdracht</summary>

Reken de volgende som uit: 0,16 tot de macht een half, vermenigvuldigd met tweeënhalf.

</details>

---


## Werken met tekst
Dat Python meer is dan een rekenmachine, gaan we nu direct al zien. Een rekenmachine kan namelijk niet werken met tekst, maar Python wel! Een stuk tekst noemen we in Python een _string_ - lekker een keer om lachen, maar vanaf nu noemen we dat gewoon een string.

```
>>> tekst = "Hello, world!"
>>> tekst
'Hello, world!'
```
Je ziet hier een paar nieuwe dingen:
* Een variabele mag langer zijn dan één letter (in theorie kun je een oneindig lange naam gebruiken).
* Tekst moet je invoeren tussen enkele (`'`) of dubbele  (`"`) apostrofs - allebei mag!

---

<details>
<summary>Opdracht</summary>

Sla je voornaam en je achternaam allebei op in een variabele met passende naam. Maak vervolgens een variabele `naam`: dit is je voornaam plus je achternaam. (Plus? Ja: een `+`.) Controleer of je naam klopt (eventueel moet je er een spatie bij plakken).

</details>

---

Je kunt een paar grappige functies uitvoeren op strings, zoals:
```
>>> school = "Ichthus College Veenendaal"
>>> school.lower()
>>> school.upper()
>>> school.count('e')
>>> school.find('t')
```

---

<details>
<summary>Opdracht</summary>

Test de bovenstaande functies op het voorbeeld of op je eigen naam. Wat doen de functies `count()` en `find()`? 

Kun je vinden wat er 'fout' lijkt met de `find()` functie? Tel namelijk de letters maar eens goed. Je leert straks waarom het wél klopt voor de computer. (Let op: zoek wel een letter die in de tekst staat.)

</details>

---

<details>
<summary>Opdracht</summary>

Hieronder zie je de inhoud van Johannes 3:16. Sla deze tekst op in een variabele. Tel vervolgens hoe vaak de letter 'e' voorkomt in deze tekst.

```python
"Want zo lief heeft God de wereld gehad, dat Hij Zijn eniggeboren Zoon gegeven heeft, opdat ieder die in Hem gelooft, niet verloren gaat, maar eeuwig leven heeft."
```

Deze tekst heeft een lengte van 130 letters. Bereken het percentage 'e's dat voorkomt in deze tekst. Op [deze website](https://onzetaal.nl/taalloket/letterfrequentie-in-het-nederlands) zie je de gemiddelde 'letterfrequentie' in het Nederlands. Hoe ver zit het er vanaf? Bereken ook nog twee andere letters.

</details>

---

## Lijsten: een verzameling
Je zult best vaak momenten tegenkomen waarbij je een lijst hebt van getallen (bijvoorbeeld de cijfers op een dobbelsteen) of een lijst van woorden of zinnen (als je een tekstdocument opent - ja, dat kan ook!). Een lijst - _list_ - kun je herkennen aan de vierkante blokhaken:
```python
>>> lst1 = [4, 6, 9, -2, 0, 3]
>>> lst2 = ["a", "b", 'c', 'abc', "test"]
```

Je kunt bij een lijst een specifiek element opvragen met behulp van een _index_. Elke type met een lengte (zoals een _list_ en een _string_) kun je _indexen_. Je herkent een index aan de vierkante haken achter een variabele:
```
>>> lst1[0]
4
>>> lst1[5]
3
>>> lst2[1]
'b'
```

> [!IMPORTANT]
> Een computer begint met tellen bij 0! Om het eerste element te zien, met je dus `[0]` opvragen. Het tweede element krijg je dan met `[1]`, enzovoorts.

---

<details>
<summary>Opdracht</summary>

Een dobbelsteen heeft de getallen 1 t/m 6. Maak daarvoor een lijst aan met de naam `dice` (Engels voor dobbelsteen). Tel alle items in de lijst bij elkaar op door gebruik te maken van de blokhaken. Een kleine tip:

```python
dice[0] + ...
```

Reken zelf na of je het goede antwoord krijgt.

</details>

---

### Random keuzes
Als je een dobbelsteen gooit, komt daar natuurlijk een willekeurig getal van 1 t/m 6 uit. In Python kunnen we ook een random item uit een lijst trekken:

```python
>>> import random
>>> random.choice(dice)
```

> [!NOTE]
> `import` betekent eigenlijk dat je een plug-in toevoegt. Heel veel mensen hebben plug-ins geschreven voor Python die allerlei extra functies toevoegen. Zoals de optie om een `random` `choice` te doen uit een lijst.

---

<details>
<summary>Opdracht</summary>

Rol jouw dobbelsteen vijf keer door dezelfde regel te herhalen

> [!TIP]
> Met de toets 'Pijltje omhoog' kun je de vorige regel tevoorschijn halen zonder het nog een keer te hoeven typen. Zo kun je de dobbelsteen dus makkelijk een heel aantal keer rollen!

</details>

---

Ook lists hebben een paar ingebouwde functies, waaronder:
```
>>> lst1.append(100)
>>> lst1.remove(3)
```
Deze functies doen het volgende:
* `append()` voegt een item toe aan het einde van de lijst.
* `remove()` verwijdert het item als die aanwezig is; als die niet aanwezig is krijg je een foutmelding.

---

<details>
<summary>Opdracht</summary>

In het spel Risk heeft de aanvallende speler drie dobbelstenen, de verdediger twee. Maak twee lege lijsten:
```python
speler1 = []
speler2 = []
```
Er zit nog niets in deze lijst.

Gooi drie keer een dobbelsteen, en voeg het resultaat in in de lijst voor speler 1. Doe hetzelfde voor speler 2. 

</details>

---

<details>
<summary>Opdracht</summary>

De volgende spelregels gelden voor de dobbelstenen in Risk:

* De beste dobbelsteen van de aanvaller wordt vergeleken met de beste dobbelsteen van de verdediger. 
* Daarna de tweede dobbelsteen van de aanvaller met de tweede dobbelsteen van de verdediger. 
* Telkens wint de speler met het hoogste aantal ogen. Wanneer dat aantal gelijk is, wint de verdediger.

Verwijder bij beide spelers de geworpen dobbelstenen die niet meetellen. (In totaal moet je dus twee dobbelstenen verwijderen.)

</details>

---

## Deel 2: tekenen met een schildpad

Tijd voor wat anders: we gaan plaatjes tekenen met een schildpad. Ja, echt.

```python
import turtle
t = turtle.Turtle()
```
*Let op!* Vanaf nu staat er niet meer elke keer `>>>` aan het begin van de regel. Ondertussen snappen we wel dat dat er staat.

> [!NOTE]
> Je importeert weer een soort van plug-in, namelijk eentje om mee te tekenen.

We voeren van `turtle` de functie `Turtle` uit. Die functie maakt een schildpad, die we opslaan in de variabele `t`.

---

<details>
<summary>Opdracht</summary>

Voer bovenstaande twee regels uit. Bij de tweede regel zie je in de taakbalk onderin een nieuw icoon tevoorschijn komen. Maak je scherm splitscreen zodat je alles in beeld krijgt. Pro-tip: de opdrachten op de ene helft, het _turtle_ scherm bovenin de andere helft, de Python _terminal_ onder in die helft.

</details>

---

Je ziet nu een kale witte vlakte, met middenop een zwart pijltje. Vroeger stond hier echt een schildpad icoon, maar nu is het standaard een pijltje. Als je wilt kun je er nog steeds een schildpad van maken!

```
t.shape("turtle")
t.shape("arrow")
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("classic")
```

---

<details>
<summary>Opdracht</summary>

Probeer de verschillende iconen en kies er eentje uit om mee verder te werken.

</details>

---

Wat doet `turtle` nou eigenlijk? Je kunt het vergelijken met het volgende: het witte scherm is een papier / canvas, en de schildpad (of ander icoon) een pen / kwast. We kunnen de pen programmeren om te bewegen, om hem van het papier te halen of er juist op te zetten, of allerlei kleurtjes te geven (en nog meer). Binnen de lijntjes kleuren was nog nooit zo makkelijk ;)

Nu kunnen we gaan tekenen!

## Simpele tekenfuncties: lijnen
Een lijstje van eenvoudige commando's om te gaan tekenen:
```python
t.forward(100)  # 100 units vooruit
t.forward(-25)  # 25 units achteruit
t.backward(50)  # 50 units achteruit
t.left(90)      # 90 graden naar links draaien
t.left(-45)     # 45 graden naar rechts draaien
t.right(180)    # 180 graden naar rechts draaien
```

> [!TIP]
> Je ziet iets nieuws:
> * Commentaar (ofwel _comments_)! Je herkent ze aan de `#` - alles achter de `#` wordt genegeerd door Python: je kunt dit gebruiken om uitleg te geven bij een regel. Mocht je het wel 'per ongeluk' invoeren, gaat er niks mis!
> * Je hoeft commentaar echt niet te kopiëren of in te voeren nu, maar we gebruiken ze vanaf nu geregeld voor uitleg bij de code zelf. Je kunt ze ook zelf gebruiken als geheugensteuntje bij je eigen code.

Makkelijke afkortingen:
```python
t.fd(..)        # tussen de haakjes uiteraard nog wel een getal invullen
t.bk(..)
t.lt(..)
t.rt(..)
```

Als je fouten hebt gemaakt kun je de volgende commando's gebruiken:
```python
t.undo()        # laatste actie ongedaan maken
t.clear()       # alle strepen verwijderen, maar de turtle laten staan
t.reset()       # helemaal opnieuw beginnen
```

> [!CAUTION]
> Vergeet niet de haakjes elke keer toe te voegen. Je voert namelijk een _functie_ uit (later leer je daar meer over) - net als bij wiskunde heeft een functie altijd haakjes (zoals bij `y = f(x)`).

---

<details>
<summary>Opdracht</summary>

Maak een rechthoek van het formaat 100 bij 250 units. Probeer daarbij ook negatieve getallen uit.

</details>

---

<details>
<summary>Opdracht</summary>

Maak een huisje zoals je die als kind altijd tekent: een rechthoek of vierkant met een driehoek er bovenop.

</details>

---

<details>
<summary>Opdracht</summary>

Maak een vijfpuntige ster. (Tip: gebruik hoeken van 145 graden.)

</details>

---


## Cirkels
Je kunt ook cirkels (of delen van cirkels maken):
```python
t.circle(radius, extent)
t.circle(50)                # cirkel met r = 50
t.circle(30.5, 180)         # halve cirkel (180 graden) met r = 30.5
```

**Let op**! Het startpunt van de cirkel is de huidige positie, waarna de pen linksom de cirkel maakt. Je kunt de cirkel ook rechtsom maken door een negatieve straal in te vullen, bijvoorbeeld `t.circle(-20)`.

--- 

<details>
<summary>Opdracht</summary>

Maak een hartje! De makkelijkste manier: begin met de turtle op 45 graden, dan een lijnstuk, vervolgens twee halve cirkels, en dan weer een lijnstuk. Vogel zelf uit hoe het precies moet!

</details>

---

Zolang je pen op het papier staat, wordt er ook een lijn naar die plek getekend. Als je wilt voorkomen dat er een lijn komt te staan, kun je de pen optillen en later weer neerzetten:
```python
t.up()
t.down()
```

Daarnaast kun je ook met kleurtjes tekenen. De makkelijkste manier is met standaardnamen:

```python
t.color("orange")
t.color("magenta")
```

---

<details>
<summary>Slotopdracht</summary>

Maak het logo van de Olympische Spelen (of doe een zo goed mogelijke poging -  de ringen van de Olympische Spelen overlappen elkaar op een manier die je niet makkelijk kunt namaken, dat mag je laten zitten).

Tip: maak gebruik van `.up()` en `.down()` om naar andere plekken op het scherm te gaan zonder lijnen te tekenen. En gebruik `.undo()` als je een fout maakt.

Laat je resultaat aan de docent zien.

</details>

---