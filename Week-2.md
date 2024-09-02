# Week 2

Tijdens week 1 hebben we rechtstreeks in de Python terminal geprogrammeerd: één regeltje per keer. Maar vaak wil je meer dingen in één keer doen, of vaker opnieuw uitvoeren. Dan is het fijner om een heel bestand in één keer uit te voeren.

We gaan hiermee aan de slag in het programma Visual Studio Code. Dat is een programma waarin je standaard alleen teksten kan maken/bewerken, maar door de eindeloze hoeveelheid *extensies* ook heel veel programmeertalen kunt gebruiken. Om te werken met Python moet er dan ook een extensie voor Python geinstalleerd worden. Zie hiervoor de opdracht.

---

<details>
<summary>Opdracht</summary>

Open Visual Studio Code. Je kunt hier gewoon op zoeken in het startmenu, of naartoe klikken via `Alle vakken > Informatica > Programmeren > Visual Studio Code`. Navigeer zodra het programma geopend is naar `View > Extensions` of gebruik de shortcut <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>X</kbd>. Zoek vervolgens naar de extensie Python en installeer die. **Let op**: waarschijnlijk moet je dit elke keer dat je inlogt op een schoolcomputer opnieuw uitvoeren; daar is helaas niets aan te doen.
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

De 'antwoorden' hierboven zie je niet als je een script 'uitvoert' (_runnen -> runt_). Je moet dan specifiek het resultaat _printen_.

Het makkelijkste Python script dat een zichtbaar resultaat geeft is het volgende:
```python
print("Hello world!")
```

`print()` betekent hier dat in de *console* een zinnetje of bijv. getal wordt geprint. Zie de opdracht. Wat in dit voorbeeld tussen de ()-haakjes staat is datgene wat je wilt zien. 

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

Je ziet dat de tekst vanaf het `#`-teken automatisch een donkere of onopvallende kleur krijgt (afhankelijk van je thema-instellingen). Dat is namelijk commentaar: Python doet er niks mee en negeert het gewoon. Commentaar lijnen we zo veel als mogelijk netjes uit zodat het er overzichtelijk uitziet.
```python
1 + 1                       # = 2
3*4 + (0.5**6 - 5)          # = 7.015625
5*(1 + 4**(0.5 + 6.37))     # = 35026131.0081...
3.141592 / 2                # = 1.570796
```


## Vergelijkingen
Je kunt in Python variabelen (zoals getallen en strings) vergelijken. Een vergelijking heeft slechts twee mogelijke uitkomsten: `True` of `False`. Python kent zes mogelijke vergelijkingen:
1. `a > b`: dit is `True` als `a` _groter_ is dan `b` (anders `False`).
1. `a < b`: dit is `True` als `a` _kleiner_ is dan `b` (anders `False`).
1. `a >= b`: dit is `True` als `a` _groter is dan of gelijk aan_ `b` (anders `False`).
1. `a <= b`: dit is `True` als `a` _kleiner is dan of gelijk aan_ `b` (anders `False`).
1. `a == b`: dit is `True` als `a` _gelijk_ is aan `b` (anders `False`).
1. `a != b`: dit is `True` als `a` _niet_ gelijk is dan `b` (anders `False`).

Een voorbeeldje:
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

> [!IMPORTANT]
> Bij kleiner dan of gelijk aan (<=), of groter dan of gelijk aan (>=) **moet** het `=`-teken **achter** het vergelijkingsteken, op dezelfde volgorde als dat je het uitspreekt. 

> [!IMPORTANT]
> Om te checken of iets aan elkaar gelijk is, **moet** je een dubbel `=`-teken gebruiken: `==`.

---

<details>
<summary>Opdracht</summary>

Zoek uit wat het antwoord is op de volgende vragen:
1. Is `3` gelijk aan `3.0`?
1. Welke is groter, `"A"` of `"a"`? (En dan bedoelen we _niet_ de grootte van de letter, maar volgens Python.)
1. Is `"abc"` gelijk aan `["abc"]`? (De tweede variant is een _lijst_: zie de vierkante haken.)
1. Kun je uitvinden welke groter is? `"abc"` of `["abc"]`.

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
* De voorwaarde start met `if`. Alleen als er aan de voorwaarde wordt voldaan (`True`), wordt de code die erbij hoort uitgevoerd, anders wordt die overgeslagen.
* Aan het einde van de regel met de voorwaarde staat een `:`. Die dubbele punt betekent eigenlijk "dan". (_Als_ leeftijd minimaal 18, _dan_...)
* Aan het begin van de regels met code die uitgevoerd moet worden, staat een <kbd>Tab</kbd>. **Elke regel die erbij hoort, moet een Tab aan het begin hebben.**
* Ben je klaar met de regels die bij de `if`-statement horen, dan moet de <kbd>Tab</kbd> ook weer weg. Zie bijvoorbeeld:
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
Vaak is een `if` alleen niet genoeg, en wil je ook iets doen als er *niet* aan de voorwaarde wordt voldaan. Bijvoorbeeld: als je een biertje wil kopen maar je bent nog geen 18, dan wordt je geweigerd. Dat kan zo:
```python
age = 16
if age >= 18:
    print("Akkoord")
else:
    print("Je bent niet oud genoeg")
```
Een `else` heeft geen voorwaarde: het wordt uitgevoerd in alle andere gevallen (als de leeftijd dus lager is dan 18). 

