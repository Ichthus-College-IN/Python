## Week 5.1
Het tekenen met een schildpad zit er voor nu op. Volgende halte: TKinter; we gaan een simpele 'app' bouwen!

Installatie:
```powershell
py -m pip install tkinter
```

Importeren:
```python
import tkinter as tk
from tkinter import ttk
```
Die tweede regel zullen we ook nodig hebben!

### Een window maken
We starten met een kale *window*; praktisch een soort canvas waar allemaal dingen op geplaatst kunnen worden.
```python
root = tk.Tk()
```

Deze `root` (de wortel van de boom waar alles van afhangt), heeft een aantal handige of grappige instellingen. Hieronder een aantal als voorbeeld:
```python
root.title("Test")          # de titel in de bovenbalk
root.geometry("800x600")    # de breedte en hoogte van de window in pixels
root.resizable(0, 0)        # de breedte en hoogte zijn nu niet schaalbaar
root.resizable(1, 0)        # alleen de breedte is schaalbaar
root.attributes('-alpha', 0.7)  # de window is 30% doorzichtig
```

---

<details>
<summary>Opdracht</summary>

Maak een window en test een aantal instellingen uit! Zoek eventueel op internet naar andere opties.

</details>

---

### Tekstvelden
Om tekst te plaatsen op de window hebben we een *label* nodig. Een label wordt eigenlijk altijd afgekort tot `lbl`. Zie het voorbeeld:
```python
lbl = ttk.Label(root, text = "Lang leve informatica!")
```

**Let op**: we maken gebruik van `ttk.Label`. Er is ook een `tk.Label`, maar dat is een oudere versie die minder opties heeft.

In de label zetten we als eerste neer dat de label op de `root` moet komen. Als tweede specificeren we de tekst die in de label moet komen staan.

Om de label nu te zien, moeten we hem nog plaatsen:
```python
lbl.place(x = 0, y = 0, width = 400, height = 200)
```

`x` en `y` zijn de positie in de window. Daarbij is het punt (0, 0) helemaal *linksboven*: de y-as loopt van boven naar beneden toe (de x-as loopt wel gewoon van links naar rechts). De `width` en `height` zijn het aantal pixels dat de label hoog en breed is. Als die te klein is, valt de tekst er deels af.

---

<details>
<summary>Opdracht</summary>

Plaats een label op je window! Of eventueel twee of meer (maar geef ze dan wel een extra nummer zoals `lbl2` en `lbl3`).

</details>

---

Mocht je een label weer willen verwijderen van je window, kan dat zo:
```python
lbl.place_forget()
```

Je label blijft nog wel 'onzichtbaar' bestaan: je kunt hem gewoon direct weer plaatsen met `lbl.place()` zonder dat je opnieuw dat label moet maken.

### Knoppen
Uiteraard is een app zonder knoppen vrij waardeloos. Tijd voor een *button*, eigenlijk altijd afgekort tot `btn`.
```python
btn = ttk.Button(root, text = "Klik op mij")
```

Zoals het er nu staat, is een button nog niet veel anders dan een label: behalve dat de `root` is aangegeven, is er alleen een tekst. Maar: het ziet er al wel uit als een knop!

---

<details>
<summary>Opdracht</summary>

Plaats een button op je window! Of eventueel twee of meer (maar geef ze dan wel een extra nummer zoals `btn2` en `btn3`).

</details>

---

Om goed van een knop gebruik te kunnen maken gaan we eerst iets anders bekijken.

## Week 5.2

### Functies
Een functie is een stuk code dat je via een naam kunt activeren of aanroepen. Als je het niet aanroept wordt het dus niet uitgevoerd, maar als je het meerdere keren achter elkaar aanroept wordt het meerdere keren uitgevoerd.

Een erg simpel voorbeeld:
```python
def voorbeeldfunctie():
    print("De voorbeeldfunctie zegt hallo")
```

