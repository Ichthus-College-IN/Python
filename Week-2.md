# Week 2.1
Straks gaan we werken met data-bestanden. Je werkt namelijk meestal niet met losse getallen, letters of woorden, maar met een hele bak aan data. Denk aan meetwaarden of lappen tekst, of als je een app bouwt aan alle gebruikers of posts. Daarvoor zijn eerst nog wat andere onderdelen handig.

## Werken met tekst
We gaan aan de slag met strings: stukken tekst. Het eerste voorbeeld was `"Hello world"`. Maar er zijn ook veel langere stukken tekst. De standaard opvultekst die eigenlijk nergens op slaat is *Lorem ipsum*:
```python
lorem = """Lorem ipsum dolor sit amet. Non itaque architecto qui expedita voluptas eum natus totam. Est mollitia voluptatem aut deleniti labore hic dolore vero aut suscipit vitae aut animi officiis aut possimus nobis. Rem dignissimos repellat id internos quis et voluptatem cupiditate non rerum nulla qui tenetur quaerat et officiis molestiae.
Et dolores temporibus a voluptatum autem ut autem impedit. Eum iste assumenda in reprehenderit consequatur est minima iusto aut quod perferendis aut dolorum culpa.
Vel atque dicta est exercitationem recusandae et dolor voluptatibus. Ea alias placeat non sint molestias est amet dolores  adipisci sunt et quis veniam et voluptatibus pariatur non voluptas quia."""
```

**Let op**: tot nu toe ken je de driedubbele apostrof als commentaar. Dat is inderdaad hoe je meerdere regels commentaar kunt maken, maar je kunt het ook opslaan in een variabele!

---

<details>
<summary>Opdracht</summary>

Print `lorem`.
</details>

---

Je kunt de lengte van een string opvragen: Python telt dan hoeveel karakters (letters / spaties / cijfers / symbolen) er in je string zitten.
```python
print(len(lorem))       # lorem is 692 karakters lang
```

Er zijn een aantal handige dingen die je kunt doen met strings. Een daarvan is het splitsen op bepaalde karakters:
```python
gesplitst = lorem.split(' ')
```

De tekst wordt gesplitst op het karakter `' '`: een spatie.

---

<details>
<summary>Opdracht</summary>

Print `gesplitst`. Wat is `gesplitst` voor iets (welk *datatype* heeft het)? Maak gebruik van een `for`-loop om elk element in `gesplitst` te printen.
</details>

---

<details>
<summary>Opdracht</summary>

Splits `lorem` op het karakter `'\n'`. Print het resultaat van het splitsen en kijk goed: waarop is er gesplitst? Wat betekent `\n` dus?
</details>

---

Een ander geintje is `replace()`:
```python
vervangen = lorem.replace('o', '0') # vervang alle letters o door het cijfer 0
vervangen2 = lorem.replace(' ', '') # vervang alle spaties door niets (verwijder dus alle spaties)
```

De eerste regel laat zien hoe je losse karakters kunt vervangen. De tweede regel is eigenlijk een soort verwijderen: we vervangen de spatie door een leeg karakter. 

Tip: achter `.replace()` kun je gewoon nog een keer `.replace()` zetten om ook een ander karakter te vervangen.

---

<details>
<summary>Opdracht</summary>

Maak gebruik van de volgende tekst:
```python
tekst = "HET VAK INFORMATICA IS HET LEUKSTE VAK DAT OP HET ICHTHUS GEGEVEN WORDT (DAT IS EEN FEIT). DAT KOMT NATUURLIJK OOK DOOR DE LEERLINGEN: ZE ZIJN IJVERIG AAN HET PROGRAMMEREN EN MAKEN HET ALTIJD GEZELLIG."
```
Vervang zoveel mogelijk letters door cijfers, waarna de tekst toch nog te lezen is (gebruik minimaal de 1, 2, 3 en 4). Of je schrijft zelf een tekst die je aan je buren laat lezen nadat je letters vervangen hebt door cijfers.

</details>

---

Je kunt ook stukken tekst 'aan elkaar lijmen'. Een stukje terug werd `lorem` gesplitst op de spaties. Je kunt dat vervolgens weer op deze manier weer een normale tekst maken:
```python
gelijmd = ' '.join(gesplitst)
```