> [!NOTE]
> Vergeet niet de dubbele punt `:` en de <kbd>Tab</kbd> toe te voegen!

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

Je kunt er in principe eindeloos veel onder elkaar zetten: `if-elif-elif-elif-elif-elif-elif....else`. Of alleen `if-elif`, zonder `else`.

---

<details>
<summary>Opdracht</summary>

Breid het script van de afgelopen twee opdrachten nog verder uit: als `t` kleiner is dan 0 graden moet het script printen: `"Het vriest!"`. Zorg dat je gebruik maakt van de `if-elif-else`-constructie. Let goed op dat het juiste resultaat wordt geprint voor temperaturen onder nul! Je zult meerdere dingen moeten aanpassen.
</details>

---

<details>
<summary>Opdracht</summary>

Hieronder staat een stuk code waarbij het 'inspringen' met Tabs is weggelaten. Fix de code zodat het toch goed werkt.

```python
hour = 20   # vanavond 20:00

if hour < 6:
print("Het is nacht")
print("Ga maar lekker slapen")
elif hour < 12:
print("Het is ochtend")
print("Je moet naar school...")
if hour < 18:
print("Het is middag")
else:
print("Het is avond")
print("Einde van de dag")
```

Test uiteraard of je het goed hebt gedaan door je code uit te voeren.
</details>

---

<details>
<summary>Opdracht</summary>

Misschien was het je al opgevallen, maar in de vorige opdracht zit een foutje in de _logica_: stel de tijd maar eens in op 10 uur. Los de fout op!
</details>

---

<details>
<summary>Opdracht</summary>

In het vorige hoofdstuk heb je gekeken naar lijsten en random selecteren uit een lijst. Als we dat combineren met de `if-else` constructie, kunnen we beginnen om een spelletje te maken. In het vorige hoofdstuk keken we bijvoorbeeld naar Risk: als de aanvaller een hogere score gooit met een dobbelsteen wint de aanvaller, anders de verdediger.

Maak een code die het volgende doet:
1. Gooi een dobbelsteen voor de aanvaller.
1. Gooi een dobbelsteen voor de verdediger.
1. _Als_ de aanvaller wint, _dan_ print je "Gewonnen", _anders_ print je "Verloren".

De code voor een willekeurige keuze was als volgt:
```python
import random

dice = [...]                # vul hier zelf de dobbelsteen in
throw = random.choice(dice) # een worp is een random keuze van de dobbelsteen
```

Als bovenstaande werkt, pas dan de laatste stap aan:
1. _Als_ de aanvaller wint, _dan_ print je "Gewonnen", _anders als_ de worp van de verdediger gelijk is aan de aanvaller, _dan_ print je "Dat is pech!", _anders_ print je "Verloren".

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

> ![NOTE]
> De laatste variant hadden we nog niet besproken: je kunt een lijst maken met daarin variabelen.


## `for`-loop
Het idee van programmeren is dat je iets gaat _automatiseren_. Bijvoorbeeld: als je jarig bent stuur je je vrienden niet helemaal hetzelfde appje, maar zet je bij ieder persoon zijn of haar eigen naam in het berichtje. Maar je hebt geen zin om het appje de hele tijd opnieuw te sturen. Dat kunnen we oplossen:

```python
vrienden = ["Jan", "Piet", "Joris", "Corneel"]
for vriend in vrienden:
    print("Hoi", vriend)
    print("Je bent uitgenodigd op mijn feestje zaterdag om 17:00")
    print()     # print een lege regel (witregel)
```

> [!TIP]
> Je kunt twee dingen op dezelfde regel printen door een komma te gebruiken in `print()`, zoals je ziet bij `print("Hoi", vriend)`.

