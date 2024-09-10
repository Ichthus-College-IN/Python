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
<summary>Opdracht</summary>

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
<summary>Opdracht</summary>

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
<summary>Opdracht</summary>

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
<summary>Opdracht</summary>

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
> * Je kunt de functie elke naam geven die je wilt, net als een variabele. Let wel op dat je hem niet de naam geeft van een ingebouwde functie als `len`: dan snapt Python het niet meer.

---

<details>
<summary>Opdracht</summary>

Maak een functie met de naam `keer4`. Deze functie krijgt één _argument_ met de naam `getal`, en doet het volgende: hij print het getal keer 4.

Test je functie met de volgende regels:
```python
keer4(3)        # dit moet 12 printen
keer4(10)       # dit moet 40 printen
keer4("Hoi")    # wat print dit?
```

</details>

---

Een functie kan ook meer dan één argument krijgen:
```python
def hele_naam(voor, achter):
    print("Jouw naam is:")
    print(voor + achter)
```

---

<details>
<summary>Opdracht</summary>

Maak een functie met de naam `vermenigvuldig`. Deze functie krijgt twee argumenten: `a` en `b`.Hij moet het volgende doen: hij print _a×b_.

Test je functie met de volgende regels:
```python
vermenigvuldig(3, 2)            # dit moet 6 printen
vermenigvuldig(10, 10)          # dit moet 100 printen
vermenigvuldig("Hallo", 3)      # wat print dit?
vermenigvuldig("Hallo", "Hoi")  # wat print dit?
```

</details>

---