Alle elementen in `gesplitst` worden ge`join`ed met een spatie (`' '`).

---

<details>
<summary>Opdracht</summary>

Pak de tekst waarbij je gesplitst hebt op het teken `\n` (dat is een *newline*) van een enkele opdracht terug. `join` de losse zinnen met een dubbele Enter zodat het echt losse alinea's worden. (Hint: je kunt `\n\n` gebruiken om twee Enters te maken.)

</details>

---

## Verder werken met tekst

Je kunt ook tellen hoe vaak een letter voorkomt in een string:
```python
L = lorem.count('L')    # als het goed is maar 1: de hoofdletter 'L' is alleen als eerste letter aanwezig
e = lorem.count('e')    # de 'e' komt 61 keer voor
```

---

<details>
<summary>Opdracht</summary>

Kopieer de volgende tekst en sla die op in een variabele:
```python
"""In het begin schiep God de hemel en de aarde.
De aarde nu was woest en leeg, en duisternis lag over de watervloed; en de Geest van God zweefde boven het water.
En God zei: Laat er licht zijn! En er was licht.
En God zag het licht dat het goed was; en God maakte scheiding tussen het licht en de duisternis.
En God noemde het licht dag en de duisternis noemde Hij nacht. Toen was het avond geweest en het was morgen geweest.
En God zei: Laat er een gewelf zijn in het midden van het water, en laat dat scheiding maken tussen water en water!
En God maakte dat gewelf en maakte scheiding tussen het water dat onder het gewelf is, en het water dat boven het gewelf is. En het was zo.
En God noemde het gewelf hemel. Toen was het avond geweest en het was morgen geweest: de tweede dag.
En God zei: Laat het water dat onder de hemel is, in één plaats samenvloeien en laat het droge zichtbaar worden! En het was zo.
En God noemde het droge aarde en het samengevloeide water noemde Hij zeeën; en God zag dat het goed was.
En God zei: Laat de aarde groen doen opkomen, zaaddragend gewas, vruchtbomen, die naar hun soort vrucht dragen, waarin hun zaad is op de aarde! En het was zo.
En de aarde bracht groen voort, zaaddragend gewas naar zijn soort en bomen die vrucht dragen waarin hun zaad is, naar hun soort. En God zag dat het goed was.
Toen was het avond geweest en het was morgen geweest: de derde dag.
En God zei: Laten er lichten zijn aan het hemelgewelf om scheiding te maken tussen de dag en de nacht; en laten zij zijn tot tekenen, en tot aanduiding van vaste tijden en van dagen en jaren!
En laten zij tot lichten zijn aan het hemelgewelf om licht te geven op de aarde! En het was zo.
En God maakte de twee grote lichten: het grote licht om de dag te beheersen en het kleine licht om de nacht te beheersen; en ook de sterren.
En God plaatste ze aan het hemelgewelf om licht te geven op de aarde,
om de dag en de nacht te beheersen en om scheiding te maken tussen het licht en de duisternis. En God zag dat het goed was.
Toen was het avond geweest en het was morgen geweest: de vierde dag.
En God zei: Laat het water wemelen van wemelende levende wezens; en laten er vogels boven de aarde vliegen, langs het hemelgewelf!
En God schiep de grote zeedieren en alle krioelende levende wezens waarvan het water wemelt, naar hun soort, en alle gevleugelde vogels naar hun soort. En God zag dat het goed was.
En God zegende ze en zei: Wees vruchtbaar, word talrijk, en vervul het water van de zeeen; en laten de vogels talrijk worden op de aarde!
Toen was het avond geweest en het was morgen geweest: de vijfde dag.
En God zei: Laat de aarde levende wezens naar hun soort voortbrengen: vee, kruipende dieren en wilde dieren van de aarde, naar zijn soort! En het was zo.
En God maakte de wilde dieren van de aarde naar hun soort, het vee naar hun soort, en alle kruipende dieren van de aardbodem naar hun soort. En God zag dat het goed was.
En God zei: Laten Wij mensen maken naar Ons beeld, naar Onze gelijkenis; en laten zij heersen over de vissen van de zee, over de vogels in de lucht, over het vee, over heel de aarde en over al de kruipende dieren die over de aarde kruipen!
En God schiep de mens naar Zijn beeld; naar het beeld van God schiep Hij hem; mannelijk en vrouwelijk schiep Hij hen.
En God zegende hen en God zei tegen hen: Wees vruchtbaar, word talrijk, vervul de aarde en onderwerp haar, en heers over de vissen van de zee, over de vogels in de lucht en over al de dieren die over de aarde kruipen!
En God zei: Ik geef u al het zaaddragende gewas dat op heel de aarde is, en alle bomen waaraan zaaddragende boomvruchten zijn; dat zal u tot voedsel dienen.
Maar aan al de dieren van de aarde, aan alle vogels in de lucht en aan al wat over de aarde kruipt, waarin leven is, heb Ik al het groene gewas tot voedsel gegeven. En het was zo.
En God zag al wat Hij gemaakt had, en zie, het was zeer goed. Toen was het avond geweest en het was morgen geweest: de zesde dag.

Zo zijn de hemel en de aarde voltooid, en heel hun legermacht.
Toen God op de zevende dag Zijn werk, dat Hij gemaakt had, voltooid had, rustte Hij op de zevende dag van al Zijn werk, dat Hij gemaakt had.
En God zegende de zevende dag en heiligde die, want daarop rustte Hij van al Zijn werk, dat God schiep door het te maken.
Dit is wat uit de hemel en de aarde voortkwam, toen zij geschapen werden. Op de dag dat de HEERE God aarde en hemel maakte –
er was nog geen enkele veldstruik op de aarde en er was nog geen enkel veldgewas opgekomen, want de HEERE God had het niet laten regenen op de aarde; en er was geen mens om de aardbodem te bewerken,
maar een damp steeg uit de aarde op en bevochtigde heel de aardbodem –
toen vormde de HEERE God de mens uit het stof van de aardbodem en blies de levensadem in zijn neusgaten; zo werd de mens tot een levend wezen.
Ook plantte de HEERE God een hof in Eden, in het oosten, en Hij plaatste daar de mens, die Hij gevormd had.
En de HEERE God liet allerlei bomen uit de aardbodem opkomen, begerenswaardig om te zien en goed om van te eten; ook de boom des levens, in het midden van de hof, en de boom van de kennis van goed en kwaad.
Een rivier kwam voort uit Eden om de hof te bevochtigen. En vandaar splitste hij zich en vormde vier hoofdstromen.
De naam van de eerste rivier is Pison; die is het die rond heel het land van Havila stroomt, waar het goud is.
En het goud van dit land is goed; ook is er balsemhars en de edelsteen onyx.
En de naam van de tweede rivier is Gihon; die is het die rond heel het land Cusj stroomt.
En de naam van de derde rivier is Tigris; die loopt ten oosten van Assur. En de vierde rivier is de Eufraat.
De HEERE God nam de mens, en zette hem in de hof van Eden om die te bewerken en te onderhouden.
En de HEERE God gebood de mens: Van alle bomen van de hof mag u vrij eten,
maar van de boom van de kennis van goed en kwaad, daarvan mag u niet eten, want op de dag dat u daarvan eet, zult u zeker sterven.
Ook zei de HEERE God: Het is niet goed dat de mens alleen is; Ik zal een hulp voor hem maken als iemand tegenover hem.
De HEERE God vormde uit de aardbodem alle dieren van het veld en alle vogels in de lucht, en bracht die bij Adam om te zien hoe hij ze noemen zou; en zoals Adam elk levend wezen noemen zou, zo zou zijn naam zijn.
Zo gaf Adam namen aan al het vee en aan de vogels in de lucht en aan alle dieren van het veld; maar voor de mens vond hij geen hulp als iemand tegenover hem.
Toen liet de HEERE God een diepe slaap op Adam vallen, zodat hij in slaap viel; en Hij nam een van zijn ribben en sloot de plaats ervan toe met vlees.
En de HEERE God bouwde de rib die Hij uit Adam genomen had, tot een vrouw en Hij bracht haar bij Adam.
Toen zei Adam:
Deze is ditmaal	been van mijn beenderen, en vlees van mijn vlees!
Deze zal mannin genoemd worden,	want uit de man	is zij genomen.
Daarom zal een man zijn vader en zijn moeder verlaten en zich aan zijn vrouw hechten; en zij zullen tot één vlees zijn.
En zij waren beiden naakt, Adam en zijn vrouw, maar zij schaamden zich niet.

De slang nu was de listigste onder alle dieren van het veld, die de HEERE God gemaakt had; en hij zei tegen de vrouw: Is het echt zo dat God gezegd heeft: U mag niet eten van alle bomen in de hof?
En de vrouw zei tegen de slang: Van de vrucht van de bomen in de hof mogen wij eten,
maar van de vrucht van de boom die in het midden van de hof staat, heeft God gezegd: U mag daarvan niet eten en hem niet aanraken, anders sterft u.
Toen zei de slang tegen de vrouw: U zult zeker niet sterven.
Maar God weet dat, op de dag dat u daarvan eet, uw ogen geopend zullen worden en dat u als God zult zijn, goed en kwaad kennend.
En de vrouw zag dat die boom goed was om ervan te eten en dat hij een lust was voor het oog, ja, een boom die begerenswaardig was om er verstandig door te worden; en zij nam van zijn vrucht en at; en zij gaf ook wat aan haar man, die bij haar was, en hij at ervan.
Toen werden de ogen van beiden geopend en zij merkten dat zij naakt waren. Zij vlochten vijgenbladeren samen en maakten voor zichzelf schorten.
En zij hoorden de stem van de HEERE God, Die in de hof wandelde, bij de wind in de namiddag. Toen verborgen Adam en zijn vrouw zich voor het aangezicht van de HEERE God te midden van de bomen in de hof.
En de HEERE God riep Adam en zei tegen hem: Waar bent u?
En hij zei: Ik hoorde Uw stem in de hof en ik werd bevreesd, want ik ben naakt; daarom verborg ik mij.
En Hij zei: Wie heeft u verteld dat u naakt bent? Hebt u van die boom gegeten waarvan Ik u geboden had daar niet van te eten?
Toen zei Adam: De vrouw die U gaf om bij mij te zijn, die heeft mij van die boom gegeven en ik heb ervan gegeten.
En de HEERE God zei tegen de vrouw: Wat hebt u daar gedaan! En de vrouw zei: De slang heeft mij bedrogen en ik heb ervan gegeten.
Toen zei de HEERE God tegen de slang:
Omdat u dit gedaan hebt, bent u vervloekt onder al het vee en onder alle dieren van het veld!
Op uw buik zult u gaan en stof zult u eten, al de dagen van uw leven.
En Ik zal vijandschap teweegbrengen tussen u en de vrouw, en tussen uw nageslacht en haar Nageslacht;
Dat zal u de kop vermorzelen, en u zult Het de hiel vermorzelen.
Tegen de vrouw zei Hij: Ik zal uw moeite in uw zwangerschap zeer groot maken; met pijn zult u kinderen baren. 
maar uw man zal uw begeerte uitgaan, maar hij zal over u heersen.
En tegen Adam zei Hij: Omdat u geluisterd hebt naar de stem van uw vrouw en van die boom gegeten hebt waarvan Ik u geboden had: U mag daarvan niet eten,
is de aardbodem omwille van u vervloekt; met zwoegen zult u daarvan eten, al de dagen van uw leven;
dorens en distels zal hij voor u laten opkomen en u zult het gewas van het veld eten.
In het zweet van uw gezicht zult u brood eten, totdat u tot de aardbodem terugkeert, omdat u daaruit genomen bent;
want stof bent u en u zult tot stof terugkeren.
En Adam gaf zijn vrouw de naam Eva, omdat zij moeder van alle levenden is.
En de HEERE God maakte voor Adam en voor zijn vrouw kleren van huiden en kleedde hen daarmee.
Toen zei de HEERE God: Zie, de mens is geworden als een van Ons, omdat hij goed en kwaad kent. Nu dan, laat hij zijn hand niet uitsteken en ook van de boom des levens nemen en eten, zodat hij eeuwig zou leven!
Daarom zond de HEERE God hem weg uit de hof van Eden, om de aardbodem te bewerken, waaruit hij genomen was.
Hij verdreef de mens, en plaatste ten oosten van de hof van Eden de cherubs met een vlammend zwaard, dat heen en weer bewoog, om de weg naar de boom des levens te bewaken."""
```
Zoals je waarschijnlijk wel gemerkt hebt is dit Genesis 1.