Een functie start je met het woord `def` en vervolgens de naam van de functie. Je kunt dat hetzelfde beschouwen als een variabele-naam: je kunt zelf gewoon een naam kiezen. De haakjes openen en sluiten `()` zijn ook verplicht, en worden straks nuttig. De dubbele punt werkt hetzelfde als bij een `if`, `for` etc. Alle regels die bij de functie horen, krijgen een Tab.

Vervolgens kun je de functie uitvoeren op de volgende manier:
```python
voorbeeldfunctie()
```

---

<details>
<summary>Opdracht</summary>

Test het volgende script:
```python
def voorbeeldfunctie():
    print("De voorbeeldfunctie zegt hallo")

print("Hoi")
voorbeeldfunctie()
```

Pas het script (maar niet de voorbeeldfunctie) vervolgens zo aan dat je in de console het volgende te zien krijgt:
```powershell
>>> De voorbeeldfunctie zegt hallo
>>> Hoi
>>> De voorbeeldfunctie zegt hallo
>>> De voorbeeldfunctie zegt hallo
>>> Hoi
```

</details>

---

Je kunt functies ook een stuk nuttiger gebruiken door met variabelen te werken. Zie het volgende voorbeeld:
```python
def printfunctie(tekst):
    print(tekst)

printfunctie("Dit is een test")
```

De functie wordt aangeroepen met een stuk tekst tussen de haakjes. Die tekst wordt doorgegeven aan de functie, en opgeslagen onder de naam `tekst`. Vervolgens wordt die `tekst` geprint.

---

<details>
<summary>Opdracht</summary>

Gebruik de printfunctie om het volgende resultaat te produceren:
```powershell
>>> Test 1
>>> Test 2
>>> Test 3
>>> Nog een laatste test
```

</details>

---

Je kunt zoveel variabelen maken als je wilt:
```python
def printuitgebreid(var1, var2, var3):
    print(var1, var2, var3)
    print(var1 + var2 + var3)
```

`var#` is hier een eenvoudige afkorting voor variabele 1, 2 en 3.

---

<details>
<summary>Opdracht</summary>

Test de uitgebreide printfunctie met de volgende regels:
```python
printuitgebreid(1, 2, 3)
printuitgebreid(0.5, 0.5, 3.1)
printuitgebreid("Dit", "is een", "test")
printuitgebreid("Dit ", "is een", " test")
printuitgebreid("Dit", "is", "een", "test")
```
Waarom werkt de laatste functie niet?

</details>

---

Normaal gesproken komen de variabelen gewoon op volgorde binnen, zoals je in de vorige opdracht hebt gezien. Maar je kunt ook specifiek een andere volgorde opgeven:
```python
printuitgebreid(var3 = 7, var1 = 5, var2 = 6)
```

**Let op**: de namen van de variabelen moeten matchen met de namen in de functie.

---

<details>
<summary>Opdracht</summary>

Test de uitgebreide printfunctie met de volgende regels:
```python
printuitgebreid(var1 = 1, var2 = 2, var3 = 3)
printuitgebreid(var3 = 3, var1 = 1, var2 = 2)
printuitgebreid(var2 = 2, var3 = 3, var1 = 1)
printuitgebreid(var2 = "Dit ", var3 = "is ", var1 = "een test ")
```
Bekijk het resultaat. Van wie zou de laatste regel afkomstig kunnen zijn? ;)

</details>

---

Soms weet je niet hoeveel variabelen je kunt verwachten. Dan kun je gebruik maken van het volgende trucje:
```python
def printeindeloos(*args):
    som = 0
    for arg in args:
        print(arg)
        som = som + arg
    print("Eindresultaat: " + str(som))
```
`*args` kan een willekeurig aantal *argumenten* of variabelen zijn: alles van nul tot en met praktisch oneindig. Vervolgens wordt in dit voorbeeld een `for`-loop gebruikt om al die argumenten te printen en bij elkaar op te tellen, en het eindresultaat wordt geprint.

---

<details>
<summary>Opdracht</summary>

