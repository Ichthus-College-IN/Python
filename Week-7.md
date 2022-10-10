# Week 7.1
Een introductie van Python kan bijna niet zonder het volgende onderdeel. Aangezien Python erg goed is in werken met data, is het ook bijzonder goed in dit onderdeel: Machine Learning

## Introductie op Machine Learning
Machine Learning (ML) is een vorm of onderdeel van kunstmatige intelligentie. ML is wel een vrij 'domme' vorm van intelligentie: ook al lijkt het veel te kunnen, is het iets wat in de basis erg eenvoudig kan zijn (al kan het ook wel erg complex worden). We gaan kijken naar de 'Hello world' van ML in Python: de iris-bloemetjes.

In de natuur zijn drie leuke varianten van de iris-bloem:
* Iris Setosa
* Iris Versicolor
* Iris Virginica

Er is een vrij duidelijk onderscheid tussen de verschillende soorten wat betreft de volgende eigenschappen:
* Kelkblad-lengte
* Kelkblad-breedte
* Kroonblad-lengte
* Kroonblad-breedte

Vrij goed te begrijpen is de KNN-classificatie: een van de mogelijke manieren om ML toe te passen. KNN staat voor *K-nearest-neighbor*: er wordt gekeken naar de beste dichtstbijzijnde oplossing.

Een voorbeeld:  
|Kelkblad-breedte|Bloemtype|
|:--|:--|
|1|A|
|2|B|
|1|A|
|2|B|
|3|C|
|4|C|
|3|C|
|2|B|
|5|A|

Hiervan is een histogram te maken: een breedte van 1 cm komt 2 keer voor, 2 cm komt 3 keer voor, 3 cm komt 2 keer voor, 4 cm komt 1 keer voor en 5 cm komt een keer voor.

Stel dat we een bloem pakken van onbekend type. De kelkblad-breedte is 2.5 cm. Dan is de vraag: wat matcht het beste? We kunnen dan kijken naar alle mogelijke getallen in de histogram, of ons beperken tot een klein aantal *buren*. Vaak kiezen we het laatste: we beperken ons tot bijvoorbeeld 3 buren (K = 3). Deze *K-nearest-neighbors* zijn dan kelkblad-breedte 1, 2 en 3 cm (4 cm is ook een optie maar komt minder vaak voor dan 1).

Het antwoord op de vraag welk type deze bloem dan is, is: 'de meest voorkomende van de *K-nearest-neighbors*. Aangezien 2 cm het meeste voorkomt, en die van type B is, voorspellen we dat de onbekende bloem ook van type B is.