Bereken de frequentie van de letter `e`. Druk die uit in een percentage: het aantal keer dat `e` voorkomt gedeeld door de totale lengte van de tekst. Zoek op internet op hoe vaak de `e` gemiddeld voorkomt in een Nederlandse tekst.

Bereken ook de frequentie als je de hoofdletter `E` meetelt samen met `e`. Komt het een beetje in de buurt?
</details>

---

<details>
<summary>Bonusopdracht</summary>

Pak de tekst van Genesis 1 er weer bij. Maak gebruik van een `for`-loop over alle letters van het alfabet, om zo de frequentie voor elke letter te berekenen. Print elke keer de letter die je bekijkt, en welk percentage er bij hoort.

Maar: let op. Bij het berekenen van het percentage gebruik je `len()`, maar `len()` rekent ook het aantal spaties en Enters mee. Dat zijn echter geen letters, dus moet je die moet je dan wel eerst verwijderen. Ter controle: als het goed is vind je daarmee een percentage van 19.4% voor de letter e/E. (Een stuk beter dus dan het percentage bij de vorige opdracht!)

Tip: als je voor een willekeurige kleine letter ook de hoofdletter wilt weten, kun je gebruik maken van dit voorbeeld:
```python
letter = 'a'    # voorbeeldletter
hoofdletter = letter.upper()    # de 'uppercase' van 'a' oftewel 'A'
```