Test `printeindeloos` met de volgende regels:
```python
printeindeloos(1, 2, 3)
printeindeloos(0.5, 0.5, 3.1)
printeindeloos(1, 2, 3, 4, 5, 6, 7, 8, 9)
printeindeloos(2/10, 3 + 5, 4 - 8, -1, 3**2)
printeindeloos("Dit ", "is ", "een ", "test")
```

Waarom werkt de laatste regel niet? Verander de functie zodanig dat die wel werkt! Maar: dan werken de anderen helaas weer niet. Gebruik eventueel internet.

Je mag als uitdaging op internet een methode opzoeken waarmee je zowel getallen als tekst kunt opgeven als argumenten (een mix hoeft niet). Het is niet verplicht.
</details>

---

## Week 5.3
### Buttons revisited
We kijken nu opnieuw naar knoppen: we kunnen ze nu een actie laten uitvoeren.
```python
btn = ttk.Button(root, text = "Klik op mij", command = lambda : printfunctie())
```

**Let op**: je ziet hier het vreemde woord `lambda` staan dat je niet kent en ook niet altijd bij voorbeelden op internet ziet staan. Het is echter om bepaalde redenen wel erg handig om te gebruiken! Je hoeft niet te weten wat het doet, maar je mag er altijd naar zoeken of om vragen.

---

<details>
<summary>Opdracht</summary>

Zorg dat je een printfunctie in je script hebt, plaats de knop met `btn.place()` en test de knop!.

</details>

---

### Invoervelden
Vaak heb je gegevens of informatie van gebruikers nodig. Die kunnen ze invullen in een `Entry`: een invoerveld. Er bestaat geen officiele of officieuze afkorting voor een entry zoals dat bij een label en button is, maar we gebruiken hier `ety`. Bekijk het volgende voorbeeld:
```python
ety = ttk.Entry(root)
ety.place(x = 0, y = 300, width = 400, height = 200)
```

---

<details>
<summary>Opdracht</summary>

Voeg het invoerveld toe aan je script en test het. Je kunt de invoer nog niet verwerken, maar dat komt als volgende onderdeel.

</details>

---

### Items aanpassen

Je kunt van alle TKinter items (labels, buttons, entries e.d.) opvragen wat er in aanwezig is via `.cget(..)` en via een index `[..]`. Het meest nuttige is de tekst:
```python
labeltekst = lbl['text']
labeltekst = lbl.cget('text')
entrytekst = ety['text']
entrytekst = ety.cget('text')
```

Je kunt alle TKinter items ook aanpassen via `.configure(..)`. Een paar voorbeelden:
```python
lbl.configure(text = "Dit is nieuwe tekst")
btn.configure(text = "Knop v2")
btn.configure(command = lambda : nieuwefunctie())
btn.configure(text = "Knop v3", command = lambda : functie3())
ety.configure(text = "Voor- en achternaam invullen")
```

Beide manieren geven exact hetzelfde resultaat.

---

<details>
<summary>Opdracht</summary>

Maak een functie die het volgende doet:
* Opvragen welke tekst er in de entry is ingevoerd
* De tekst in de label aanpassen naar de nieuwe tekst

Geef vervolgens een button het commando om bovenstaande functie uit te voeren.

</details>

---

<details>
<summary>Slotopdracht</summary>

Maak een app die de BMI van een gebruiker kan berekenen. Daarvoor zijn de volgende dingen nodig:

* Een label met de tekst "Gewicht (kg)" en entry waar de gebruiker het gewicht kan invoeren.
* Een label met de tekst "Lengte (cm)" en entry waar de gebruiker de lengte kan invullen.
* Een button waarmee de BMI berekent wordt en label waarin de berekende BMI weergegeven wordt.
* Een label waar na het berekenen in komt te staan of dat ondergewicht, goed gewicht of overgewicht betekent. Geef deze label eventueel afhankelijk van het type gewicht een oranje of groene achtergrondkleur.

**Beoordeling:**
* 0.00pt: niet ingeleverd / werkt totaal niet
* 0.5pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 1.0pt: ingeleverd en (zo goed als) correct op minder goede manier
* 1.5pt: ingeleverd en helemaal correct op de manier zoals geleerd in het hoofdstuk
</details>

---
