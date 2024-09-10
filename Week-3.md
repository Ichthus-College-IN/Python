# Week 3
In deze week ga je een spelletje programmeren: twee spelers gaan met behulp van de schildpad tegen elkaar een potje boter-kaas-en-eieren spelen. In deze week leer je eerst wat je nodig hebt om vervolgens het spel zelf te maken.

## `input` van de gebruiker
Om boter-kaas-en-eieren te spelen, moet je uiteraard de computer kunnen vertellen waar je een kruisje of rondje wil plaatsen. Dit doen we met de functie `input()`.

Voorbeeld:
```python
naam = input("Wat is je naam? ")
print("Hallo, ", naam, "!")
```
Wanneer je dit stukje code uitvoert, zal de computer de gebruiker om een naam vragen. Vervolgens wordt de naam getoond. 

> [!NOTE]
> Als je de code uitvoert, kun je onderin in het _uitvoerscherm_ ook iets invoeren. Klik maar eens achter het vraagteken in het uitvoerscherm: je kunt hier typen. Om de invoer compleet te maken, druk je op Enter.

---

<details>
<summary>Opdracht 3.1</summary>

Vraag de gebruiker naar zijn of haar favoriete eten en sla dit op in een variabele. Toon dit daarna op het scherm met een zin zoals "Je favoriete eten is ...".

Om je op gang te helpen:
```python
_ = input(_)
print("Je favoriete eten is", _)
```
Vul op de plek van de underscores `_` de goede dingen.

</details>

---

<details>
<summary>Opdracht 3.2</summary>

Vraag de gebruiker achtereenvolgens om twee getallen: de kolom en een rij waarin ze een vakje willen plaatsen voor boter-kaas-en-eieren.

Om je op gang te helpen:
```python
_ = input(_)
_ = input(_)
print("Je hebt gekozen voor het vakje:", _, ",", _)
```

</details>

---

## integers en strings
Wanneer je `input()` gebruikt, wordt de invoer altijd als een _string_ opgeslagen. Maar soms willen we werken met getallen (_integers_), bijvoorbeeld om een zet op het bord te plaatsen. Hiervoor gebruiken we de functies `int()` om een string om te zetten naar een getal, en `str()` om een getal om te zetten naar een string.

Een voorbeeldje:
```python
leeftijd = input("Hoe oud ben je? ")
leeftijd = int(leeftijd)  # Zet de string om naar een geheel getal
volgend_jaar = leeftijd + 1
print("Volgend jaar ben je " + str(volgend_jaar) + " jaar!")
```

> [!CAUTION]
> In de `print()` functie in het voorbeeld zie je dat de tekst nu 'aan elkaar geplakt' wordt met behulp van het `+`-teken. Op die manier wordt er géén spatie tussen de stukken tekst gezet. Dit in tegenstelling tot de volgende regel: `print("Volgend jaar ben je", str(volgend_jaar), "jaar!")`. Daar worden de spaties automatisch ingevoegd. Het ligt aan de situatie wat beter uitkomt.

---

<details>
<summary>Opdracht 3.3</summary>

Vraag de gebruiker achtereenvolgens om twee getallen: de kolom en een rij waarin ze een vakje willen plaatsen voor boter-kaas-en-eieren. Bereken de volgende _index_: `kolom * 3 + rij`. Print het resultaat hiervan. Je kunt de vorige oefenopdracht hergebruiken en aanpassen. Dit getal zal straks van pas komen.

</details>

---

## Het speelbord
In boter-kaas-en-eieren hebben we een bord met 9 vakjes. Een handige manier om het bord op te slaan is met een lijst in Python. Een lijst is een verzameling van waarden die je kunt aanpassen.
```python
bord = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print(bord)
```

Dit maakt een lege lijst voor het speelbord. Elk vakje in de lijst staat voor een plek op het bord.

Je kunt de elementen van een lijst aanpassen door naar hun positie te verwijzen:
```python
bord[0] = "X"  # Zet een X op de eerste plek
print(bord)
```

---

<details>
<summary>Opdracht 3.4</summary>

Vraag de gebruiker weer om de kolom en de rij. Bereken vervolgens de _index_ zoals in de vorige opdracht, en zet op die plek een "X": speler 1 noteert daar een kruis. Gebruik een `for`-loop, zodat speler 1 drie keer een kruisje opschrijft. Nog niet een heel eerlijk spel; dat komt zometeen.

Een idee om mee te werken:
```python
for _ in range(_, _):
    _ = input(_)
    _ = input(_)
    index = _
    bord[_] = _
    print(bord)
```

</details>

---

## Functies
Er is nog één onderdeel dat we nodig hebben: functies. We zijn al een paar ingebouwde functies tegengekomen, zoals `print(_)` en `count(_)`. Je kunt deze vergelijken met wiskunde: `y = f(x)`.

