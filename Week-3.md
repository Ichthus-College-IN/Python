# Week 3.1
Na een tijd lang alleen maar dingen te printen wordt het tijd dat er ook andere dingen op het scherm tevoorschijn getoverd worden. De eerste manier waarop we dat gaan doen is het maken van grafiekjes: we hebben al heel wat voorkennis in huis om daarmee aan de slag te gaan.

Daarvoor moeten we eerst MATplotlib installeren en importeren, net zoals we dat bij NumPy doen.

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
data = np.genfromtxt("voorbeeldgetallen_2d.txt", delimiter = ',')
temperatuur = data[:, 0]
luchtdruk = data[:, 1]
vochtigheid = data[:, 2]
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
fig.show()
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

Als je nog eens kijkt naar het plaatje, zie je dat de y-as automatisch een goede schaal krijgt. De x-as is echter nog wel onhandig. Als er 20 punten in je temperatuurmeting zitten, loopt de x-as ook van 1 tot 20. Maar als je elke 6 minuten gemeten hebt, dan is het veel beter om de x-as van 0 tot 2 uur (of 120 minuten) te laten lopen.

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

Maak een array van $0$ tot $2\pi$ door `np.linspace()` te gebruiken; zorg dat er minimaal 50 elementen gebruikt worden. Plot vervolgens de volgende $x$ en $y$ tegen elkaar:

$x = 16sin(t)^3$  
$y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)$

Wat is het resultaat?

</details>

---

# Week 3.2
Het grafiekje tot nu toe is compleet kaal: we zien alleen een lijn en getallen op de x-as en y-as. Er is echter veel meer opmaak mogelijk.

## Opmaak met MATplotlib
Op een rijtje zijn hier een aantal veelvoorkomende opties voor het opmaken van een grafiek:

* `ax.set_title("titel")`: voeg een titel toe aan de grafiek.
* `ax.set_xlabel("x-label")`: voeg een titel toe aan de x-as.
* `ax.set_ylabel("y-label")`: voeg een titel toe aan de y-as.
* `ax.set_xlim(x_min, x_max)`: pas het domein van de x-as aan van `x_min` tot `x_max` (bijvoorbeeld `set_xlim(0, 10)`).
* `ax.set_ylim(y_min, y_max)`: pas het bereik van de y-as aan van `y_min` tot `y_max` (bijvoorbeeld `set_ylim(19.5, 24.8)`).
* `ax.grid()`: voeg een raster toe aan de grafiek om beter af te kunnen lezen.
* `ax.plot(x, y, label = "meting")`: voeg een label toe aan de lijn.
* `ax.legend()`: voeg een legenda toe die alle labels toont.
* `ax.set_aspect(aspect)`: stel de verhouding van de assen in (bijvoorbeeld `set_aspect(1)` betekent dat allebei de assen dezelfde verhouding hebben).

---

<details>
<summary>Opdracht</summary>

Geef alle drie de grafieken van de vorige opdracht een mooie opmaak. Gebruik minimaal aslabels, een titel, legenda en grid.

Probeer ook het domein en bereik van de assen in te stellen, net als de asverhouding (ook al maken die je grafiek niet altijd mooier).

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

Maak de drie grafieken tot nu toe op met verschillende combinaties zoals je hierboven kunt vinden. Het hoeft niet per se mooi te worden, zolang je maar een aantal dingen probeert.

</details>

---

<details>
<summary>Opdracht</summary>

Zie het volgende script:

```python
import numpy as np
import matplotlib.pyplot as plt

jaren = np.arange(1981, 2022)                         # bereik x-as
temp = np.sqrt(jaren) - 2*np.random.rand(len(jaren))  # meetpunten maken
trend = np.sqrt(jaren) - 1                            # trendlijn maken

fig, ax = plt.subplots()              # figuur maken
ax.plot(jaren, temp, 'k.')            # meetpunten plotten
ax.plot(jaren, trend, 'r-')           # trendlijn plotten
```

Maak de grafiek goed op.

</details>

---

# Week 3.3
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

---

<details>
<summary>Opdracht</summary>

Verander je plots zodat je 
* bij de temperatuur de eerste tien meetpunten niet meeneemt. Let op: je moet dan ook op de x-as (de eerste) tien punten weglaten!
* bij de luchtdruk de laatste vijf punten niet meeneemt.
* bij de luchtvochtigheid de eerste twee en de laatste twee meetpunten niet meeneemt.

</details>

---

Nog twee extra trucs wat betreft het selecteren van elementen:
```python
deel4 = start[:-3]  # selecteer alles behalve de laatste drie
deel5 = start[:int(len(start) / 3)] # selecteer alles tot een derde van de totale lengte
```

Bij de laatste truc moet je heel erg opletten: als bijvoorbeeld de totale lengte 10 is, en je selecteert tot element $\frac{10}{3}$, komt er een error, want het element 3.333 bestaat niet. Daarom moet er een `int` van gemaakt worden.

---

<details>
<summary>Slotopdracht</summary>

Maak gebruik van het bestand (komt nog online). Hierin is voor elke sensor in het Meet je leefomgeving-kastje een kolom aanwezig met alle meetwaarden gedurende twee dagen.

Maak voor elke sensor een mooi opgemaakte figuur. De x-as loopt van 0 tot 24 uur, dus dat betekent dat je voor elke figuur twee lijnen moet plotten: dag 1 en dag 2. Zorg uiteraard ook dat duidelijk is welke lijn bij welke dag hoort.

</details>

---

<details>
<summary>Bonusopdracht</summary>

Zorg dat alle grafieken niet in losse figuren staan, maar in een heel erg grote figuur door meerdere plots in één `plt.subplots()` te maken. Zoek op internet op hoe je daarmee aan de slag kunt! Regel dat de grafieken goed leesbaar zijn: groot genoeg met onderlinge ruimte, legenda's etc.

**Let op**: dit is een pittige opdracht om netjes te maken.

</details>

---
