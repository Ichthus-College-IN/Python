# Week 2

Tijdens week 1 hebben we rechtstreeks in de Python terminal geprogrammeerd: één regeltje per keer. Maar vaak wil je meer dingen in één keer doen, of vaker opnieuw uitvoeren. Dan is het fijner om een heel bestand in één keer uit te voeren.

We gaan hiermee aan de slag in het programma Visual Studio Code. Dat is een programma waarin je standaard alleen teksten kan maken/bewerken, maar door de eindeloze hoeveelheid *extensies* ook heel veel programmeertalen kunt gebruiken. Om te werken met Python moet er dan ook een extensie voor Python geinstalleerd worden. Zie hiervoor de opdracht.

---

<details>
<summary>Opdracht</summary>

Open Visual Studio Code. Je kunt hier gewoon op zoeken in het startmenu, of naartoe klikken via `Alle vakken > Informatica > Programmeren > Visual Studio Code`. Ga zodra het geopend is naar `View > Extensions` of gebruik de shortcut <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>X</kbd>. Zoek vervolgens naar de extensie Python en installeer die. **Let op**: waarschijnlijk moet je dit elke keer dat je inlogt op een schoolcomputer opnieuw uitvoeren; daar is helaas niets aan te doen.
</details>

---


## Werken met een script
Een Python-document wordt eigenlijk altijd (en dus ook in de lessen) een *script* genoemd. Een script wordt standaard van boven naar beneden, regel voor regel uitgevoerd tot de laatste is bereikt.

Een groot verschil tussen de terminal en een script, is dat je bij een script niet zomaar een antwoord of resultaat ziet. Tot nu toe zag het er bijvoorbeeld zo uit:
```
>>> 5 + 3
8
>>> naam = "bns"
>>> naam
'bns'
```

De regels met een 'antwoord' zie je niet als je een script 'uitvoert' (_runnen -> runt_). Je moet dan specifiek het resultaat _printen_.

Het makkelijkste Python script dat een zichtbaar resultaat geeft is het volgende:
```python
print("Hello world!")
```

`print()` betekent hier dat in de *console* een waarde wordt geprint. Zie de opdracht. Wat in dit voorbeeld tussen de ()-haakjes staat is datgene wat je wilt zien (zoals `5 + 3`, `naam`). 

---

<details>
<summary>Opdracht</summary>

Kopieer bovenstaande code (dat kan heel erg makkelijk door met de muis op het vak te staan en dan op het kopieersymbool rechtsbovenin het vak te klikken). Plak het in een nieuw Pythonbestand in VSCode. Klik vervolgens rechtsboven op het pijltje (Run Python file). Als het goed is zie je in de terminal onderin het scherm het resultaat van je script tevoorschijn komen.

Pas `"Hello world!"` aan naar bijvoorbeeld je eigen naam en controleer of het werkt.

</details>

---


## Commentaar in Python
Als je zelf een script schrijft weet je vaak best goed wat er gebeurt. Maar het kan zijn dat je soms je script naar een ander stuurt, of kopieert vanaf internet. Daarbij komt commentaar heel erg van pas: tekst in je script die aangeeft wat er bedoeld wordt. Ter herinnering:
```python
print(1 - 2 + 3*4**5) # dit is 3071
```

Je ziet dat de tekst vanaf het `#`-teken automatisch een donkere of onopvallende kleur krijgt (afhankelijk van je thema-instellingen). Dat is namelijk commentaar: Python doet er niks mee en negeert het gewoon.

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


## Vergelijkingen
Je kunt in Python variabelen (en getallen en strings) vergelijken. Een vergelijking heeft slechts twee mogelijke uitkomsten: `True` of `False`.
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
Kleiner dan (<) en groter dan (>) spreken voor zich; bij kleiner dan of gelijk aan (<=), of groter dan of gelijk aan (>=) **moet** het `=`-teken **achter** het vergelijkingsteken, op dezelfde volgorde als dat je het uitspreekt. Om te controleren of iets aan elkaar ongelijk is, gebruik je `!=`. Om te checken of iets aan elkaar gelijk is, **moet** je een dubbel `=`-teken gebruiken: `==`.

---

<details>
<summary>Opdracht</summary>

