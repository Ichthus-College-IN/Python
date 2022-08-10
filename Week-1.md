# Week 1.1
Dit blok gaan we aan de slag met de programmeertaal Python. Het is een van de meest populaire programmeertalen. Niet per se omdat het de snelste of de beste is, maar vooral omdat het zo makkelijk is om heel erg veel verschillende dingen ermee te doen. Een grafiekje maken, een bestand verwerken, een robot aansturen of een app maken zijn een paar voorbeelden.

We gaan hiermee aan de slag in het programma Visual Studio Code. Dat is een programma waarin je standaard alleen teksten kan maken/bewerken, maar door de eindeloze hoeveelheid *extensies* ook heel veel programmeertalen kunt gebruiken. Om te werken met Python moet er dan ook een extensie voor Python geinstalleerd worden. Zie hiervoor de opdracht.

---

<details>
<summary>Opdracht</summary>

Open Visual Studio Code. Je kunt hier gewoon op zoeken in het startmenu, of naartoe klikken via `Alle vakken > Informatica > Programmeren > Visual Studio Code`. Ga zodra het geopend is naar `View > Extensions` of gebruik de shortcut <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>X</kbd>. Zoek vervolgens naar de extensie Python en installeer die. **Let op**: waarschijnlijk moet je dit elke keer dat je inlogt op een schoolcomputer opnieuw uitvoeren; daar is helaas niets aan te doen.
</details>

---

Een Python-document wordt eigenlijk altijd (en dus ook in de lessen) een *script* genoemd. Een script wordt standaard van boven naar beneden, regel voor regel uitgevoerd tot de laatste is bereikt.

## `print()` met Python
Het makkelijkste Python script dat een zichtbaar resultaat geeft is het volgende:
```python
print("Hello world!")
```

`print()` betekent hier dat in de *console* een waarde wordt geprint. Zie de opdracht. Wat in dit voorbeeld tussen de ()-haakjes staat is een *string*: een stuk tekst. Dat is te herkennen aan de dubbele apostrof <kbd>"</kbd> ervoor en erachter (dat mag ook een enkele apostrof ' zijn, maar " heeft de voorkeur).

---

<details>
<summary>Opdracht</summary>

Kopieer bovenstaande code (dat kan heel erg makkelijk door met de muis op het vak te staan en dan op het kopieersymbool rechtsbovenin het vak te klikken). Plak het in een nieuw Pythonbestand in VSCode. Klik vervolgens rechtsboven op het pijltje (Run Python file). Als het goed is zie je in de terminal onderin het scherm het resultaat van je script tevoorschijn komen.

Pas `"Hello world!"` aan naar bijvoorbeeld je eigen naam en controleer of het werkt.

</details>

---

Je kunt ook een berekening uitvoeren. Hieronder een simpel voorbeeld:
```python
print(3 + 5)
```

Dit keer staat er geen *string* tussen de haakjes, maar gewone getallen die opgeteld moeten worden. Zie de opdracht, al kun je wel raden wat er gebeurt als je de regel hierboven uitvoert.

---

<details>
<summary>Opdracht</summary>

Kopieer bovenstaande code en plak het onder (of in plaats van) de vorige opdracht. Voer je script opnieuw uit. Controleer het resultaat.

</details>

---

## Rekenen met Python
Om te rekenen met Python zijn er (onder andere) de volgende opties:
```python
1 + 1
2 - 2
3*3
4/4
5**5
```

De laatste is onbekend: <kbd>**</kbd> betekent <kbd>^</kbd>. Je ziet hier direct ook een conventie: voor en na de <kbd>+</kbd> en <kbd>-</kbd> staan een spatie, maar bij de andere tekens niet. Dit maakt het makkelijker om de rekenregels te lezen: machtsverheffen, vermenigvuldigen en delen hebben uiteraard voorrang op optellen en aftrekken. Zie de opdracht.

**Let op**: in de wiskunde kun je vermenigvuldigingen zo opschrijven:
```python
3(4 -1)
```

Maar: Python accepteert dat **niet**: je moet specifiek een vermenigvuldigingsteken zetten voor (en na) haakjes:
```python
3*(4 - 1)
```

---

