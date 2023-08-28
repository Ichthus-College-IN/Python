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

Je kunt strings aan elkaar plakken:
```
tekst2 = "Hello, " + "world!"
tekst2 = "Hello" + ", " + "world" + "!"
```

---

<details>
<summary>Opdracht</summary>

Sla je voornaam en je achternaam allebei op in een variabele met passende naam. Maak vervolgens een variabele `naam` die bestaat uit je voor- en achternaam aan elkaar. Controleer of je naam klopt (eventueel moet je er een spatie bij plakken).

</details>

---

Hoe lang is jouw naam?
```
>>> len(naam)
```
Weer een paar nieuwe dingen
* `len(...)` is een functie - net zoals in wiskunde `f(x)` een functie is.
* Een functie herken je aan de _ronde_ haken die om de inhoud (officieel 'argumenten') heen staan.
* De lengte van een string is het aantal karakters, inclusief spaties, leestekens of getallen die in de tekst kunnen staan.

Je kunt ook mix-and-matchen:
```
>>> klas = "H5F"
>>> "Ik zit in klas " + klas
'Ik zit in klas H5F'
```

*Let op!* Je kunt alleen items van hetzelfde _type_ mixen. Het volgende werkt niet:
```
>>> age = 16
>>> "I am " + age + " years old"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
Lees de error: `can only concatenate str (not "int") to str`. Vertaald is dit: je kunt alleen een string aan een string toevoegen (to concatenate), je kunt geen integer (getal) toevoegen.

Je moet dan het getal specifiek omzetten in een string. Dat kan met de functie `str()`:
```
>>> "I am " + str(age) + " years old"
'I am 16 years old'
```

Je kunt een paar grappige functies uitvoeren op strings, zoals:
```
>>> school = "Ichthus College Veenendaal"
>>> school.lower()
>>> school.upper()
>>> school.count('e')
>>> school.find('t')
```
Je ziet wat nieuws:
* Een variabele kan functies hebben die specifiek zijn voor dat _type_. Dan gebruik je die functie door `<variabele>.<functie>(...)` te typen, met `<variabele>` de naam van jouw variabele, en `<functie>` de naam van je functie met eventuele argumenten tussen de haakjes.

---

<details>
<summary>Opdracht</summary>

Test de bovenstaande functies op het voorbeeld, en/of op je eigen naam. Wat doen de functies `count()` en `find()`? 

Kun je vinden wat er 'fout' lijkt met de `find()` functie? Je leert straks waarom het wél klopt voor de computer. (Let op: zoek wel een letter die in de tekst staat.)

</details>

---

## Lijsten: een verzameling
Je zult best vaak momenten tegenkomen waarbij je een lijst hebt van getallen (als je bijvoorbeeld een grafiek tekent) of een lijst van woorden / zinnen (als je een document opent - ja, dat kan ook!). Een lijst - _list_ - kun je herkennen aan de vierkante blokhaken:
```python
>>> lst1 = [10, 11, 12, 13, 14, 15]
>>> lst2 = ["a", "b", 'c', 'abc', "test"]
```

Net als een string, heeft een list een lengte: het aantal items in de lijst.

---

<details>
<summary>Opdracht</summary>

Maak een variabele `totale_lengte`: deze heeft als waarde de lengte van beide lijsten opgeteld. Hint: `len(...)`. Controleer uiteraard of je antwoord klopt!

</details>

---

Je kunt bij een lijst een specifiek element opvragen met behulp van een _index_. Elke type met een lengte (zoals een _list_ en een _string_) kun je _indexen_. Je herkent een index aan de vierkante haken achter een variabele:
```
>>> lst1[0]
10
>>> lst1[5]
15
>>> lst2[1]
'b'
>>> lst2[2:5]
['c', 'abc', 'test']
```

Er valt weer wat op:
* Een computer begint met tellen bij 0! Om het eerste element te zien, met je dus `[0]` opvragen. Het tweede element krijg je dan met `[1]`, enzovoorts.
* Je kunt meerdere elementen in één keer opvragen met `[start:end]`. Je krijgt dan de elementen _vanaf_ de start _tot_ (niet tot en met!) _end_. Wat je dus terugkrijgt is een deel van de lijst - de vierkante haken geven aan dat je een lijst krijgt.

---

<details>
<summary>Opdracht</summary>

Sla je volledige naam weer op in de variabele `naam`. Vraag vervolgens alleen precies je voornaam op met behulp van de `[.. : ..]` methode, en vervolgens alleen precies je achternaam.

</details>

---

Ook lists hebben een paar ingebouwde functies, waaronder:
```
>>> lst1.append(100)
>>> lst1
>>> lst2.insert(0, "hallo")
>>> lst2
>>> lst2.pop(0)
>>> lst2
```
Deze functies doen het volgende:
* `append()` voegt een item toe aan het einde van de lijst
* `insert()` voegt een item toe vóór de index die je aangeeft (in het voorbeeld is die index 0)
* `pop()` verwijdert het item op de index die je aangeeft, en vertelt je wat er staat (in het voorbeeld is dat index 0)

---

<details>
<summary>Opdracht</summary>

Stel: je hebt een slimme koelkast. Er zijn tegenwoordig varianten die automatisch een boodschappenlijstje kunnen presenteren, omdat ze weten wat er uit de koelkast verdwenen is.

Na het bijvullen van de boodschappen, is het boodschappenlijstje leeg:
```python
lijstje = []
```

Werk de volgende gebeurtenissen af door gebruik te maken van `lijstje.append(..)`, `lijstje.insert(..)` en `lijstje.pop(..)`.
* Na verloop van tijd blijkt dat de melk en boter op zijn. Voeg deze toe aan het lijstje, zodat de melk vooraan staat en de boter erachter. 
* Na een tijdje blijkt dat de appels ook op zijn. Deze liggen vooraan in de winkel, dus voeg ze voorin het lijstje toe. 
* Nog wat later is ook de kipfilet op. Voeg deze toe aan het einde van het lijstje.
* Bij de lokale kippenboer haal je eieren. Dit specifieke item moet dus weer van het lijstje verwijderd worden.

Hoe ziet de uiteindelijke lijst eruit?

</details>

---


## Deel 2: tekenen met een schildpad

De allereerste basis is nu klaar! Tijd voor wat anders: we gaan plaatjes tekenen met een schildpad. Ja, echt.

```
import turtle
t = turtle.Turtle()
```
*Let op!* Vanaf nu staat er niet meer elke keer `>>>` aan het begin van de regel. Ondertussen snappen we wel dat dat er staat.

Je ziet nieuwe dingen:
* `import` betekent dat we dingen toevoegen aan de Python sessie die niet écht standaard in Python zitten. Andere mensen hebben dan een soort 'plugin' gemaakt voor Python die jij makkelijk kunt toevoegen. (Je kunt ze ook zelf maken, maar dat bespreken we niet.)
* We voeren uit de 'plugin' `turtle` de functie `Turtle` uit. Die functie maakt een schildpad, die we opslaan in de variabele `t`.

---

<details>
<summary>Opdracht</summary>

Voer bovenstaande twee regels uit. Bij de tweede regel zie je in de taakbalk onderin een nieuw icoon tevoorschijn komen. Maak je scherm splitscreen zodat je alles in beeld krijgt. Pro-tip: de opdrachten op de ene helft, het _turtle_ scherm boven op de andere helft, de Python _terminal_ onder op die helft.

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
Je ziet iets nieuws:
* Commentaar (ofwel _comments_)! Je herkent ze aan de `#` - alles achter de `#` wordt genegeerd door Python: je kunt dit gebruiken om uitleg te geven bij een regel. Mocht je het wel 'per ongeluk' invoeren, gaat er niks mis!
* Je hoeft commentaar echt niet te kopiëren of in te voeren nu, maar we gebruiken ze vanaf nu geregeld voor uitleg bij de code zelf. Later zul je je eigen code ook hier en daar moeten uitleggen met behulp van _comments_.


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