## Machine Learning in Python
In de library `scikit-learn` is een bestand aanwezig met data voor 50 bloemen van elke soort Iris. Zie de volgende link voor een visualizatie: [link](https://python-course.eu/images/machine-learning/data-representation-and-visualization-data_3.webp).


We installeren de nodige packages:
```powershell
py -m pip install scipy scikit-learn
```

En we hebben de volgende imports nodig:
```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
```

Om de gegevens van de bloemen te openen, hebben we de volgende regel nodig:
```python
iris_dataset = load_iris()
```
In deze dataset zitten van de eerdergenoemde vier categorieen alle gemeten lengtes en breedtes, en staat er genoemd welk type bloem het is.

Vervolgens gaan we alle 150 *samples* (metingen) opdelen in twee delen: trainingdata en testdata. De trainingdata wordt gebruikt om categorieen te maken zoals in het kleine voorbeeld; testdata wordt gebruikt om te kijken 'of het ergens op slaat'. Bij de tests wordt voorspeld welke bloem een meting is, en daarna gecontroleerd wat de echte soort is.

Hoe meer trainigdata, hoe beter de voorspelling, maar er moet ook wat getest worden. Zonder tests weet je namelijk niet echt of het goed gaat. Als voorbeeld gebruiken we een 50/50 verdeling:
```python
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], train_size = 0.5, random_state = 4)
```
Je hoeft niet precies te begrijpen wat hier staat, maar het is handig om te zien dat `train_size = 0.5` (50%), en `test_size` is automatisch dan de andere helft.

Vervolgens starten en trainen we het algoritme. Dat gebeurt helemaal automatisch en duurt een seconde of iets dergelijks, afhankelijk van je computer:
```python
kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train, y_train)
print("Test score: {:.2f}".format(kn.score(X_test, y_test)))
```

---

<details>
<summary>Opdracht</summary>

Kopieer alle bovenstaande onderdelen en zet ze onder elkaar. De test score geeft aan hoe goed het algoritme heeft voorspeld van welke soort een bloem is. Wat is de test-score bij een 50/50 verdeling? Experimenteer hoeveel procent `train_size` er nodig is om de overige bloemen helemaal goed te voorspellen (alles goed betekent test score = 1). Lukt dat?
</details>

---

Het doel is natuurlijk om te proberen te voorspellen van welk type een nieuwe bloem is:
```python
iris_new = np.array([[5, 2.9, 1, 0.2]]) # meting van een nieuwe bloem
prediction = kn.predict(iris_new)       # voorspelling van type bloem

print("Voorspelde soort: " + str(iris_dataset["target_names"][prediction]))   # printen welk type bloem er voorspeld wordt
```

---

<details>
<summary>Opdracht</summary>

Welk type is de onbekende bloem waarschijnlijk? Door een grotere `train_size` te gebruiken kun je meestal zekerder zijn van de voorspelling. Hoe klein moet de `train_size` zijn om op een waarschijnlijk foute voorspelling uit te komen?

</details>

---

# Week 7.2
## Machine Learning en plaatjes
Machine Learning gaat heel vaak samen met plaatjes. Denk bijvoorbeeld aan het verwerken van kentekens, of het automatisch blokkeren van gevoelige of ongepaste beelden op social media. Zonder machine learning is daar geen beginnen aan.

Het is best moeilijk om echt een betrouwbaar programma te maken, maar als je onderscheid wilt maken tussen twee heel erg verschillende categorieën gaat het al wel snel goed. Hiervoor hoef je niet zelf een programma te schrijven, maar kun je gebruik maken van een bestaand script waar je zelf mee kunt experimenteren.

Eerst moet je een paar dingen installeren:
```python
py -m pip install duckduckgo_search fastdownload fastai
```
Let op: dit kan wel een minuutje duren.

(*Tip*: als je het thuis wilt installeren moet je waarschijnlijk `python` invoeren in plaats van `py`!)

Als het installeren voltooid is, kun je het bestand `fastai_voorbeeld.py` openen en downloaden.

## Opzet
Het bestand heeft een aantal *parameters* op regel 36 t/m 41. Het meeste kun je daar aanpassen.

Het kan best veel werk kosten om zelf heel veel plaatjes te downloaden. Als eerste kun je invoeren waarop je wilt zoeken (fun fact: als zoekmachine wordt DuckDuckGo gebruikt, niet Google!). Als tweede kun je invoeren wat de naam van de map moet zijn waarin je de plaatjes wilt hebben. Als derde kun je invoeren hoeveel plaatjes je wilt downloaden per zoekterm. Het duurt wel een seconde of twee per plaatje om te downloaden, dus maak het getal niet veel groter dan 20 of 30 (al zou dat waarschijnlijk wel een beter resultaat opleveren!).

Kies je twee categorieën die erg veel op elkaar lijken (bijvoorbeeld `tiger` en `lion`), dan zal je programma natuurlijk slecht kunnen voorspellen. Het voorbeeld kiest voor `forest` en `bird`: twee dingen die niet snel op elkaar lijken.

De gedownloade bestanden kun je terugvinden in de map die aangegeven staat; zo kun je controleren of de plaatjes die gedownload zijn inderdaad kloppen.

Als vierde argument vul je de `train_size` in. Net zoals in de vorige opdracht met de bloemen geeft dit aan hoeveel procent je gebruikt om te trainen, en hoeveel om te controleren of je training klopt. Meestal is circa 80% een goed percentage, zoals je waarschijnlijk in de vorige opdracht hebt geconstateerd.

Als vijfde argument kun je invullen hoeveel `epochs` je wilt gebruiken. Een `epoch` is eigenlijk een trainingsronde. Hoe meer rondes je traint, hoe beter je resultaat meestal wordt maar hoe langer je moet wachten. Er zit nog een klein ander nadeel aan het gebruik van veel epochs. Denk bijvoorbeeld aan als je altijd zou trainen tegen dezelfde persoon: je weet precies hoe die persoon te werk gaat, maar als je tegenover een ander staat dan heb je bijna voor niets getraind omdat de tegenstander heel andere tactieken gebruikt. 

Als laatste argument geef je aan voor welk bestand je de uitkomst wilt voorspellen. In dit geval heet dat bestand `bird.jpg`, maar dat kun je zelf natuurlijk altijd aanpassen als je iets anders wilt proberen.

---

<details>
<summary>Opdracht</summary>

Installeer de benodige packages, download het voorbeeldbestand en zoek op internet naar een doorsnee plaatje van een vogel. Download dat plaatje als `bird.jpg` in dezelfde map als het voorbeeldbestand.

Voer vervolgens het voorbeeldbestand uit met de standaard ingevulde waarden. Let op: het duurt wel een minuutje voordat het script klaar is. In de terminal zie je dingen voorbij komen die aangeven dat er wel wat gebeurt, dus maak je geen zorgen zolang daar elke paar seconden wat gebeurt.

</details>

---

<details>
<summary>Opdracht</summary>

Kies in plaats van de zoektermen `forest` en `bird` voor twee andere items. Pas uiteraard ook de naam van de map aan waar ze in moeten komen. Zoek op internet een plaatje dat bij één van de twee categorieën hoort en kijk of je script goed (genoeg) kan voorspellen waar het bij hoort.

</details>

---

<details>
<summary>Opdracht</summary>

De voorspellingen kloppen lang niet altijd. We gaan dat eens bekijken: download een heel ander plaatje dan de twee categorieën die je ingevuld hebt. Voer de naam van dat bestand in bij `test_image`. Maak vervolgens van regels 44 en 45 even commentaar: je hoeft dezelfde plaatjes niet opnieuw te downloaden. Voer je script daarna uit en kijk wat er voorspeld wordt bij dit heel andere plaatje.

</details>

---

<details>
<summary>Opdracht</summary>

De grote vraag is vaak: hoeveel epochs is een goed aantal? Daarvoor zijn enorme formules opgesteld die allemaal op hun eigen manier berekenen hoe ver je van je doel af bent. Daarvoor mag je naar wiskunde; bij informatica geven we iets minder om de exacte formules en meer om het resultaat. Waarschijnlijk is je al wel opgevallen dat er dingen worden geprint bij de verschillende epochs ofwel trainingsrondes. Je kunt daarbij kijken naar de `train_loss`, `valid_loss` en `error_rate`. Deze geven alle drie weer hoe goed de training gaat. Zie bijvoorbeeld:
```
epoch     train_loss  valid_loss  error_rate  time
0         1.417494    1.177329    0.571429    00:08
epoch     train_loss  valid_loss  error_rate  time
0         0.830921    0.958205    0.285714    00:08
1         0.726589    0.823547    0.142857    00:08
2         0.496408    0.725432    0.142857    00:08
```

Hoeveel epochs is dan genoeg? Een niet-bestaande maar voor nu oké vuistregel is dat je genoeg epochs gebruikt als geen van drie kolommen bij een extra epoch meer dan ongeveer 10% zakt. In het bovenstaande voorbeeld zie je dat de derde epoch (getal 2) nog stevig gezakt is ten opzichte van de tweede epoch. Dan kan een extra ronde het nog wel waard zijn dus!

Test voor jouw programma zoals die nu ingesteld is, hoeveel epochs je zou moeten gebruiken. Je kunt altijd wat teveel epochs instellen en je script stoppen via <kbd>Ctrl</kbd>+<kbd>C</kbd> als je ziet dat er weinig winst meer behaald wordt, en dat getal vervolgens aanhouden.

</details>

---

# Week 7.3

---

<details>
<summary>Slotopdracht</summary>

In de algemene repository zijn drie plaatjes te vinden, `muse_1.jpg`, `muse_2.jpg` en `muse_3.jpg`. Deze komen uit het spel 'Muse' waarbij je als speler op basis van een woord, gebaar of geluidje van een medespeler de bijbehorende foto moet raden. De meeste plaatjes zijn nogal trippy en vreemd; deze zeker ook. De opdracht is als volgt:

* Kies één van de drie afbeeldingen om mee te werken.
* Bedenk twee of meerdere zoekopdrachten waar jouw plaatje op lijkt; bijvoorbeeld 'boat', 'crab' of 'girl' om per plaatje een idee te geven.
* Zorg ervoor dat er per categorie een aantal plaatjes gedownload worden; kies zelf hoeveel je er wilt. Je hoeft de plaatjes maar één keer te downloaden, en de regels met downloaden daarna weer commentaar maken als je tevreden bent met de gedownloade plaatjes.
* Ga experimenteren met de variabelen `num_images`, `train_size` en `epochs` om het meest betrouwbare resultaat te halen: wat staat er op jouw plaatje?
* Houd bij in comments aan het einde van je script welke resultaten je krijgt bij welke instellingen (bijvoorbeeld `# 30 plaatjes, 0.7 training, 5 epochs -> 90% boot`)

**Beoordeling**
* Je kunt 0.3 pt krijgen voor de categorieën die je uitgekozen hebt: zijn dat twee vage, of misschien meerdere goede kanshebbers?
* Je kunt 0.5 pt krijgen voor het uitzoeken van een goede waarde voor de drie genoemde variabelen. Uiteraard wordt krijg je meestal betere resultaten als je de computer een uur laat werken in plaats van een minuut, maar is dat niet de bedoeling.
* Je kunt 0.7 pt krijgen voor het bijhouden van de gebruikte instellingen voor de variabelen en de bijbehorende resultaten.

*Let op*: het gaat bij deze opdracht er niet om dat je 100% betrouwbaarheid haalt, want zoals je in een van de opdrachten hebt kunnen zien kan je resultaat best onzinnig zijn bij kleine aantallen afbeeldingen. Het gaat er met name om dat je de invloed test van de mogelijke instellingen!

</details>

---