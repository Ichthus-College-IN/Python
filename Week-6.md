# Week 6

Om te werken met grote hoeveelheden getallen gaan we kijken naar het werken met losse bestanden. We gaan ook gebruik maken van een *library* die goed overweg kan met getallen: `numpy` (numerical python).

## Bestanden importeren (getallen) / NumPy
In Python kun je naast gewone bestanden importeren ook Python bestanden importeren die je helpen. Sommige zijn voorgeïnstalleerd, zoals `turtle`, maar andere *libraries* moet je eerst installeren, en kun je vervolgens in al je scripts gebruiken. Daarvoor moet je het volgende commando invoeren in de *terminal* onderin je scherm:
```powershell
py -m pip install numpy
```

Is dat gelukt, dan kun je in je script NumPy importeren als volgt:

```python
import numpy
```

---

<details>
<summary>Opdracht</summary>

Installeer NumPy. 

Test of de installatie is gelukt door in een (leeg) script NumPy te importeren met behulp van de regel hierboven, en het script uit te voeren. Bij succes gebeurt er 'niets'; anders komt er een error in de Terminal.

</details>

---

**Let op**: het importeren van een library doe je altijd bovenaan een script, op de eerste regels. Zo is het altijd duidelijk welke libraries er nodig zijn om jouw script te draaien.

NumPy brengt allemaal extra functies met zich mee. Als je daarvan gebruik wilt maken, moet je de naam `numpy` ervoor zetten. Wil je bijvoorbeeld een sinus berekenen, kan dat als volgt:

```python
x = numpy.sin(1.57)
```

De hele tijd `numpy` typen is redelijk wat werk, dus maken we graag gebruik van een afkorting: we vervangen de regel `import numpy` door
```python
import numpy as np
```

Nu kunnen we de sinus op deze manier berekenen:
```python
x = np.sin(1.57)
```

---

<details>
<summary>Opdracht</summary>

Doe een gok of zoek op internet op hoe je de waarde van $\pi$ kunt printen. Tip: $\pi$ is een onderdeel van NumPy.

</details>

---

Rekenen met NumPy bewaren we voor straks; voor nu kijken we naar het uitlezen van bestanden met getallen. Daarvoor komt de volgende functie erg goed van pas:
```python
data = np.genfromtxt("voorbeeld_getallen_1d.txt")
```

Het resultaat van deze functie is een (soort van) lijst met alle getallen in het bestand. 

---

<details>
<summary>Opdracht</summary>

Download het voorbeeldbestand en sla deze weer op in dezelfde map als je script. Maak gebruik van `np.genfromtxt()` om het bestand uit te lezen. Print vervolgens met een `for`-loop alle getallen die in het bestand staan. Controleer natuurlijk of het resultaat klopt door het bestand te openen en te vergelijken.

Zoals je waarschijnlijk opgevallen zal zijn: `genfromtxt()` negeert de regels met een <kbd>#</kbd> ervoor, net zoals Python de tekst na <kbd>#</kbd> als commentaar beschouwt. Ideaal!

</details>

---


## Werken met NumPy

`genfromtxt` maakt niet echt een lijst zoals we tot nu toe gewend zijn. Bekijk het volgende voorbeeld maar eens:
```python
test = [1, 2, 3, 4, 5]  # 'normaal'
print(type(test))       # list
data = np.genfromtxt("voorbeeld_getallen_1d.txt")
print(type(data))       # numpy.ndarray
```

Het resultaat is een `np.ndarray`. Het komt eigenlijk neer op een `numpy`-lijst, die gemaakt is om te werken met getallen en NumPy. Je kunt van een Python lijst makkelijk een NumPy *array* (de officiele naam) maken:
```python
python_lijst = [1, 2, 3, 4, 5, 6]
numpy_array = np.array(python_lijst)
```

Uiteraard is dat hetzelfde als dit:
```python
python_lijst = range(1, 7)
numpy_array = np.array(python_lijst)
```

Maar NumPy kan dat zelf ook:
```python
numpy_array = np.arange(1, 7)
```

---

<details>
<summary>Opdracht</summary>

Maak een NumPy array van 0 tot 100 in stapjes van 5 (dus 0, 5, 10, .., 95). Controleer of je het goed gedaan hebt door de array te printen.

Maak vervolgens ook een array van 5 tot en *met* -5. Controleer ook hier natuurlijk of je het goed hebt gedaan.