Om naar een specifieke plek op het scherm te gaan, is de volgende functie beschikbaar:
```python
t.goto(x, y)        # ga naar het punt (x, y)
t.goto(-50, 10)     # ga naar het punt (-50, 10)
t.home()            # ga naar het punt (0, 0)
t.position()        # huidige (x, y)-coordinaten weergeven
t.pos()             # korte alias van .position()
```

Zolang je pen op het papier staat, wordt er ook een lijn naar die plek getekend. Als je wilt voorkomen dat er een lijn komt te staan, kun je de pen optillen en later weer neerzetten:
```python
t.up()
t.down()
```

---

<details>
<summary>Opdracht</summary>

Maak de Joodse ster na.

</details>

---


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

Maak het logo van Audi.

Tip: maak gebruik van `.up()`, `.down()` en `.goto()` om naar andere plekken op het scherm te gaan zonder lijnen te tekenen. En gebruik `.undo()` als je een fout maakt.

</details>

---

<details>
<summary>Slotopdracht ⭐</summary>

Maak een hartje! De makkelijkste manier: begin met de turtle op 45 graden, dan een lijnstuk, vervolgens twee halve cirkels, en dan weer een lijnstuk. Vogel zelf uit hoe het precies moet!

Laat je resultaat aan de docent zien.

</details>

---