<details>
<summary>Opdracht</summary>

Bereken en print het resultaat van de volgende rekensom: $3 * 1289 / (5^5 +  1875)$.

Als je dit op een traditionele rekenmachine uitrekent en je draait het display om, wat staat er dan? ;)
</details>

---

Om te werken met kommagetallen, wordt het helaas wennen: ongeveer elke programmeertaal gebruikt de 'normale' Engelse notatie: een <kbd>.</kbd> in plaats van de <kbd>,</kbd>. Als je naar het resultaat kijkt van de vorige opdracht zie je al dat er een punt staat in plaats van een komma. Hieronder ook een werkend voorbeeld:
```python
3*0.5
```

Grote getallen *mag* je opsplitsen met underscores; onderstaand zijn twee goede manieren om in Python 15 miljoen te typen (met als bonus de wetenschappelijke notatie zoals je kent van de standaard rekenmachine):
```python
15000000
15_000_000
1.5e7
```

---

<details>
<summary>Opdracht</summary>

Vermenigvuldig $\pi$ met vierenhalf miljoen door alle drie de notaties te proberen.
</details>

---

## Commentaar in Python
Als je zelf een script schrijft weet je vaak best goed wat er gebeurt. Maar het kan zijn dat je soms je script naar een ander stuurt, of kopieert vanaf internet. Daarbij komt commentaar heel erg van pas: tekst in je script die aangeeft wat er bedoeld wordt. Een voorbeeld:
```python
print(1 - 2 + 3*4**5) # dit is 3071
```

Je ziet dat de tekst vanaf het <kbd>#</kbd>-teken automatisch een donkere of onopvallende kleur krijgt (afhankelijk van je thema-instellingen). Dat is namelijk commentaar: Python doet er niks mee en negeert het gewoon.

Stijlpuntje: als je onder elkaar regels hebt van verschillende lengtes, gebruik dan <kbd>Tab</kbd> om het commentaar netjes uit te lijnen. Dat maakt het wel zo makkelijk om te lezen. Vergelijk:
```python
1 + 1 # = 2
3*4 + (0.5**6 - 5) # = 7.015625
5*(1 + 4**(0.5 + 6.37)) # = 35026131.0081...
3.141592 / 2 # = 1.570796
```
```python
1 + 1                       # = 2
3*4 + (0.5**6 - 5)          # = 7.015625
5*(1 + 4**(0.5 + 6.37))     # = 35026131.0081...
3.141592 / 2                # = 1.570796
```

---

<details>
<summary>Opdracht</summary>

Zet achter alle rekensommen die tot nu toe in je script staan het antwoord door commentaar toe te voegen.
</details>

---

Je kunt ook een heel stuk van je script in een keer commentaar maken:
```python
print("Regel 1")
"""
print("Regel 2")
print("Regel 3")
print("Regel 4")
"""
print("Regel 5")
```

Je bent in dat geval verplicht om drie enkele apostrofs <kbd>'</kbd> of dubbele apostrofs <kbd>"</kbd> te gebruiken aan het begin en einde.

---

<details>
<summary>Opdracht</summary>

Maak met bovenstaande tactiek al de code in je script tot nu toe commentaar. Dan kun je gewoon verder werken in je script en toch alle voorgaande opdrachten laten staan als je ernaar terug wilt of moet kijken.
</details>

---

## Variabelen
Uiteraard werkt het niet om alle getallen in Python te typen als je het net zo snel of sneller kunt invoeren in je rekenmachine. Daarom gaan we het aanpakken op de manier die in de wiskunde gebruikt wordt: met *variabelen*. Een voorbeeld:
```python
a = 3
b = -1.2
c = 4
print(a + b*c) # dit is 3 + -4*1.2 oftewel 3 - 4.8 = -1.8
```

---

<details>
<summary>Opdracht</summary>

Maak de volgende variabelen in je script: $a = 3867$, $b = 4$, $c = 6.5$, $d = -3192$.
Bereken en print het resultaat van de volgende rekensom: $a / (b^c + d)$.

Kijk nog eens goed naar het resultaat (als alles goed gegaan is herken je wat van een vorige opdracht)!
</details>

---

