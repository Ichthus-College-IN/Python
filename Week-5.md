## Week 5.1
Het tekenen met een schildpad zit er op. Volgende halte: TKinter; we gaan een simpele 'app' bouwen!

Tkinter is ook standaard geïnstalleerd, dus kun je het direct importeren:
```python
import tkinter as tk
from tkinter import ttk
```
Die tweede regel zullen we ook nodig hebben!

We gaan dit hoofdstuk weer met gewone scripts werken in plaats van in de REPL.

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
root.attributes('-alpha', 0.7)  # de window is 70% opaque oftewel 30% doorzichtig
```

**Let op**: de laatste regel in je script moet (net als bij turtle) altijd zijn:
```python
root.mainloop()
```

---

<details>
<summary>Opdracht</summary>

Maak een window en test bovenstaande instellingen uit! Op internet zijn er trouwens nog wel meer te vinden.

</details>

---

## Tekstvelden
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


Om goed van een knop gebruik te kunnen maken gaan we eerst een functie maken.

Je kunt zoveel variabelen maken als je wilt:
```python
def press(naam):
    print(f"Je hebt de knop [ {naam} ] ingedrukt")
```
Je ziet hier een wat gekke notatie: een `f` voor de apostrofs, en vervolgens tussen accolades (`{ }`) de variabele. Dit betekent dat je de inhoud van de variabele middenin het stuk tekst wilt printen. Kost niet zoveel moeite.


We gaan de knoppen nu een actie laten uitvoeren.
```python
btn = ttk.Button(root, text = "Klik op mij", command = lambda : press("Knop 1"))
```

**Let op**: je ziet hier het vreemde stuk `lambda : ` staan dat je niet kent. Voor nu ook niet al te belangrijk, maar het is wel nodig om altijd bij het commando van een knop te zetten.

---

<details>
<summary>Opdracht</summary>

Voeg de `press()` functie in, pas je knop aan en test hem uit! Voeg je functie ook toe aan de andere knoppen die je gemaakt hebt, maar gebruik dan een andere naam dan `Knop 1`, zodat je het verschil ziet.

</details>

---


## Invoervelden
Vaak heb je gegevens of informatie van gebruikers nodig. Die kunnen ze invullen in een `Entry`: een invoerveld. Een entry heeft een bijzonder type string nodig: een `tk.StringVar()`. Die helpt erbij om de tekst van een entry uit te lezen.

Er bestaat geen officiele of officieuze afkorting voor een entry zoals dat bij een label en button is, maar we gebruiken hier `ety`. Bekijk het volgende voorbeeld voor het maken van een `StringVar` en `Entry`:
```python
tekst = tk.StringVar()
ety = ttk.Entry(root, textvariable = tekst)
ety.place(x = 0, y = 300, width = 400, height = 200)
```

---

<details>
<summary>Opdracht</summary>

Voeg het invoerveld toe aan je script en test of je invoerveld te gebruiken is. Je kunt de invoer nog niet verwerken, maar dat komt als volgende onderdeel.

</details>

---

## Items aanpassen

Je kunt van veel TKinter items (labels, buttons, entries e.d.) opvragen wat er in aanwezig is via `.cget(..)` en via een index `[..]`. Het meest nuttige is de tekst:
```python
labeltekst = lbl['text']
labeltekst = lbl.cget('text')
buttontekst = btn['text']
buttontekst = btn.cget('text')
```

Het opvragen van de invoer in een entry gaat zo:
```
entrytekst = ety.get()
```

Mocht je het fijn vinden: je kunt veel TKinter items ook aanpassen via `.configure(..)`. Je hoeft daar nu verder niets mee te doen. Een paar voorbeelden:
```python
lbl.configure(text = "Dit is nieuwe tekst")
btn.configure(text = "Knop v2")
btn.configure(command = lambda : nieuwefunctie())
btn.configure(text = "Knop v3", command = lambda : functie3())
```

---

<details>
<summary>Opdracht</summary>

Maak een functie die het volgende doet:
* Opvragen welke tekst er in de entry is ingevoerd
* De tekst in de label aanpassen naar de nieuwe tekst

De structuur ziet er dan als volgt uit (vul op de ___ zelf de benodigde dingen/namen in):
```python
def ___():
    invoer = ___
    ___.configure(text = invoer)
```
Geef vervolgens een button het commando om bovenstaande functie uit te voeren.

</details>

---

<details>
<summary>Slotopdracht ⭐⭐⭐</summary>

Maak een app die de BMI van een gebruiker kan berekenen. Daarvoor zijn de volgende dingen nodig:

* Een label met de tekst "Gewicht (kg)" en entry waar de gebruiker het gewicht kan invoeren.
* Een label met de tekst "Lengte (cm)" en entry waar de gebruiker de lengte kan invullen.
* Een button waarmee de BMI berekent wordt en een label waarin de berekende BMI weergegeven wordt.
* Een label waar na het berekenen in komt te staan of dat ondergewicht, goed gewicht of overgewicht betekent. Geef deze label eventueel afhankelijk van het type gewicht een oranje of groene achtergrondkleur, maar dat is niet verplicht.

*Tip*: de tekst uit een invoerveld is van het type `str`. Om ermee te kunnen rekenen heb je een `int` nodig, dus zorg ervoor dat je daar wat mee doet! Zie eventueel week 1.

*Tip*: zoek op internet de formule op om de BMI te berekenen.

*Tip*: als commando bij de knop gebruik je een functie. Voor die functie kun je het voorbeeld uit de bovenstaande opdracht gebruiken, behalve dat je nu _twee_ invoeren moet uitlezen en in de functie ook de BMI moet uitrekenen.

*Tip*: vergeet niet `root.mainloop()` onderaan je script te zetten.

**Beoordeling:**
* : niet ingeleverd / werkt totaal niet
* ⭐: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* ⭐⭐: ingeleverd en (zo goed als) correct op minder goede manier
* ⭐⭐⭐: ingeleverd en helemaal correct op de manier zoals geleerd in het hoofdstuk
</details>

---