Je wilt de twee variabelen `k` en `l` vergelijken: hebben ze dezelfde waarde? Het antwoord moet `True` of `False` zijn.

Test daarvoor de volgende code:
```python
k = 34
l = 27
print(k = l)
```
Wat is het resultaat? 

Zorg dat de vergelijking werkt.
</details>

---


## `if`-statement
Je kunt op basis van een vergelijking keuzes maken. Bijvoorbeeld: als je legaal een biertje wilt kopen, moet je wel minimaal 18 jaar zijn. Je moet dus vergelijken of de leeftijd van iemand minimaal 18 is of lager, en op basis van de uitkomst mag je het kopen of niet.

In codetaal:
```python
age = 16
if age >= 18:
    print("Akkoord")
```
We zien hier weer nieuwe dingen:
* De voorwaarde start met `if`. Als er aan de voorwaarde wordt voldaan (`True`), wordt de code die erbij hoort uitgevoerd, anders niet.
* Aan het einde van de voorwaarde staat een `:`. Die dubbele punt betekent eigenlijk "dan". (_Als_ leeftijd minimaal 18, _dan_...)
* Vóór de code die uitgevoerd moet worden, staat een <kbd>Tab</kbd>. Elke regel die erbij hoort, moet een Tab aan het begin hebben.
* Ben je klaar met de regels die bij de `if`-statement horen, moet de tab ook weer weg. Zie bijvoorbeeld:
```python
age = 16
if age >= 18:
    print("Akkoord")

print("Afrekenen a.u.b.")
```
Voor de netheid staat er vaak een extra <kbd>Enter</kbd> achter om de scheiding te benadrukken.

---

<details>
<summary>Opdracht</summary>

Maak een variabele `t` en geef die een bepaalde waarde (temperatuur in graden Celsius).

Als je `t` een getal kleiner dan 15 maakt, moet je script `"Het is koud!"` printen, maar als `t` groter is dan 15, hoeft er niets te gebeuren.
</details>

---


## `if-else`-statement
Vaak is een if alleen niet genoeg, en wil je ook iets doen als er *niet* aan de voorwaarde wordt voldaan. In het geval van worteltrekken bijvoorbeeld een waarschuwing printen: "let op, negatief getal!". Dat kan zo:
```python
age = 16
if age >= 18:
    print("Akkoord")
else:
    print("Je bent niet oud genoeg")
```
Een `else` heeft geen voorwaarde: het wordt uitgevoerd in alle andere gevallen (als de leeftijd dus lager is dan 18). Vergeet uiteraard de dubbele punt en tab niet.

---

<details>
<summary>Opdracht</summary>

Breid het script van de vorige opdracht uit: als `t` gelijk aan of groter is dan 15 moet er geprint worden: `"Het is warm."`.
</details>

---

## `if-elif-else` statement
Je kunt heel veel extra voorwaarden toevoegen. Cassièries moeten bijvoorbeeld tot grofweg 25 jaar je ID controleren, daarboven krijg je het automatisch mee. Check het voorbeeld:
```python
if age_guess < 15:
    print("Je moet minimaal 18 zijn.")
elif age_guess <= 25:
    print("ID-kaart tonen a.u.b.")
else:
    print("Akkoord!")
```
De `elif` staat eigenlijk voor `else if`, en heeft uiteraard ook een voorwaarde nodig: "als .. dan ..". Ook hier is de dubbele punt natuurlijk weer nodig, net als de Tab.