Om de omtrek en het oppervlak van een cirkel te berekenen nog een voorbeeld:
```python
pi = 3.1415926535
straal = 2.5
omtrek = 2 * pi * straal
oppervlak = pi * straal**2
```

Je ziet dat een naam dus ook bijvoorbeeld een heel woord kan zijn. En we kunnen variabelen gebruiken om nieuwe variabelen uit te rekenen. Zie opdracht 9. Je ziet ook dat hier een beetje afgeweken wordt van de stijlregel om geen spaties voor en na een vermenigvuldigingsteken te zetten. Het is in dit geval namelijk een stuk beter leesbaar met de spaties erbij. De uitzondering maakt de regel ;)

# Week 1.2

## Vergelijkingen
Je kunt in Python variabelen (en getallen) vergelijken. Een vergelijking heeft slechts twee mogelijke uitkomsten: `True` of `False`.
```python
a = 5
b = 3
print(a < b)  # False
print(a > b)  # True
c = 3.0
print(b < c)  # False
print(b >= c) # True
print(b != c) # False
print(b == c) # True
```
Kleiner dan (<) en groter dan (>) spreken voor zich; bij kleiner dan of gelijk aan (<=), of groter dan of gelijk aan (>=) **moet** het <kbd>=</kbd>-teken **achter** het vergelijkingsteken, op dezelfde volgorde als dat je het uitspreekt. Om te controleren of iets aan elkaar ongelijk is, gebruik je <kbd>!=</kbd>. Om te checken of iets aan elkaar gelijk is, **moet** je een dubbel <kbd>=</kbd>-teken gebruiken: <kbd>==</kbd>.

---

<details>
<summary>Opdracht</summary>

Test de volgende code:
```python
k = 34
l = 27
print(k = l)
```
Wat is het resultaat? 

Zorg dat de vergelijking werkt.
</details>

---

<details>
<summary>Opdracht</summary>

Een beetje natuurkunde: als je bovenaan een enorme waterglijbaan staat heb je de potentiële energie $E=mgh$. Kies voor $m$ je eigen gewicht, $g=10$, en de hoogte $h$ van de glijbaan 80 meter. Als er geen wrijving is, wordt alle potentiële energie omgezet in kinetische energie: $E = \frac{1}{2}mv^2$. Vul hier weer je eigen gewicht in, en test welke van de volgende snelheden de juiste eindsnelheid is: $v = \{30, 40, 50, 60\} m/s^2$. Doe dit door gebruik te maken van de vergelijkingen hierboven.

Een aanzet:
```python
m = 70  # gewicht in kg
g = 10  # zwaartekracht in m/s^2
h = 80  # hoogte van de glijbaan in m
E = m * g * h
```

</details>

---

## `if`-statement
Vaak zijn er stukken van je script die je alleen wilt uitvoeren als er aan een bepaalde voorwaarde wordt voldaan. Denk aan bijvoorbeeld worteltrekken: je kunt niet de wortel trekken van een negatief getal. Voordat je dus worteltrekt, moet je controleren of je getal positief of negatief is. Bekijk het voorbeeld:
```python
getal = 3
if getal >= 0:
    print(getal**0.5) # getal is groter dan 0, dus wordt 1.7... geprint
```
We maken hier gebruik van een `if`-statement: *als* de voorwaarde `True` is, *dan* wordt de code uitgevoerd. Let op: na de voorwaarde **moet** een <kbd>:</kbd>, en alles wat bij de if-statement hoort **moet** vervolgens een tab aan het begin van de regel krijgen. Vaak gebeurt dat automatisch zodra je op Enter drukt na de dubbele punt. Ben je klaar met de regels die bij de if-statement horen, moet de tab ook weer weg. Zie bijvoorbeeld:
```python
getal = 3
if getal >= 0:
    print(getal**0.5)

print("Hoi")
```
Voor de netheid staat er vaak een extra Enter om de scheiding te benadrukken.

---

<details>
<summary>Opdracht</summary>

Maak een variabele `T` en geef die een bepaalde waarde (temperatuur in graden Celsius).

Als je `T` een getal kleiner dan 15 maakt, moet je script `"Het is koud!"` printen, maar als `T` groter is dan 15, hoeft er niets te gebeuren.
</details>