Je kunt zelf ook functies maken en gebruiken. We beginnen uiteraard met een voorbeeld:
```python
def voorstellen():
    print("Mijn naam is Tom")
    print("Ik ben 16 jaar oud")
    print("Ik woon in Veenendaal")

voorstellen()
```
> [!NOTE]
> * Een functie herken je aan het woord `def`.
> * Je kunt de functie elke naam geven die je wilt, net als een variabele.

---

<details>
<summary>Opdracht 3.5</summary>

Je komt op een uiterst traditionele kringverjaardag waar de familie van een vriend aanwezig is. Tijd voor een voorstelrondje: elke keer als iemand zich voorstelt, stel jij je voor met behulp van de functie `voorstellen`:

```python
print("Hoi, ik ben Daphne")
_
print("Hoi, ik ben Fleur")
_
print("Hoi, ik ben Daan")
_
print("Hoi, ik ben Ezra")
_
```

</details>

---

Om de groet iets persoonlijker te maken, kunnen we de functie _argumenten_ meegeven. Zie het voorbeeld:

```python
def persoonlijke_groet(ander, ik, leeftijd):
    print("Hey", ander)
    print("Mijn naam is", ik)
    print("Ik ben", leeftijd, "jaar oud")
```

Je ziet hier twee _argumenten_: `ander` en `ik`. Ook dit zijn variabelen waarvan je de naam zelf mag kiezen. Deze variabelen bestaan alleen _binnen_ de functie, dus alles 'onder' de `def` waar een inspringing/tab voor staat.

Je kunt de functie dan bijvoorbeeld als volgt gebruiken:
```python
persoonlijke_groet("Jip", "Janneke", 15)
```

---

<details>
<summary>Opdracht 3.6</summary>

Er komen nog wat opa's en oma's binnen op het feestje. Je groet ze wat persoonlijker:
```python
print("Ha, dit is oma")
_
print("Goedenavond, opa hier")
_
```

</details>

---

## Onderweg naar de slotopdracht
Tijd om een functie te bekijken voor de slotopdracht van dit hoofdstuk.

```python
def teken_bord(bord):
    print(bord[0] + " | " + bord[1] + " | " + bord[2])
    print("---------")
    print(bord[3] + " | " + bord[4] + " | " + bord[5])
    print("---------")
    print(bord[6] + " | " + bord[7] + " | " + bord[8])

bord = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
teken_bord(bord)
```

---

<details>
<summary>Opdracht 3.7</summary>

Teken het spelbord door het voorbeeld hierboven uit te voeren.  
Pas vervolgens het spelbord aan: plaats drie kruisjes op de middelste kolom (dus van boven naar beneden). Let goed op welke vakjes van het bord je daarvoor moet gebruiken! Teken het spelbord om jezelf te controleren.

</details>

---

## De slotopdracht 3
Maak boter-kaas-en-eieren!

1. Begin met een nieuw bestand, en sla deze alvast op als `slotopdracht3.py`.
1. In opdracht 3.4 heb je geoefend om een speler drie keer een zet te laten maken. Pak deze code erbij als basis, vul hem weer aan waar nodig en test het.
1. Teken het bord op de manier zoals je in opdracht 3.7 hebt geoefend, in plaats van het 'oude' `print(bord)`.
1. Voeg code toe voor een tweede speler, zodanig dat ze allebei omstebeurt een zet maken (dus in de volgorde 1-2 - 1-2 - 1-2). Zorg er uiteraard voor dat de tweede speler een ander symbool op het bord zet dan de eerste!
1. Hoe vaak moet je de `for`-loop herhalen voor het geval dat alle hokjes getekend moeten worden?

## Bonus 3-I
In dit spel kun je best een beetje cheaten: niemand verhindert je om een hokje te overschrijven als daar al iets stond van de tegenstander. Dat kun je voorkomen! Als de speler een keuze heeft gemaakt voor een rij en een kolom, moet je eerst checken of er al iets op het bord staat. Dat kan zo:
```python
bord[_] != " "  # vergelijk of er op een plek op het bord iets anders staat dan 'niks'
```

Bouw deze check in in je programma. Aangezien het best een flauwe move is als je dat probeert, moet die speler gewoon z'n beurt overslaan. Er gebeurt dan dus niets voor die speler.

## Bonus 3-II
Je moet nu zelf kijken of je gewonnen hebt. Uiteraard kun je ook de computer laten uitrekenen of er iemand gewonnen heeft. Niet zo makkelijk, maar je hebt bijna alle tools al geleerd, en je krijgt een opstapje.

Maak een nieuwe functie:
```python
def speler1_gewonnen(bord):
    if bord[_] == _ and bord[_] == _ and bord[_] == _:
        return True
    else if _:
        return True
    else:
        return False
```
Je ziet hier twee nieuwe dingen:
1. Je kunt meerdere voorwaarden combineren met het woordje `and`.
1. Een functie kan een `return`-waarde hebben. Die kun je als volgt gebruiken:
```python
if speler1_gewonnen(bord):
    print("Speler 1 heeft gewonnen")
```

Kun jij de rest uitvogelen?