Snap je niet helemaal wat er gebeurt? Vertaal dan de twee regels die er staan en maak er een Nederlandse zin van. Als geheugensteuntje kun je `for` ook zien als `foreach` (sommige programmeertalen gebruiken dat ook in plaats van `for`). Dus: _voor elke..._.

> [!TIP]
> Je mag zelf de namen van variabelen bepalen. Je bent dus helemaal niet verplicht om `vriend` te gebruiken als naam; het mag net zo goed de naam `Hoi` of `abcd95` krijgen.*

---

<details>
<summary>Opdracht</summary>

Maak een lijst van alle vakken die je vandaag hebt. Gebruik vervolgens een `for`-loop zodat op volgorde jouw vakken geprint worden. Om je op weg te helpen:
```python
vakken = [_]

print("Je rooster vandaag is:")
for _ in _:
    print(_)
```
Vul zelf op de `_` in wat nodig is.

</details>

---

## `range()`: makkelijk een lijst maken
Het kan best veel werk zijn om een lijst van getallen te maken van bijvoorbeeld 1 t/m 100. Daarvoor is een handige `range()`-functie. Tussen de haakjes kun je een paar dingen invullen: de startwaarde en stopwaarde. Voorbeelden:


```python
range(start, stop)          # <-- vul zelf het startgetal en stopgetal in

a = range(0, 10)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = range(3, 11)            # [3, 4, 5, 6, 7, 8, 9, 10]
c = range(5, 0)             # [] (leeg, je kunt niet van 5 naar 0)
```

> [!WARNING]
> Zoals je ziet wordt het laatste getal niet meegenomen in de lijst. 

---

<details>
<summary>Opdracht</summary>

Maak een `range()` voor alle getallen op een normale dobbelsteen. Print elk getal in die range door middel van een `for`-loop om het te controleren.

> [!TIP]
> Je kunt je code heel kort houden:
> ```python
> for _ in range(_):
>     _
> ```
> Vul de `_` zelf weer in.

</details>

---

## Terug naar de schildpad
Als afsluiter van dit hoofdstuk gaan we nog even tekenen met gebruik van de nieuwe trucs. Als refresher eerst nog even een aantal commando's op een rijtje:

```python
import turtle
t = turtle.Turtle()

t.fd(_)         # tussen de haakjes uiteraard nog wel een getal invullen
t.bk(_)
t.lt(_)
t.rt(_)

t.undo()        # laatste actie ongedaan maken
t.clear()       # alle strepen verwijderen, maar de turtle laten staan
t.reset()       # helemaal opnieuw beginnen

t.circle(50)        # hele cirkel met r = 50
t.circle(-20)       # hele cirkel met r = 20, maar achteruit
t.circle(30.5, 180) # halve cirkel (180 graden) met r = 30.5

t.up()          # pen omhoog
t.down()        # pen omlaag

t.color(_)      # penkleur instellen
t.color("magenta")
```

--- 

<details>
<summary>Opdracht</summary>

Maak een vierkante spiraal door de volgende code compleet te maken:

```python
import turtle
t = turtle.Turtle()

hoek = 90
lengtes = [10, 20, 30, 40, 50, 60, 70, 80]

for _ in _:
    t.fd(_)     # ga vooruit
    t.lt(_)     # maak een bocht
```

</details>

---

Nog even een handigheidje voor de `range`-functie: je kunt instellen hoe groot je de stappen tussen de getallen wilt maken. De stapgrootte is standaard 1, maar die kan ook iets anders zijn. Zie als volgt:
```python
range(start, stop, step)    # <-- vul zelf het startgetal, stopgetal en stapgrootte in

a = range(0, 10, 1)         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = range(10, 100, 10)      # [10, 20, 30, 40, 50, 60, 70, 80, 90]
c = range(25, 55, 5)        # [25, 30, 35, 40, 45, 50]
```

--- 

<details>
<summary>Opdracht</summary>

Maak de vierkante spiraal van de vorige opdracht heel groot. Je hoeft nu alleen niet zelf een enorme lijst te typen, maar kunt gebruik maken van de `range`-functie. Wijzig de volgende regel in je script:

```python
for _ in range(_, _, _):
```

</details>

---

<details>
<summary>Opdracht</summary>

Maak de vierkante spiraal nu een (zo goed als) ronde spiraal. Je moet daarvoor de hoek heel klein maken, zodat je nauwelijks ziet dat de turtle draait. 

> [!TIP]
> Omdat je per keer maar een kleine bocht maakt, moet je ook maar een heel klein stukje vooruit. Zorg dus dat je `range`-functie niet zulke grote stappen neemt.

</details>

---