---


## `if-else`-statement
Vaak is een if alleen niet genoeg, en wil je ook iets doen als er *niet* aan de voorwaarde wordt voldaan. In het geval van worteltrekken bijvoorbeeld een waarschuwing printen: "let op, negatief getal!". Dat kan zo:
```python
getal = -3
if getal >= 0:
    print(getal**0.5)   # getal >= 0 is niet waar, dus dit gebeurt niet
else:
    print("Let op, negatief getal!")    # dit wordt dus wel uitgevoerd
```
Een `else` heeft geen voorwaarde: het wordt uitgevoerd in alle andere gevallen (als het getal dus kleiner is dan 0). Vergeet uiteraard de dubbele punt en tab niet.

---

<details>
<summary>Opdracht</summary>

Breidt het script van de vorige opdracht uit: als `T` gelijk aan of groter is dan 15 moet er geprint worden: `"Het is warm."`.
</details>

---

## `if-elif-else` statement
Je kunt heel veel extra voorwaarden toevoegen. In het geval van worteltrekken hoef je bijvoorbeeld geen wortel te trekken als het getal gelijk is aan 0, want wortel(0) = 0. Check de uitbreiding:
```python
getal = 0
if getal > 0:
    print(getal**0.5)   # getal > 0 is niet waar, dus dit gebeurt niet
elif getal == 0:
    print(0)            # dit is waar, dus kunnen we gewoon 0 printen
else:
    print("Let op, negatief getal!")    # dit wordt niet meer uitgevoerd
```
De `elif` staat eigenlijk voor `else if`, en heeft uiteraard ook een voorwaarde nodig: "als .. dan ..". Ook hier is de dubbele punt natuurlijk weer nodig, net als de tab.