</details>

---

Met NumPy-arrays kun je heel erg makkelijk rekenen. Zie het volgende voorbeeld:
```python
a = np.arange(1, 11)
k = a + a
print(k)            # array([2, 4, 6, 8, ..., 20])
```

Het eerste getal uit `a` wordt opgeteld bij het eerste getal uit `a`, het tweede getal bij het tweede getal, etc.

---

<details>
<summary>Opdracht</summary>

Maak een array `a` van 0 tot en met 5 en een array `b` van 0 tot en met 10. Tel deze bij elkaar op. Wat gebeurt er?

</details>

---

<details>
<summary>Opdracht</summary>

Maak een array `c` van 0 tot en met 10. Bereken het resultaat van $c^c$. Wat gebeurt er? Zoek op internet een oplossing op en/of vraag het aan de docent.

</details>

---

Je kunt ook in een keer bijvoorbeeld de sinus of cosinus van een heel array berekenen:
```python
data = np.genfromtxt("voorbeeld_getallen_1d.txt")
l = np.sin(data)
print(l)
```


---

<details>
<summary>Opdracht</summary>

Maak een array van 0 tot 2 $\pi$ met stapjes van 0.1. Bereken de sinus, cosinus en tangens van de array. Print uiteraard elke keer het resultaat.

</details>

---

## NumPy in twee dimensies
Het gebeurt eigenlijk nooit dat je maar een enkele kolom met gegevens hebt. Als je bijvoorbeeld de temperatuur meet, meet je vaak ook de luchtdruk, luchtvochtigheid of andere gerelateerde zaken. Je hebt dus heel vaak meer dan een kolom. 

Tussen verschillende kolommen staat een *scheidingsteken* om de kolommen uit elkaar te houden. Vaak is dat een komma (`','`), tab (`'\t'`) of spatie (`' '`). Natuurlijk niet de punt, want die wordt gebruikt voor decimalen. Bij het uitlezen van een bestand met `np.genfromtxt()` kun je ook aangeven welk scheidingsteken of *delimiter* er nodig is:
```python
data = np.genfromtxt("voorbeeld_getallen_2d.txt", delimiter = ",")
```

---

<details>
<summary>Opdracht</summary>

Importeer het tweede voorbeeldbestand zoals hierboven. Print de data. Wat valt je op?

Print vervolgens `data[0]`, `data[1]` en `data[2]` en let op wat er geprint wordt.

</details>

---

Een NumPy array kan dus ook twee-dimensionaal zijn. **Let op**: de x-as en y-as zijn tegengesteld aan wat je gewend bent.

Je kunt een los getal opvragen op de volgende twee manieren:
```python
getal1 = data[0, 0]     # regel 0, getal 0
getal1 = data[0][0]

getal2 = data[10, 2]    # regel 10, getal 2
getal2 = data[10][2]
```

Met `data[0]` selecteer je de eerste *rij*, hebben we gezien. Om de eerste (of andere) *kolom* te selecteren kun je het volgende gebruiken:
```python
data = np.genfromtxt("voorbeeld_getallen_2d.txt", delimiter = ',')
kolom0 = data[:, 0]
kolom1 = data[:, 1]
```
De <kbd>:</kbd> betekent hier dat je de *hele x-as* selecteert. 

---

<details>
<summary>Opdracht</summary>

Print nogmaals de lengte van de x-as en y-as, maar nu door gebruik te maken van bovenstaand voorbeeld.

</details>

---

<details>
<summary>Opdracht</summary>

Print de temperatuur, luchtdruk en luchtvochtigheid uit het voorbeeldbestand.

</details>

---

<details>

<summary>Bonusopdracht</summary>

Werk het volgende stappenplan af:

* Voeg bovenaan je bestand de volgende regel in: `np.set_printoptions(threshold = np.inf, linewidth = np.inf)`
* Importeer het bestand `"bonus_getallen.txt"`. Let op: dit is een vrij groot bestand.
* Zoek op internet hoe je de hele array kunt *afronden*. Dat is dus niet hetzelfde als overal een integer van maken. (Want: `int(0.9) = 0`.) Als het goed is houd je alleen 0 en 1 over in de array.
* Maak van de hele array nu een integer: zoek op internet hoe dat kan.
* Maak van de hele array een string: `str(data)`.
* Verwijder de `[` en `]`.
* Maak een bestand, schrijf de string naar het bestand, en sluit het bestand.
* Open het bestand en geniet van de creatie (tip: zoom een stuk uit)!

