# Week 2
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

**Beoordeling:**
* 0.00pt: niet ingeleverd / werkt totaal niet
* 0.25pt: ingeleverd maar geen correct resultaat / simpele oplossing om werkend te krijgen
* 0.50pt: ingeleverd en (zo goed als) correct
</details>

---

## Functies
Er is nog één ingebouwd onderdeel van Python dat echt nuttig is om te bekijken: functies. We zijn al een paar ingebouwde functies tegengekomen, zoals `len()`: je zet tussen de haakjes wat je wilt 'meten', en krijgt als resultaat het aantal items in de lijst of string terug.

Je kunt zelf ook functies maken en gebruiken. We beginnen uiteraard met een voorbeeld:
```python
print("Wij zijn het Ichthus!")

def chant(text):
    print(text + text + text)

chant("Ichthus!")
```
Je ziet nieuwe dingen:
* Een functie herken je aan het woord `def`.
* Je kunt de functie elke naam geven die je wilt, net als een variabele. Let wel op dat je hem niet de naam geeft van een ingebouwde functie als `len`: dan snapt Python het niet meer.
* Tussen de haakjes achter de functienaam kun je zetten welke _argumenten_ je wilt ontvangen. Ook deze kun je elke naam geven die je wilt. Je mag zoveel argumenten invoeren als je wilt (nul, één, drieduizend), maar als je de functie _aanroept_, moet je wel alle argumenten meegeven die de functie verwacht.
* Als laatste roepen we de functie aan, met als argument `"Ichthus!"`. Dit komt bij de functie binnen onder de naam `text`: die print vervolgens drie keer aan elkaar je tekst.

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

## Letters als getal(?)
De computer kent eigenlijk helemaal geen letters - alleen getallen. Elke letter is dus stiekem ook een getal. Er is een tabel die aangeeft welk getal voor welk karakter staat: ook wel de ASCII-tabel. (ASCII staat voor _American Standard Code for Information Interchange_.)

In Python kunnen we ook 'rekenen' met letters, door het bijbehorende getal te bekijken.

```python
ord('a')        # de 'ordinaal' van de letter 'a'
print(ord('2')) # de cijferwaarde van het karakter '1' is 49
```

---

<details>
<summary>Opdracht</summary>

Wat is de waarde van de letters 'X', 'Y' en 'Z' (hoofdletters)? En die van de 'a' en 'b'?

</details>

---

Je ziet dat er tussen de hoofdletters en de kleine letters nog wat andere karakters zitten. Laten we eens bekijken welke dat zijn: met de functie `chr()` (_character_). `chr()` is het 'omgekeerde' van `ord()`: je gebruikt `chr()` om van een getal het bijbehorende karakter te maken.

```python
print(chr(91))      # het omgekeerde van ord()
```

---

<details>
<summary>Opdracht</summary>

Welke andere karakters zitten er tussen de 'Z' en de 'a'?

</details>

---

## Letters (de)coderen / het Caesar schrift
In de oudheid werden teksten som op een simpele maar tijdrovende manier gecodeerd: als je een tekst wilde versleutelen, schoof je alle letters een aantal plekken op; als je een verschuiving van 2 gebruikt, wordt de 'a' een 'c', de 'b' wordt een 'd' enzovoorts. De 'z' wordt dan een 'b': het alfabet gaat rond. Dit wordt ook wel _Caesar_-versleuteling genoemd.

---

<details>
<summary>Opdracht</summary>

Maak een functie `letter_schuiven`. Deze functie gebruikt twee argumenten: `letter` en `verschuiving`. De functie doet het volgende: hij print de letter, maar dan het aantal posities verschoven dat je invult.

Je moet daarvoor de volgende dingen doen:
* De 'ordinaal' berekenen van de ingevulde letter (welk getal erbij hoort).
* Berekenen wat het nieuwe getal wordt.
* Het karakter printen dat bij het nieuwe getal hoort.

Test je functie met de volgende regels (bedenk zelf wat je zou moeten zien als resultaat):
```python
letter_schuiven('a', 2)
letter_schuiven('F', 4)
letter_schuiven('d', -3)
letter_schuiven('x', 5)     # wat is hiervan het resultaat?
```
</details>

---

## De modulus
Als je functie goed werkt en je hebt de laatste test uit de opdracht uitgevoerd, dan zie je een probleem: je moet na de 'z' terug naar de 'a', en van de 'a' terug naar de 'z' als je achteruit gaat.