(Dat kan ook andersom:)
```python
letter = 'B'    # voorbeeldletter
kleineletter = letter.lower()   # de 'lowercase' van 'B' oftewel 'b'
```

</details>

---

# Week 2.2
## Bestanden importeren (tekst)
Teksten zoals Genesis 1 van de vorige opdrachten zijn erg onhandig om middenin een pagina te zetten en te kopiëren/plakken in je script. Het werkt veel fijner als het in een los bestand staat dat je kunt importeren. Dat kan op de volgende manier: download het bestand 

BESTANDBESTANDBESTANDBESTAND (never gonna give you up, decrypted2.txt)

BESTANDBESTANDBESTANDBESTAND

BESTANDBESTANDBESTANDBESTAND

BESTANDBESTANDBESTANDBESTAND 

en sla het op in dezelfde map als waar je script staat opgeslagen. Gebruik vervolgens dit voorbeeld om het te importeren:
```python
file = open("voorbeeldbestand.txt")     # een bestand openen
# je kunt dan dingen doen met dit bestand
file.close()                            # het bestand sluiten
```

Om uit te lezen wat er in het bestand staat, zijn er twee voor de hand liggende opties `readline()` en `readlines()` (een subtiel verschil):
```python
regel1 = file.readline()        # lees de eerstvolgende regel (de eerste)
regel2 = file.readline()        # lees de eerstvolgende regel (de tweede dus)

alleregels = file.readlines()   # lees alle regels die nog niet gelezen zijn (derde tot en met laatste)
```