**Beoordeling:**
* 0.00pt: niet ingeleverd / werkt totaal niet
* 0.50pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 1.00pt: ingeleverd en (zo goed als) correct
</details>

Je kunt een bestand zelf maken vanuit Python. Een voorbeeld:
```python
file = open("test.txt", "w")    # open het bestand 'test.txt' met 'w'rite permissions
file.write("Hello world!")      # schrijf een regel in het bestand
file.write("")                  # schrijf een lege regel
file.write("Dit is\neen test")  # schrijf twee regels in één keer
file.close()                    # sluit het bestand
```
---


## Grafieken maken
Na een tijd lang alleen maar dingen te printen wordt het tijd dat er ook andere dingen op het scherm tevoorschijn getoverd worden: grafieken. Daarvoor moeten we eerst MATplotlib installeren en importeren, net zoals we dat bij NumPy doen.

In de terminal:
```powershell
py -m pip install matplotlib
```

En bovenaan in het script:
```python
import matplotlib.pyplot as plt
```

We gebruiken specifiek de `pyplot` package uit MATplotlib, maar daar hoef je verder geen aandacht aan te besteden. De gebruikelijke afkorting is `plt`.

---

<details>
<summary>Opdracht</summary>

Installeer MATplotlib via de terminal en test of de installatie geslaagd is door de `import` regel in een script te zetten en uit te voeren.

</details>

---

## Grafiekjes maken met MATplotlib
Het vorige hoofdstuk is geeindigd met een 2d-array met temperatuur, luchtdruk en luchtvochtigheid. Het mooiste is natuurlijk om dat in grafiekvorm te zetten.

We beginnen met het importeren van de data:
```python
data = np.genfromtxt("voorbeeld_getallen_2d.txt", delimiter = ',')
temperatuur = data[:, 0]
vochtigheid = data[:, 1]
luchtdruk = data[:, 2]
```

Vervolgens maken we een kaal figuur aan:
```python
fig, ax = plt.subplots()
```

`plt.subplots()` is een functie die twee dingen maakt: een heel plaatje en een grafiek in het plaatje. Het gehele plaatje slaan we op in de variabele `fig`, en de grafiek in de variabele `ax`.

In de grafiek `ax` kunnen we een lijn gaan *plotten*. De simpelste vorm is zo:
```python
ax.plot(temperatuur)
```

De temperatuur is nu een lijn in de grafiek `ax` in het plaatje `fig`. Om het plaatje te bekijken, is het volgende nodig:
```python
plt.show(block = True)
```

---

<details>
<summary>Opdracht</summary>

Maak een grafiek van de temperatuur, door alle bovenstaande stappen te combineren. Kopieer en plak alle benodigdheden om ook een tweede en derde grafiek te maken van de luchtdruk en luchtvochtigheid.

</details>

---

<details>
<summary>Opdracht</summary>

In plaats van drie losse figuren te maken kun je ze ook combineren in één *plot*. Maak dit keer maar een figuur en gebruik drie keer `ax.plot()` om alle drie de lijnen bij elkaar te stoppen. Uiteraard ziet dit er wel minder handig uit.

</details>

---

Als je nog eens kijkt naar het plaatje, zie je dat de y-as automatisch een goede schaal krijgt. De x-as is echter nog wel onhandig. Als er 20 punten in je temperatuurmeting zitten, loopt de x-as van 0 tot 20. Maar als je elke 6 minuten gemeten hebt, dan is het veel beter om de x-as van 0 tot 2 uur (of 120 minuten) te laten lopen.

## Nog een klein beetje NumPy
Eerder hebben we al gekeken naar `np.arange(start, stop, step)`. Als je een x-as wilt maken van 0 tot en met 2 met 20 punten (want je hebt 20 metingwaarden), dan is dat best moeilijk te maken. Want hoe groot zijn de stappen? Een makkelijkere optie is de volgende:
```python
t1 = np.linspace(start = 0, stop = 2, num = 20)  # 20 getallen verdeeld tussen 0 en 2 uur
t2 = np.linspace(0, 120, 20) # 20 getallen verdeeld tussen 0 en 120 minuten
```