Je kunt er in principe eindeloos veel onder elkaar zetten: `if-elif-elif-elif-elif-elif-elif....else`. Of alleen `if-elif` (en eventueel extra `elif`'s).

---

<details>
<summary>Opdracht</summary>

Breid het script van de afgelopen twee opdrachten nog verder uit: als `t` kleiner is dan 0 graden moet het script printen: `"Het vriest!"`. Zorg dat je gebruik maakt van de `if-elif-else`-constructie. Let goed op dat het juiste resultaat wordt geprint voor temperaturen onder nul! Je zult meerdere dingen moeten aanpassen.
</details>

---

<details>
<summary>Opdracht</summary>

Stel dat je rooster voor een dag er zo uit ziet:
```
3: nederlands
4: biologie
5: informatica
6: informatica
7: wiskunde
```
De andere uren ben je vrij. Maak het onderstaande programma zo af dat je aan de hand van het uur print welk vak je hebt. Vergeet niet het 8e en 9e (en alles daarna) toe te voegen: dan ben je ook vrij.
```python
uur = 1

if uur <= 2:
    print("je bent vrij")
# voeg hier de rest van de dag toe!
```
</details>

---


## integers, floats en strings
Voordat we door kunnen gaan naar het volgende onderdeel kijken we naar het verschil tussen tekst en getallen.

Getallen zijn er in twee soorten: `int`, de afkorting van integer, en `float`, wat gewoon een float wordt genoemd. Een integer is een geheel getal; een float een kommagetal.

Een string is een stuk tekst zoals we eerder gezien hebben bij `"Hello world"`, en daar staan **altijd** apostrofs voor en achter. Je kunt uiteraard ook getallen in een stuk tekst tegenkomen: `"Ik ben 20 jaar"`. De 20 die hier staat is niet écht een getal, maar een string, omdat er apostrofs voor en achter staan. `"20"` is dus **niet** hetzelfde als `20`! Of, als je het op de Python manier bekijkt:
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

In de console komt de mogelijkheid om te typen: klik achter de tekst `Voer iets in: `. Zodra je op Enter drukt eindigt de invoer, en wordt de input opgeslagen in de variabele `invoer`. 

**Let op**: `input()` maakt van je invoer een `string`, dus als je een getal invoert moet je die nog omzetten naar een integer of float! Voorbeeld:

```python
invoer = input("Voer een getal in: ")
x = int(invoer) / 2
print("U hebt het dubbele ingevoerd van: ")
print(x)
```

---

<details>
<summary>Opdracht</summary>

Test bovenstaand voorbeeld meerdere keren. Probeer hele getallen, kommagetallen, letters en combinaties van cijfers en letters. Wat gaat wel goed, en wat gaat niet goed?
</details>

---


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

Test de code hierboven uit. Als je goed kijkt naar de uitvoer, zie je dat het getal 10 helaas toch niet geprint wordt. Vind twee (of met een beetje creativiteit drie of vier) manieren om alle getallen van 0 tot en **met** 10 te printen waarbij je gebruik maakt van (een variant van) bovenstaande `while`-loop.
</details>

---

<details>
<summary>Opdracht</summary>

Maak een programma dat de gebruiker eindeloos om `input()` vraagt. Bedenk een voorwaarde die _altijd_ waar is, zodat de _loop_ eindeloos doorgaat. Elke keer als de gebruiker iets invoert, moet je het eerste karakter printen.

_Tip: de invoer van een gebruiker is een string, ofwel 'lijst' van karakters. Hoe kun je dan ook alweer het eerste karakter opvragen?_
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

Eerder heb je een script gemaakt dat aangeeft welke les je hebt, maar dan zag je maar één les. Nu ga je ervoor zorgen dat je je rooster voor de hele dag ziet.

Maak een variabele `uur` die begint op 1. Maak daarna een `while`-loop die alle uren tot het 10e uur langs gaat. Voeg als laatste de `if-else` stukken toe zoals in de eerdere opdracht; dat begon zo:
```python
if uur <= 2:
    print("je bent vrij")
```
</details>

---


## Throwback: `list`
We hebben in de eerste week al gekeken naar lists. Nog een samenvatting om het even te herinneren:
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

Je kunt de elementen van een lijst ook los bekijken. Daarvoor maken we gebruik van een *index*, een getal dat gebruikt wordt om de waarde op een plek in een lijst te bekijken. Je herkent ze aan de vierkante haken `[..]`:
```python
print(x[0])     # 1
print(y[2])     # "c"
```

Oja: een computer begint te tellen vanaf 0!

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


## `range()`: makkelijk een lijst maken
Het kan best veel werk zijn om een lijst van getallen te maken van bijvoorbeeld 1 t/m 100. Daarvoor is een handige `range()`-functie. Tussen de haakjes kun je een paar dingen invullen: **op volgorde** de startwaarde, stopwaarde en eventueel de stapgrootte, die standaard +1 is. De stapgrootte moet een integer zijn. Voorbeelden:


```python
range(start, stop, step)    # <-- vul zelf de start, stop en step in

a = range(0, 10)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = range(3, 11)            # [3, 4, 5, 6, 7, 8, 9, 10]
c = range(0, 100, 10)       # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
d = range(5, 0)             # [] (leeg, want met stapgrootte +1 kun je niet van 5 naar 0)
e = range(8, -2, -1)        # [8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
```

Zoals je ziet wordt het laatste getal niet meegenomen in de lijst. Daarnaast kun je ook achteruit tellen, maar dan moet je wel specifiek zeggen dat de stapgrootte -1 (of een ander getal) is. Anders is de lijst gewoon leeg.

---

<details>
<summary>Opdracht</summary>

Maak een lijst `l` die elk 7e getal bevat van 0 tot en **met** 70. Print elk getal in `l` door middel van een `while`-loop om het te controleren. Kijk daarvoor terug naar de vorige opdracht.
</details>

---


## `for`-loop
Als laatste ingrediënt: de `for`-loop. Een `for`-loop lijkt soms best veel op een `while`-loop, maar is vaak een stuk netter. Als je bijvoorbeeld elk element in `l` van de vorige opdracht wilt printen::
```python
for element in l:
    print(element)
```

Hoewel het er heel anders ziet dan een `while`-loop, gebeurt er hetzelfde. Snap je niet helemaal wat er gebeurt? Vertaal dan de twee regels die er staan en maak er een Nederlandse zin van. Als geheugensteuntje kun je `for` ook zien als `foreach` (sommige programmeertalen gebruiken dat ook in plaats van `for`). 

Een `for`-loop is een van de meest nuttige dingen om te gebruiken tijdens het programmeren: je weet eigenlijk altijd zeker dat je elk getal, letter of tekst langsgaat.

*Tip: je mag zelf de namen van de variabelen bepalen. Je bent dus helemaal niet verplicht om `element` te gebruiken als naam; het mag net zo goed de naam `Hoi` of `abcd95` krijgen.*

---

<details>
<summary>Opdracht</summary>

Print de getallen -20 tot en met 100 met stappen van 10 door gebruik te maken van een `range()`-lijst en een `for`-loop.
</details>


---

<details>
<summary> Slotopdracht ⭐⭐⭐</summary>

Het spel Dungeons & Dragons gebruikt dobbelstenen met soms tot wel 20 zijden - veel meer dan de 6 die we normaal gewend zijn. Een klassieke vraag bij een dobbelsteen is: wat is de som van alle zijden? Dat wordt wel een vervelende som als je dat tot en met 20 gaat uitrekenen. We gaan daarom een programmaatje bouwen waarbij een gebruiker een getal kan invullen (het aantal zijden van de dobbelsteen), en het programma geeft als antwoord wat het aantal ogen is op zo'n dobbelsteen.

Het programma stopt zodra de gebruiker een getal kleiner dan of gelijk aan 1 invoert (dat is namelijk geen dobbelsteen).

Je moet daarvoor twee _loops_ gebruiken: een `while`-loop die zich herhaalt zolang de invoer groter is dan 1, en daar 'binnen' een `for`-loop die de som van alle zijden berekent. 

De meeste onderdelen ben je al eerder tegengekomen:
* Hoe je een `while`-loop maakt.
* Hoe je een gebruiker om `input` vraagt, en hiervan een geheel getal maakt.
* Hoe je een `for`-loop maakt..
* Hoe je een `range` maakt (die je gebruikt in de `for`-loop).

Wel een hint voor het berekenen van het aantal ogen:

```python
ogen = 0
# (schrijf deze regel zelf:) voor alle zijden van de dobbelsteen...
    ogen = ogen + zijde   # 'zijde' is het aantal ogen op deze zijde, die tellen we op bij het totaal
print(ogen)
```

**Beoordeling:**
* : niet ingeleverd / werkt totaal niet
* ⭐: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* ⭐⭐: ingeleverd en (zo goed als) correct op minder goede manier
* ⭐⭐⭐: ingeleverd en helemaal correct op de manier zoals geleerd in het hoofdstuk
</details>

---