`readlines()` geeft als resultaat een lijst van alle (overige) regels in het bestand. Als je nog geen regel gelezen hebt zijn dat alle regels; als je al een paar regels hebt gelezen zoals in het voorbeeld, dan worden die regels niet meegeteld.

---

<details>
<summary>Opdracht</summary>

Importeer het voorbeeldbestand, en lees alle regels die er in staan met `readlines()`. Gebruik vervolgens een `for`-loop om elke regel los te printen. Vergeet niet het bestand te sluiten, want anders krijg je soms problemen.

Zoek vervolgens op internet een methode om het bestand regel voor regel te lezen met een `while`-loop en `readline()`.

</details>

---

Een nadeel van `readline()` en `readlines()`, is dat alles altijd als string wordt gelezen. Ook al bestaat je bestand alleen uit getallen, zal het altijd in string-vorm gelezen worden en moet je dus alles omzetten naar integer of float als je ermee wilt rekenen.

---

<details>
<summary>Opdracht</summary>

Importeer het tweede voorbeeldbestand, en lees alle regels die er in staan met `readlines()`. Gebruik vervolgens een `for`-loop om voor elke regel het kwadraat van het getal uit te rekenen. Houd uiteraard rekening met de opmerking hierboven!

</details>

---

Om te werken met grote hoeveelheden getallen zijn er betere manieren dan bestanden te lezen met `readline()`. We gaan gebruik maken van een externe *library* die goed overweg kan met getallen: `numpy` (numerical python).

