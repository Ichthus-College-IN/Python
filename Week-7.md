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
iris_dataset=load_iris()[:,:75]
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