Het derde *argument* tussen de haakjes `num` is het aantal getallen dat je wilt tussen `start` en `stop`.

Je mag de woorden `start`, `stop` en `num` gebruiken, maar ze ook weglaten zoals in het voorbeeld voor `t2`.

Het kan echter zijn dat je een tweede meting doet met opeens 30 meetwaarden. Je moet dan handmatig de `num = 20` veranderen naar `num = 30`. Dat kan beter:
```python
t3 = np.linspace(0, 2, len(temperatuur))
```

Het aantal elementen in `t3` is dan automatisch evenveel als het aantal elementen in de meting!

Hoe plotten we dit vervolgens?
```python
ax.plot(t3, temperatuur)    # eerst de waarden voor de x-as, dan de y-as
```

---

<details>
<summary>Opdracht</summary>

Maak een grafiek van de temperatuur, waarbij je de x-as van 12 tot 18 uur laat lopen. Gebruik precies evenveel punten als er metingen zijn, op de manier zoals hierboven voor `t3` beschreven is.

</details>

---

<details>
<summary>Opdracht</summary>

Maak een array met de naam `t` die loopt van $0$ tot $2\pi$ door `np.linspace()` te gebruiken; zorg dat er 50 elementen gebruikt worden. Maak vervolgens de volgende `x` en `y`:

$x = 16sin(t)^3$  
$y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)$

Plot ze vervolgens (op parametrische manier):
```python
ax.plot(x, y)
```
Wat is het resultaat?

</details>

---


## Opmaak met MATplotlib
Het grafiekje tot nu toe is compleet kaal: we zien alleen een lijn en getallen op de x-as en y-as. Er is echter veel meer opmaak mogelijk.
Op een rijtje zijn hier een aantal veelvoorkomende opties voor het opmaken van een grafiek:

* `ax.set_title("titel")`: voeg een titel toe aan de grafiek.
* `ax.set_xlabel("x-label")`: voeg een titel toe aan de x-as.
* `ax.set_ylabel("y-label")`: voeg een titel toe aan de y-as.
* `ax.set_xlim(x_min, x_max)`: pas het domein van de x-as aan van `x_min` tot `x_max` (bijvoorbeeld `set_xlim(0, 10)`).
* `ax.set_ylim(y_min, y_max)`: pas het bereik van de y-as aan van `y_min` tot `y_max` (bijvoorbeeld `set_ylim(19.5, 24.8)`).
* `ax.grid()`: voeg een raster toe aan de grafiek om beter af te kunnen lezen.
* `ax.plot(x, y, label = "meting")`: voeg een label toe aan de lijn.
* `ax.legend()`: voeg een legenda toe die alle labels toont (let op: *eerst* iets plotten mét een label, anders is de legenda leeg!).

---

<details>
<summary>Opdracht</summary>

Geef een van de drie de grafieken van de vorige opdracht een mooie opmaak. Gebruik minimaal aslabels, een titel, legenda en grid.

Probeer ook het domein en bereik van de assen van één grafiek in te stellen.

**Let op**: voeg deze opmaak toe vóór de regel `plt.show(block = True)`. Want zodra je grafiekje zichtbaar wordt kun je de opmaak er niet meer van aanpassen.

</details>

---

Daarnaast kun je ook de punten of lijnen in je grafiek opmaken:
* je kunt de kleur kiezen door tijdens het plotten een letter in te vullen; als je dat niet doet maakt MATplotlib automatisch een ander kleurtje. 
* je kunt de stijl kiezen door een of twee tekens toe te voegen; als je dat niet doet maakt MATplotlib automatisch een lijn tussen de punten.

De standaardkleuren zijn:
```python
# b: blauw         # m: magenta      # c: cyaan
# g: groen         # y: geel         # w: wit
# r: rood          # k: zwart
```

De standaardstijlen zijn:
```python
#--: gestreepte lijn                # .: punten
# o: stippen                        # -:  lijn
#-.: afwisselend lijn/punt
```

Deze stijlen zijn op de volgende manier te gebruiken:
```python
ax.plot(x, y, 'r.')     # rode punten
ax.plot(x, y, 'go')     # groene stippen
ax.plot(x, y, 'w--')    # witte gestreepte lijn
```

---

<details>
<summary>Opdracht</summary>