Je kunt er in principe eindeloos veel onder elkaar zetten: `if-elif-elif-elif-elif-elif-elif....else`. Je kunt ook de `else` achterwege laten en het gewoon houden bij `if-elif` (en eventueel extra `elif`'s).

---

<details>
<summary>Opdracht</summary>

Breidt het script van de afgelopen twee opdrachten nog verder uit: als `T` kleiner is dan 0 graden moet het script printen: `"Het vriest!"`. Zorg dat je gebruik maakt van de `if-elif-else`-constructie.
</details>

---

## integers, floats en strings
Voordat we door kunnen gaan naar het volgende onderdeel kijken we naar het verschil tussen tekst en getallen.

Getallen zijn er in twee soorten: <kbd>int</kbd>, de afkorting van integer, en <kbd>float</kbd>, wat meestal gewoon een float wordt genoemd. Een integer is een geheel getal; een float een kommagetal.

Een string is een stuk tekst zoals we eerder gezien hebben bij `"Hello world"`, en daar staan **altijd** apostrofs voor en achter. Je kunt uiteraard ook getallen in een stuk tekst tegenkomen: `"Ik ben 20 jaar"`. De 20 die hier staat is niet echt een getal, maar een string, omdat er apostrofs voor en achter staan. `"20"` is dus **niet** hetzelfde als `20`! Of, als je het echt op de Python manier bekijkt:
```python
print("20" == 20)       # dit print False!
```

Het is wel mogelijk om een getal dat in een string staat om te zetten in een officiele integer of float:
```python
tekst = "20"
getal = int(tekst)      # resultaat: 20 omdat int een geheel getal is
getal = float(tekst)    # resultaat: 20.0 omdat float een kommagetal is
```

Eventueel kan het ook andersom:
```python
getal = 14
tekst = str(getal)      # resultaat: "14"
getal2 = 14.8
tekst2 = str(getal2)    # resultaat: "14.8"
```

Je kunt ook een float naar een integer omzetten en andersom:
```python
geheelgetal = 14
kommagetal = float(geheelgetal) # resultaat: 14.0
kommagetal2 = 3.9
geheelgetal2 = int(kommagetal2) # resultaat: 3
```

**Let op**! Als je een float omzet in een int, wordt alles na de punt **weggegooid**. Dat is dus niet hetzelfde als afronden!

## `input()` van een gebruiker
Soms wil je de gebruiker van je programma om input vragen. Of je wilt makkelijk een paar dingen testen. Daarvoor is invoer van een gebruiker best praktisch. Hoe werkt dat?
```python
invoer = input("Voer iets in:" )
print(invoer)
```

In de console komt dan een mogelijkheid om te typen. Zodra je op Enter drukt eindigt de invoer, en wordt de input opgeslagen in de variabele `invoer`. 

**Let op**: `input()` maakt van je invoer een `string`, dus als je een getal invoert moet je die nog omzetten naar een integer of float! Voorbeeld:

```python
invoer = input("Voer een getal in: ")
x = int(invoer) / 2
print(x)
```

---

<details>
<summary>Opdracht</summary>

Test bovenstaand voorbeeld. Probeer hele getallen, kommagetallen, letters en combinaties van cijfers en letters. Wat gaat wel goed, en wat gaat niet goed?
</details>

---

# Week 1.3

## `While`-loop
Eerder is de `if-else`-constructie aan de orde geweest. Daarbij wordt eenmalig gekeken of er aan een voorwaarde voldaan wordt. Andere keren doe je het liefst iets *zolang* een voorwaarde geldt. Je kunt bijvoorbeeld alle getallen van 0 tot en met 10 printen met de volgende code:
```python
x = 0           # startwaarde 0
while x < 10:   # zolang x kleiner is dan 10...
    print(x)    # print de waarde van x
    x = x + 1   # en tel 1 op bij x
```

---

<details>
<summary>Opdracht</summary>

Test de code hierboven uit. Als je goed kijkt, zie je dat het getal 10 helaas toch niet geprint wordt. Vind twee (of met een beetje creativiteit drie of vier) manieren om alle getallen van 0 tot en **met** 10 te printen waarbij je gebruik maakt van (een variant van) bovenstaande `while`-loop.
</details>

---

## Combineren van statements

Uiteraard is het mogelijk om `while` en `if(-else)` ook door elkaar heen te gebruiken / te combineren. Bekijk het volgende voorbeeld:
```python
y = 20
while y > 0:
    print(y)
    if y <= 10:
        print("Doei")
    else:
        print("Hoi")
    y = y - 1
```

**Let op**! Kijk goed naar de tabs voor de regels: die moeten wel matchen met de statement waar ze bij horen. 

---

<details>
<summary>Opdracht</summary>

Bedenk wat er zou moeten gebeuren als je bovenstaande code uitvoert en controleer dat ook. Test daarna eens het volgende script:
```python
z = 0
while z != 20:
    print(z)
    if z <= 10:
        print("Kleiner of gelijk aan 10")
        z = z + 1
```
Tip: klik in de terminal onderin en druk op <kbd>Ctrl</kbd> <kbd>C</kbd> als het script te lang duurt en je wilt het stoppen.

Waarom gaat dit mis? Los het probleem op!
</details>

---


## `list`: een lijst
Wat we voor de basis van Python ook zeker nodig hebben is een `list`. Die is niet zo spannend: het is een lijst van waarden (of variabelen). Voorbeeld:
```python
x = [1, 2, 3, 4, 5]
y = ["a", "b", "c", "d"]

k = 3
l = "hoi"
m = 2.78
z = [k, l, m]
```

Een handig trucje met een lijst is dat je de lengte van een lijst op kunt vragen:
```python
len(x)  # 5
len(y)  # 4
len(z)  # 3
```

Je kunt de elementen van een lijst ook los bekijken. Daarvoor maken we gebruik van een *index*, een getal dat gebruikt wordt om de waarde op een plek in een lijst te bekijken:
```python
print(x[0])
print(y[2])
```

Ja.. een computer begint bij index 0. Als voorbeelden: `x[0]` heeft als waarde `1`, `x[1]` heeft als waarde `2`, `y[2]` heeft als waarde `"c"`, en `z[1]` heeft als waarde `"hoi"`.

---

<details>
<summary>Opdracht</summary>

Gebruik een `while`-loop om alle elementen uit `x` te printen. Maak gebruik van het volgende opstapje:
```python
i = 0
print(x[i])
```

Denk goed na: hoe gebruik je `i` en `len(x)` zo goed mogelijk? Je mag het getal 5 niet gebruiken! 
</details>

---

## `for`-loop
Als een-na-laatste ingrediënt: de `for`-loop. Een `for`-loop lijkt soms best veel op een `while`-loop, maar is vaak een stuk netter. Kijk maar naar dit voorbeeld:
```python
for element in x:
    print(element)
```

Hoewel het er heel anders ziet dan een `while`-loop, gebeurt er hetzelfde. Snap je niet helemaal wat er gebeurt? Vertaal dan de twee regels die er staan en maak er een Nederlandse zin van. Als geheugensteuntje kun je `for` ook zien als `foreach` (sommige programmeertalen gebruiken dat ook in plaats van `for`). 

Een `for`-loop is een van de meest nuttige dingen om te gebruiken tijdens het programmeren: je weet eigenlijk altijd zeker dat je elk getal, letter of tekst langsgaat.

*Tip: je mag zelf de namen van de variabelen bepalen. Je bent dus helemaal niet verplicht om `element` te gebruiken als naam; het mag net zo goed de naam `Hoi` of `abcd95` krijgen.*

---

<details>
<summary>Opdracht</summary>

Print de inhoud van de lijsten `x`, `y` en `z` van een paar voorbeelden terug door middel van een `for`-loop voor elke lijst.
</details>

---

## `range()`: makkelijk een lijst maken
Het kan best veel werk zijn om een lijst van getallen te maken van bijvoorbeeld 1 t/m 100. Daarvoor is een handige `range()`-functie. Tussen de haakjes kun je een paar dingen invullen: **op volgorde** de startwaarde, stopwaarde en eventueel de stapgrootte, die standaard +1 is. De stapgrootte moet een integer zijn. Voorbeelden:
```python
a = range(start = 0, stop = 10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = range(3, 11)                # [3, 4, 5, 6, 7, 8, 9, 10]
c = range(0, 100, 10)           # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
d = range(5, 0)                 # [] (leeg, want met stapgrootte +1 kun je niet van 5 naar 0)
e = range(8, -2, -1)            # [8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
f = range(start = 8, stop = -4, step = -2)  # [8, 6, 4, 2, 0, -2]
```

Zoals je ziet wordt het laatste getal niet meegenomen in de lijst. Daarnaast kun je ook achteruit tellen, maar dan moet je wel specifiek zeggen dat de stapgrootte -1 is. Anders is de lijst gewoon leeg.

Je mag ook de namen `start`, `stop`, en `step` specifiek aangeven, maar dat is niet verplicht. Het kan het wel makkelijker maken om te lezen, al wordt het er ook een stuk langer van.

---

<details>
<summary>Opdracht</summary>

Maak een lijst `l` die elk 7e getal bevat van 0 tot en **met** 70. Print elk getal in `l` door middel van een `for`-loop om het te controleren.
</details>

---

<details>
<summary>Slotopdracht 1</summary>

Schrijf een script dat aan jou als gebruiker om input vraagt en vervolgens wel of niet een wortel trekt. Dat herhaalt zich tot je het getal nul invoert: dan stopt het script.

Vraag hiervoor als eerste om input van de gebruiker. Gebruik vervolgens een `while`-loop. Je moet dan testen of de invoer gelijk is aan 0 (dan stopt de loop), en daarna controleren of het getal positief of negatief is. Als het getal negatief is, print dan `"Dombo, geen negatief getal"`. Print anders de wortel van het getal. Vraag als laatste weer opnieuw om input, waarna je weer vooraan in de loop komt.
</details>

---

<details>
<summary>Slotopdracht 2</summary>

Schrijf een script dat voor de temperaturen van -10 tot en **met** 100 Fahrenheit met stappen van 5 Fahrenheit de temperatuur in graden Celsius berekent. 

Print voor elke stap

* de temperatuur in Fahrenheit, 
* de berekende temperatuur in Celsius, 
* en de conclusie of het wel of niet vriest. 

(Hint: controleer dus of de temperatuur in graden Celsius kleiner of groter is dan 0!)

De formule om Fahrenheit om te rekenen naar Celsius: $C=\frac{5}{9}(F-32)$.
</details>

---
