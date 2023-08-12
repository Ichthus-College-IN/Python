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

De regels met een 'antwoord' zie je niet als je een script 'uitvoert'. Je moet dan specifiek het resultaat _printen_.

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
Als je zelf een script schrijft weet je vaak best goed wat er gebeurt. Maar het kan zijn dat je soms je script naar een ander stuurt, of kopieert vanaf internet. Daarbij komt commentaar heel erg van pas: tekst in je script die aangeeft wat er bedoeld wordt. Een voorbeeld:
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
Kleiner dan (<) en groter dan (>) spreken voor zich; bij kleiner dan of gelijk aan (<=), of groter dan of gelijk aan (>=) **moet** het `=`-teken **achter** het vergelijkingsteken, op dezelfde volgorde als dat je het uitspreekt. Om te controleren of iets aan elkaar ongelijk is, gebruik je `!=`. Om te checken of iets aan elkaar gelijk is, **moet** je een dubbel `=`-teken gebruiken: `==`.

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


## `if`-statement
Vaak zijn er stukken van je script die je alleen wilt uitvoeren als er aan een bepaalde voorwaarde wordt voldaan. Denk aan bijvoorbeeld worteltrekken: je kunt niet de wortel trekken van een negatief getal. Voordat je dus worteltrekt, moet je controleren of je getal positief of negatief is. Bekijk het voorbeeld:
```python
getal = 3
if getal >= 0:
    print(getal**0.5) # getal is groter dan 0, dus wordt 1.7... geprint
```
We maken hier gebruik van een `if`-statement: *als* de voorwaarde `True` is, *dan* wordt de code uitgevoerd. Let op: na de voorwaarde **moet** een `:`, en alles wat bij de if-statement hoort **moet** vervolgens een tab aan het begin van de regel krijgen. Vaak gebeurt dat automatisch zodra je op Enter drukt na de dubbele punt. Ben je klaar met de regels die bij de if-statement horen, moet de tab ook weer weg. Zie bijvoorbeeld:
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

Breid het script van de vorige opdracht uit: als `T` gelijk aan of groter is dan 15 moet er geprint worden: `"Het is warm."`.
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

Breid het script van de afgelopen twee opdrachten nog verder uit: als `T` kleiner is dan 0 graden moet het script printen: `"Het vriest!"`. Zorg dat je gebruik maakt van de `if-elif-else`-constructie. Let goed op dat het juiste resultaat wordt geprint voor temperaturen onder nul!
</details>

---

## integers, floats en strings
Voordat we door kunnen gaan naar het volgende onderdeel kijken we naar het verschil tussen tekst en getallen.

Getallen zijn er in twee soorten: `int`, de afkorting van integer, en `float`, wat meestal gewoon een float wordt genoemd. Een integer is een geheel getal; een float een kommagetal.

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

Het volgende script moet de getallen 0 tot 20 printen. Daarbij moet bij de getallen kleiner of gelijk aan 10 een extra regel geprint worden. Er is echter een fout waardoor het niet goed gaat. Voer het script uit en bedenk wat er fout gaat.
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
range(start, stop, step)

a = range(0, 10)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = range(3, 11)            # [3, 4, 5, 6, 7, 8, 9, 10]
c = range(0, 100, 10)       # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
d = range(5, 0)             # [] (leeg, want met stapgrootte +1 kun je niet van 5 naar 0)
e = range(8, -2, -1)        # [8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
f = range(8, -4, -2)        # [8, 6, 4, 2, 0, -2]
```

Zoals je ziet wordt het laatste getal niet meegenomen in de lijst. Daarnaast kun je ook achteruit tellen, maar dan moet je wel specifiek zeggen dat de stapgrootte -1 is. Anders is de lijst gewoon leeg.

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

**Beoordeling:**
* 0.00pt: niet ingeleverd / werkt totaal niet
* 0.25pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 0.50pt: ingeleverd en (zo goed als) correct op minder goede manier
* 0.75pt: ingeleverd en helemaal correct op de manier zoals geleerd in het hoofdstuk
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

**Beoordeling:**
* 0.00pt: niet ingeleverd / werkt totaal niet
* 0.25pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 0.50pt: ingeleverd en (zo goed als) correct op minder goede manier
* 0.75pt: ingeleverd en helemaal correct op de manier zoals geleerd in het hoofdstuk
</details>

---