Maak één de drie grafieken van de vorige opdrachten op met verschillende combinaties zoals je hierboven kunt vinden. Het hoeft niet per se mooi te worden, zolang je maar een aantal dingen probeert.

</details>

---

<details>
<summary>Opdracht</summary>

Zie het volgende script:

```python
import numpy as np
import matplotlib.pyplot as plt

jaren = np.arange(1981, 2022)                         # bereik x-as in jaren
temp = np.sqrt(jaren) - 2*np.random.rand(len(jaren))  # temperatuur meetpunten maken
trend = np.sqrt(jaren) - 1                            # trendlijn maken

fig, ax = plt.subplots()              # figuur maken
ax.plot(jaren, temp, 'k.')            # temperatuur plotten
ax.plot(jaren, trend, 'r-')           # trendlijn plotten
plt.show(block = True)
```

Maak de grafiek goed op.

</details>

---

## Arrays (en lijsten) revisited
Zometeen gaan we naar een databestand waarin twee volledige dagen aan metingen zitten. Het doel wordt om beide dagen te plotten in een grafiek van 0 tot 24 uur, maar dan moeten we wel de data kunnen splitsen in dag 1 en dag 2. Daarvoor kijken we weer kort naar arrays (en het werkt hetzelfde voor een gewone Python lijst).

Het selecteren van een deel van een array kan als volgt:
```python
start = np.arange(3, 13, step = 1)  # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
deel1 = start[2:]                   # [5, 6, 7, 8, 9, 10, 11, 12]
deel2 = start[:4]                   # [3, 4, 5, 6]
deel3 = start[3:6]                  # [6, 7, 8]
```

De dubbele punt geeft aan dat het om 'alle elementen tot', 'alle elementen vanaf', of 'alle elementen van .. tot ..' gaat. `deel1` selecteert alle elementen vanaf het derde (dat is dus vanaf index 2); `deel2` selecteert alle elementen *tot* de vijfde (dat is dus tot index 4); `deel3` selecteert alle elementen vanaf de vierde tot de zevende (dus van index 3 tot 6).

---

<details>
<summary>Opdracht</summary>

Maak een variabele waarin je je eigen voornaam en achternaam als string opslaat (bijvoorbeeld `naam = "Mark Rutte"`).

Print los je voornaam en je achternaam door bovenstaande methode te gebruiken.

</details>

Nog twee extra trucs wat betreft het selecteren van elementen:
```python
deel4 = start[:-3]          # selecteer alles behalve de laatste drie
kwart = int(len(start) / 4) # bereken de lengte van een kwart (als integer)
eerstekwart = start[:kwart] # selecteer alles tot een kwart van de totale lengte
```

Bij de laatste truc moet je heel erg opletten: als bijvoorbeeld de totale lengte 18 is, en je selecteert tot element $\frac{18}{4}$, komt er een error, want het element 4.5 bestaat niet. Daarom moet er een `int` van gemaakt worden.

---

<details>
<summary>Slotopdracht</summary>

Maak gebruik van het bestand `mjlo-15_0.txt`. Hierin is voor elke sensor in een Meet je leefomgeving-kastje een kolom aanwezig met alle meetwaarden gedurende twee dagen.

Maak voor elke sensor een mooi opgemaakte figuur. De x-as loopt van 0 tot 24 uur, dus dat betekent dat je voor elke figuur twee lijnen moet plotten: dag 1 en dag 2. Zorg uiteraard ook dat duidelijk is welke lijn bij welke dag hoort.

**Beoordeling:**
* 0.0pt: niet ingeleverd / werkt totaal niet
* 0.5pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 1.0pt: ingeleverd en (zo goed als) correct op minder goede manier
* 1.55pt: ingeleverd en helemaal correct op de manier zoals geleerd in het hoofdstuk
</details>

---

<details>
<summary>Bonusopdracht</summary>

Zorg dat alle grafieken niet in losse figuren staan, maar in een heel erg grote figuur door meerdere plots in één `plt.subplots()` te maken. Zoek op internet op hoe je daarmee aan de slag kunt! Regel dat de grafieken goed leesbaar zijn: groot genoeg met onderlinge ruimte, legenda's etc.

**Let op**: dit is een pittige opdracht om netjes te maken.

**Beoordeling:**
* 0.0pt: niet ingeleverd / werkt totaal niet
* 0.5pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 1.0pt: ingeleverd en (zo goed als) correct
</details>

---