## Bestanden importeren (getallen) / NumPy
In Python kun je naast gewone bestanden inlezen ook Python bestanden importeren. Zo'n *library* moet je eerst installeren, en kun je vervolgens in al je scripts gebruiken. Daarvoor moet je het volgende commando invoeren in de *terminal* onderin je scherm:
```powershell
py -m pip install numpy
```

Is dat gelukt, dan kun je NumPy importeren als volgt:

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
data = np.genfromtxt("voorbeeldgetallen_1d.txt")
```

Het resultaat van deze functie is een (soort van) lijst met alle getallen in het bestand. 

---

<details>
<summary>Opdracht</summary>

Download het voorbeeldbestand en sla deze weer op in dezelfde map als je script. Maak gebruik van `np.genfromtxt()` om het bestand uit te lezen. Print vervolgens met een `for`-loop alle getallen die in het bestand staan. Controleer natuurlijk of het resultaat klopt door het bestand te openen en te vergelijken.

Zoals je waarschijnlijk opgevallen zal zijn: `genfromtxt()` negeert de regels met een <kbd>#</kbd> ervoor, net zoals Python de tekst na <kbd>#</kbd> als commentaar beschouwt. Ideaal!

</details>

---

# Week 2.3
## Werken met NumPy

`genfromtxt` maakt niet echt een lijst zoals we tot nu toe gewend zijn. Bekijk het volgende voorbeeld maar eens:
```python
test = [1, 2, 3, 4, 5]
print(type(test))       # list
data = np.genfromtxt("voorbeeldgetallen_1d.txt")
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
data = np.genfromtxt("voorbeeldgetallen_1d.txt")
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
data = np.genfromtxt("voorbeeldgetallen_2d.txt", delimiter = ",")
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

getal2 = data[14, 2]    # regel 14, getal 2
getal2 = data[14][2]
```

Je kunt alle items in een 2d-array bijvoorbeeld op de volgende manier printen:
```python
for rij in data:        # rij is dan bijvoorbeeld [23.1, 1020.2, 45.6]
    for getal in rij:
        print(getal)
```


---

<details>
<summary>Opdracht</summary>

Print de lengte van de x-as (aantal regels) en de y-as (aantal kolommen) van de data in het 2d-voorbeeldbestand.

</details>

---

Met `data[0]` selecteer je de eerste *rij*, hebben we gezien. Om de eerste (of andere) *kolom* te selecteren kun je het volgende gebruiken:
```python
data = np.genfromtxt("voorbeeldgetallen_2d.txt", delimiter = ',')
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

## `print()` revisited
Nog een enkele tip voor het printen van meerdere dingen tegelijkertijd. Je kunt meerdere variabelen of stukken tekst aan elkaar plakken met behulp van de <kbd>+</kbd> of met een spatie ertussen door <kbd>,</kbd> te gebruiken:
```python
print("a", "b")     # resultaat: a b
print("a" + "b")    # resultaat: ab

print(3, 5)         # resultaat: 3 5
print (3 + 5)       # resultaat: 8 (want getallen worden bij elkaar opgeteld!)

i = 1
print(x[i, 0], x[i, 1], x[i, 2])    # als 'x' een 2d-array is kun je zo de eerste drie kolommen printen
```

---

<details>
<summary>Opdracht</summary>

Print de GPS coordinaten uit het bestand. GPS bestaat uit een NoorderBreedte-getal en OosterLengte-getal. Zorg ervoor dat je ze dus per tweetal print door naar bovenstaand voorbeeld te kijken.

</details>

---

<details>
<summary>Bonusopdracht</summary>

Importeer het bestand `"bonus_getallen.txt"`. Let op: dit is een flink groot bestand. Ga vervolgens de volgende stappen af:

* Zoek op internet hoe je de hele array kunt *afronden*. Dat is dus niet hetzelfde als overal een integer van maken. (Want: `int(0.9) = 0`.) Als het goed is houd je alleen -1, 0 en 1 over in de array.
* Maak van de hele array een string: `str(data)`.
* Vervang elke -1 door een Enter en verwijder de `[`, `]` en spaties.
* Print de hele string. Wat zie je?

</details>

---