We weten ondertussen dat `ord('a') = 97`, en `ord('z') = 122`. Op een of andere manier moeten we er dan voor zorgen dat je van 123 weer naar 97 gaat. We kunnen daarvoor gebruik maken van de _operator_ `%`, ookwel _mod_ (van modulus). De modulus deelt de twee getallen die je aangeeft, en geeft terug wat de 'rest' is. Een paar voorbeelden:
```python
3 % 2   #  3/2 = 1 rest 1   => 1
5 % 2   #  5/2 = 2 rest 1   => 1
11 % 4  # 11/4 = 2 rest 3   => 3
8 % 26  # 8/26 = 0 rest 8   => 8
```

---

<details>
<summary>Opdracht</summary>

Maak een variabele `begin = ord('a')`: dit is de waarde van de eerste letter 'a', ofwel 97. Maak ook een variabele `letter = 'd'`, en `totaal = 26`. Bereken het volgende: de hoeveelste letter in het alfabet is `letter`?

Tip: gebruik een formule die eruit ziet als `getal = (x - y) % z`. Bedenk zelf welke variabele op de plekken `x`, `y`, en `z` moeten komen. Print je resultaat om het te controleren!

Tip: je verwacht dat het antwoord 4 is: de 'd' is de vierde letter. Maar vergeet niet dat de computer begint te tellen bij 0, dus is het goede antwoord inderdaad 3.

</details>

---

<details>
<summary>Opdracht</summary>

Maak een variabele `verschuiving = -4`. We gaan nu uitrekenen wat de nieuwe verschoven letter moet zijn: we verschuiven de `d` met -4 plekken: het moet een `z` worden.

Pas de formule van de vorige opdracht aan: we moeten nu uitrekenen wat het getal is na de verschuiving. Je moet de verschuiving dus op de goede plek in de formule erbij optellen. Als je het goed doet, zie je nu dat je het alfabet rond gaat!

Tip: de 'z' is de hoeveelste letter? Want de computer begint met tellen bij 0.

</details>

---

We hebben nu bijna alle ingrediënten om een Caesar-gecodeerde tekst de ontcijferen! De formule die je gemaakt hebt moet terug in de functie van eerder, en dan kunnen we de functie gebruiken voor alle letters in een boodschap.

---

<details>
<summary>Opdracht</summary>

Je hebt eerder de functie gemaakt `letter_schuiven` gemaakt. Die functie deed het nog niet goed: je kon het alfabet nog niet rond. Nu kunnen we dat wel! We gaan daarom de functie aanpassen. Verwijder eerst wat er in de functie stond.

Je functie moet nu het volgende doen:
* Bereken het `getal` van de verschoven letter. Die formule kun je kopiëren van de vorige opdracht!
* Print vervolgens de nieuwe letter: dat is 97 (van de 'a') plus het nieuwe getal.

Test je functie met de volgende regels:
```python
letter_schuiven('a', 2)
letter_schuiven('k', -4)
letter_schuiven('c', -3)
letter_schuiven('x', 5)
```
Je functie moet nu het alfabet rond kunnen, dus zorg dat dat werkt!
</details>

---

Tijd om een woord te gaan ontcijferen!
```python
tekst = "eydpdqo"

for letter in tekst:
    letter_verschuiven(letter, 4)
```

In je functie print je de nieuwe letter. Automatisch komt er dan een <kbd>Enter</kbd> achter. Dat is onhandig: je wilt alle letters achter elkaar omdat het één woord is. Daarvoor is een trucje:
```python
print(nieuwe_letter, end = "")
```
Het kan zijn dat jij `nieuwe_letter` een andere naam hebt gegeven, maar het deel vanaf de komma moet je wel zo overnemen. Dat zegt dat er aan het einde 'niks' moet komen, dus ook geen Enter.

---

<details>
<summary>Opdracht</summary>

Pas de `print()`-regel in je functie aan zodat er geen Enter geprint wordt. Voer vervolgens de bovenstaande code uit: wat is het ontcijferde woord? 

Wat betekent "chzilguncwu"? De verschuiving is -20.

</details>

---

Om een tekst met meer dan één woord te ontcijferen moeten we nog één aanpassing doen:
```python
for letter in tekst:
    if letter.isalpha():
        letter_verschuiven(letter, 4)
    else:
        print(letter, end = "")
```

---

<details>
<summary>Opdracht</summary>

Wat betekent "xofob qyxxk qsfo iye ez, xofob qyxxk vod iye nygx"? De verschuiving is -10.

</details>

---

(Inspiratie van [deze](https://youtu.be/VH_mU42lQkQ?t=883) video en bijbehorende [course](https://learn.microsoft.com/nl-nl/training/modules/secret-message/).)