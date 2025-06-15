---
author: "Šimon Kochánek"
date: "15/6/2025"
output: pdf_document
fontsize: 10.5pt
---

<style type="text/css">
  body{
    font-size: 10.5pt;
  }
</style>

# 1. Bioinformatika

## Biologická data a jejich typy

Biologická data představují základní vstup pro bioinformatiku a zahrnují široké spektrum informací popisujících strukturu, funkci, variabilitu a chování živých organismů. Nejčastěji se setkáváme s:

- Genomickými daty (sekvence DNA a RNA)
- Proteomickými daty (informace o složení, množství a modifikacích proteinů)
- Metabolickými daty (údaje o metabolických drahách a produktech)
- Fenotypovými daty (popis znaků a vlastností organismu)

Správné zpracování těchto dat je klíčové pro pochopení biologických procesů, evoluce, chorob i pro biomedicínský výzkum.

## Transkripce, translace a replikace

### Transkripce

Transkripce je proces, během něhož je genetická informace uložená v DNA přepisována do molekuly RNA. Tento enzymaticky řízený proces zajišťuje RNA polymeráza a probíhá ve třech základních krocích:

- Iniciace: RNA polymeráza se naváže na specifickou oblast DNA zvanou promotor.
- Elongace: Postupné přidávání ribonukleotidů podle komplementarity s DNA.
- Terminace: Uvolnění hotové RNA po dosažení terminátorové sekvence.

Transkripce je klíčová pro regulaci genové exprese.

### Translace

Translace je proces, kterým se informace v mRNA překládá do pořadí aminokyselin v bílkovině. Probíhá na ribozomech ve třech krocích:

- Iniciace: Navázání malé ribozomální podjednotky na start kodon mRNA (AUG).
- Elongace: tRNA přináší aminokyseliny podle kodonů; vznikají peptidové vazby.
- Terminace: Uvolnění polypeptidu po dosažení stop kodonu (UAA, UAG, UGA).

### Replikace

Replikace je proces, kdy vzniká přesná kopie DNA před dělením buňky:

- Iniciace: Otevření dvoušroubovice DNA v místě originu replikace.
- Elongace: DNA polymeráza syntetizuje nové vlákno.
- Terminace: Oddělení dvou molekul DNA po dokončení kopírování.

  

  


## Biologické databáze

Biologické databáze uchovávají, organizují a zpřístupňují rozsáhlé soubory dat (sekvencování genomů, analýza proteinů aj.). 

Mezi nejvýznamnější patří:

- GenBank (sekvence nukleových kyselin)
- Protein Data Bank (PDB) (3D struktury proteinů)
- Ensembl (anotované genomy)

## Sequence alignment (zarovnání sekvencí)

Zarovnání sekvencí je základní bioinformatická technika, která hledá shody/podobnosti mezi sekvencemi DNA, RNA nebo proteinů.

Důvody pro zarovnání sekvencí:
- Zjištění homologie (společného původu) či funkční podobnosti
- Identifikace důležitých oblastí (např. aktivní místa enzymů)
- Odhalení evolučních vztahů a mutací

Typy zarovnání:
- Globální zarovnání (Needleman-Wunsch): srovnává celé sekvence
- Lokální zarovnání (Smith-Waterman): hledá nejpodobnější úseky v rámci sekvencí

Skórování zarovnání:
- Skórovací matice (BLOSUM, PAM) a penalizace za mezery
- Různé matice pro různé evoluční vzdálenosti (např. BLOSUM62 pro blízkou homologii)

## BLAST a heuristické algoritmy pro vyhledávání podobných sekvencí

BLAST (Basic Local Alignment Search Tool) je nejrozšířenější nástroj pro rychlé vyhledávání podobných oblastí v databázích. Pracuje ve dvou fázích: rychlé nalezení krátkých identických/podobných úseků (slov), pak rozšíření a přesnější zarovnání.

- Varianty: blastn (DNA-DNA), blastp (protein-protein) aj.
- Statistické ukazatele: E-value (očekávaný počet náhodných shod), p-value
- Další: FASTA (podobný, někdy citlivější na vzdálenější homologii)

## Dotplot a vizuální porovnávání sekvencí

Dotplot je grafická metoda pro porovnání dvou sekvencí. Na osách jsou znaky obou sekvencí, v místech shody je tečka. Diagonály označují podobné úseky; lze odhalit inverze, duplikace, posuny.

  

  

## Homologie, ortologie a paralogie

- Homologie: sekvence mají společného předka
    - Ortologie: geny vzniklé speciací (různé druhy, stejná funkce)
    - Paralogie: geny vzniklé duplikací v jednom organismu (mohou diverzifikovat)

Rozpoznání homologických vztahů je klíčové pro přenos funkční anotace a evoluční analýzy.

## Strukturní srovnávání a predikce struktury proteinů

### Strukturální srovnávání

Porovnávání 3D struktur proteinů může odhalit podobnosti nezjevné na úrovni sekvence a napomáhá objasnit evoluční a funkční vztahy.

### Predikce proteinové struktury

- Homologní modelování: modelování podle známé struktury podobného proteinu (templátu)
- Ab initio modelování: bez známého templátu, čistě na základě fyzikálně-chemických principů
- Threading: hledání nejvhodnějšího známého foldingu bez významné sekvenční podobnosti

Moderní přístupy (např. AlphaFold) využívají kombinace algoritmů a strojové učení.

## Substituční matice BLOSUM

BLOSUM (BLOcks SUbstitution Matrix): sada substitučních matic pro zarovnávání proteinů. Odvozeny z bloků evolučně diverzifikovaných sekvencí; umožňují hodnotit pravděpodobnost záměn aminokyselin při evoluci. Např. BLOSUM62 vhodná pro blízké příbuznosti.

## Predikce sekundární struktury proteinů

Sekundární struktura = alfa-helixy, beta-listy, smyčky

Metody predikce: Chou-Fasman, GOR – využívají pravděpodobnosti výskytu aminokyselin v daném typu struktury.

## Multiple Sequence Alignment (MSA)

MSA znamená zarovnání tří a více sekvencí současně. Pomáhá najít konzervované (důležité) oblasti pro evoluční studie, funkční anotace i predikci proteinových struktur.

Progresivní metody: např. CLUSTAL

HMM metody: využití skrytých Markovovských modelů

# 2. Pravděpodobnost a matematická statistika

## Náhodná veličina: diskrétní a spojité rozdělení, distribuční funkce, pravděpodobnostní funkce, hustota

Náhodná veličina je proměnná, jejíž hodnota závisí na výsledku náhodného jevu.

Rozlišujeme dva typy:

- Diskrétní náhodná veličina  
  Nabývá jen určitých (napočitatelných) hodnot, např. počet vržených šestek při 10 hodech kostkou.

- Spojitá náhodná veličina  
  Může nabývat libovolných hodnot v intervalu, např. tělesná výška člověka.

### Pravděpodobnostní funkce (PMF) a hustota pravděpodobnosti (PDF)

- Pravděpodobnostní funkce  
  \( p(x) = P(X = x) \)  
  Je definovaná pro diskrétní veličiny. U každé hodnoty \( x \) říká, jaká je pravděpodobnost, že ji veličina nabude.

- Hustota pravděpodobnosti  
  \( f(x) \)  
  Používá se pro spojité veličiny. Pravděpodobnost, že veličina spadne do intervalu \([a, b]\), je  
  \( \int_a^b f(x) dx \).  
  Pravděpodobnost pro přesnou hodnotu je vždy nulová.

### Distribuční funkce

- Distribuční funkce  
  \( F(x) = P(X \leq x) \)  
  Udává kumulativní pravděpodobnost, že veličina je menší nebo rovna \( x \).

  - Pro diskrétní veličiny má tvar schodovité funkce (skoky odpovídají jednotlivým hodnotám).
  - Pro spojité veličiny je spojitá a plynule roste.

  

  

  

## Kvantily, střední hodnota, rozptyl

### Kvantily

- **Kvantil** je hodnota, která rozděluje uspořádaný soubor dat na zvolené části.
- **Medián** je 50% kvantil (polovina hodnot leží níže, polovina výše).
- **Kvartily** (Q1, Q2, Q3) dělí soubor na čtvrtiny, **percentily** na 100 částí.

### Střední hodnota (průměr, očekávaná hodnota)

- Pro diskrétní veličiny: \( E[X] = \sum x \cdot p(x) \)
- Pro spojité veličiny: \( E[X] = \int x f(x) dx \)
- Udává průměrnou (očekávanou) hodnotu při nekonečném opakování náhodného pokusu.

### Rozptyl

- Měří, jak moc jsou hodnoty rozptýleny kolem střední hodnoty.
- \( Var(X) = E[(X - E[X])^2] \)
- **Standardní odchylka** je odmocnina z rozptylu a má stejnou jednotku jako původní veličina.

## Bodové a intervalové odhady

### Bodový odhad

- Konkrétní číselná hodnota, kterou stanovíme na základě výběru jako odhad parametru populace (např. výběrový průměr jako odhad průměru celé populace).

### Intervalový odhad

- Rozsah hodnot, který s určitou pravděpodobností obsahuje skutečný parametr populace (například 95% interval spolehlivosti pro průměr).
- Zohledňuje nejistotu v odhadu, je praktičtější než bodový odhad.
- Interval se zužuje s větším počtem měření a s menší rozptýleností dat.

## Obecné principy testování statistických hypotéz

- Testování hypotéz je proces, kterým na základě vzorku dat rozhodujeme, zda nějaký předpoklad o populaci platí.

### Formulace hypotéz

- **Nulová hypotéza** (\( H_0 \)): většinou "není efekt", "data odpovídají předpokladu".
- **Alternativní hypotéza** (\( H_1 \)): existuje efekt, rozdíl apod.

### Postup testování

1. Výběr testu podle typu dat a hypotézy (např. t-test, z-test, chi-kvadrát test).
2. Stanovení hladiny významnosti (\( \alpha \)), často 0,05 (5 %).
3. Výpočet testové statistiky a p-hodnoty.
4. Rozhodnutí: Pokud \( p < \alpha \), zamítáme \( H_0 \).

- **Chyba I. druhu:** Pravděpodobnost, že zamítneme správnou \( H_0 \) (falešně pozitivní výsledek, velikost je \( \alpha \)).
- **Chyba II. druhu:** Pravděpodobnost, že nezamítneme nepravdivou \( H_0 \) (falešně negativní výsledek, velikost je \( \beta \)).
- **Síla testu:** \( 1 - \beta \), pravděpodobnost správného zamítnutí nepravdivé nulové hypotézy.

## Testy parametrů normálního rozdělení

- Testují vlastnosti normálně rozdělených populací, zejména střední hodnotu:

- **Z-test:** Pro velké výběry nebo pokud známe rozptyl populace.
- **T-test:** Pro malé výběry nebo neznámý rozptyl. Existují:
    - Jednovýběrový t-test (porovnání výběrového průměru s hypotetickou hodnotou).
    - Dvouvýběrový t-test (porovnání průměrů dvou skupin, nezávislých).
    - Párový t-test (porovnání hodnot na stejných subjektech před a po zásahu).

## Chi-kvadrát test dobré shody

- Testuje, zda pozorované četnosti odpovídají očekávaným.
- Používá se pro kategorická data, např. pro ověření, zda rozdělení krevních skupin v populaci odpovídá teoretickému rozdělení.

### Formulace hypotéz

- \( H_0 \): pozorované frekvence odpovídají očekávaným.
- \( H_1 \): neodpovídají.

## Variabilita a normálnost dat

- **Variabilita:** měří rozptyl hodnot v datech – základní ukazatele jsou rozptyl, směrodatná odchylka, interkvartilové rozpětí (IQR).
- **Normálnost dat:** ověřuje se pomocí statistických testů (Shapiro-Wilk, Kolmogorov-Smirnov), případně graficky (histogram, Q-Q plot).
- Pro normální rozdělení je typická zvonovitá křivka; většina statistických testů předpokládá normalitu dat.

  

  

  

  

## Typy experimentálních a observačních studií

### Experimentální studie

- **Randomizovaná kontrolovaná studie (RCT):**
    - Účastníci jsou náhodně rozděleni do skupin, jedna dostává intervenci, druhá slouží jako kontrola. Minimalizuje vliv náhody a zkreslení.
- **Crossover studie:**
    - Každý účastník dostává postupně různé léčby; slouží k eliminaci individuálních rozdílů.

### Observační studie

- **Kohortové studie:**
    - Sledování skupiny lidí v čase, zjišťování výskytu určitého jevu (nemoci) podle různých faktorů.
    - **Prospektivní:** sledují se dopředu.
    - **Retrospektivní:** analyzují se již existující záznamy.
- **Případově-kontrolní studie:**
    - Porovnání skupiny s onemocněním (případy) a bez onemocnění (kontroly), hledání rozdílů v expozici rizikovým faktorům.

## Medicína založená na důkazech (Evidence Based Medicine, EBM)

EBM je systematický přístup, který spojuje:

- Nejlepší dostupné vědecké důkazy,
- klinické zkušenosti lékaře,
- preference a hodnoty pacienta.

### Kroky v EBM

1. **Formulace klinické otázky** (často podle PICO: pacient, intervence, komparátor, outcome/výsledek).
2. **Vyhledání důkazů** (PubMed, Cochrane atd.).
3. **Kritické zhodnocení důkazů** (například pomocí nástroje GRADE).
4. **Aplikace důkazů** do konkrétní klinické praxe s ohledem na individuální situaci pacienta.
5. **Hodnocení výsledků a zpětná vazba**.

---
author: "Šimon Kochánek"
date: "15/6/2025"
output: pdf_document
fontsize: 10.5pt
---

<style type="text/css">
  body{
    font-size: 10.5pt;
  }
</style>

# Aplikovaná zdravotnická informatika

### Data, informace a znalosti v medicíně

Ve zdravotnictví hraje zásadní roli rozlišování mezi daty, informacemi a znalostmi:

- **Data** jsou základní, nezpracovaná fakta – například naměřené hodnoty (teplota, krevní tlak) nebo laboratorní výsledky. Bez dalšího kontextu samy o sobě nic neříkají.
- **Informace** vznikají uspořádáním a interpretací dat. Například když se k naměřené hodnotě přidá čas a kontext (kdo byl měřen, v jakém stavu), dostáváme smysluplnou informaci.
- **Znalosti** představují porozumění informacím v širším kontextu, jejich propojení s vědeckými poznatky a zkušeností – umožňují rozhodování v konkrétních situacích, např. volbu správné léčby na základě předchozích případů a aktuálního vývoje medicíny.

### Doporučené lékařské postupy

- Systematicky vypracované dokumenty, které určují optimální způsoby diagnostiky, léčby a péče o pacienta při různých diagnózách.
- Jsou vytvářeny na základě aktuálních vědeckých důkazů, klinických studií i zkušeností odborníků.
- Cílem je standardizovat péči, zvýšit její kvalitu a bezpečnost, snížit riziko chyb a nejednotnosti mezi jednotlivými pracovišti.
- Uplatňování těchto postupů umožňuje poskytovat léčbu, která je ověřená a vysoce efektivní.

### Medicína založená na důkazech (Evidence Based Medicine, EBM)

- Přístup, který integruje nejlepší dostupné vědecké důkazy s klinickou zkušeností lékaře a preferencemi pacienta.
- EBM zahrnuje systematické vyhledávání, kritické hodnocení a aplikaci relevantních studií do praxe.
- Pomáhá lékařům činit rozhodnutí, která jsou podložena vědecky ověřenými poznatky a zároveň jsou přizpůsobena konkrétnímu pacientovi.

### Základy biomedicínské statistiky

Biomedicínská statistika je vědní disciplína, která umožňuje analyzovat, interpretovat a vyhodnocovat medicínská data:

- **Popisná statistika** sumarizuje data pomocí průměru, mediánu, rozptylu atd.
- **Testování hypotéz** (např. t-test, ANOVA) umožňuje zjišťovat rozdíly mezi skupinami.
- **Korelace a regrese** hledají vztahy a závislosti mezi proměnnými.
- Statistická analýza je základem pro rozhodování na základě dat a umožňuje vědecky hodnotit účinnost léčby, nové postupy či rizikové faktory.

### Počítačová bezpečnost a informační systémy ve zdravotnictví

Počítačová bezpečnost ve zdravotnictví zahrnuje ochranu zdravotnických dat i samotných informačních systémů před neoprávněným přístupem, zneužitím, ztrátou či kybernetickými útoky.

#### Klíčové prvky bezpečnosti:

- **Autentifikace:** Ověření identity uživatele (například heslem, kartou, otiskem prstu).
- **Autorizace:** Nastavení práv a oprávnění uživatelů k různým datům a funkcím.
- **Šifrování:** Ochrana dat jak při přenosu, tak při ukládání (pomocí SSL/TLS, VPN apod.).
- **Zálohování:** Pravidelná tvorba záloh pro možnost obnovy v případě havárie nebo útoku.
- **Firewall, antivirus:** Ochrana před neoprávněným vstupem a škodlivým softwarem.
- **Bezpečnostní protokoly:** Standardizované způsoby bezpečné komunikace (HTTPS, SSL/TLS).

### Ochrana a zabezpečení dat

Ochrana dat ve zdravotnictví se zaměřuje na důvěrnost, integritu a dostupnost zdravotnických údajů:

- **Důvěrnost (Confidentiality):** Ochrana osobních údajů před neoprávněným přístupem, např. šifrováním a kontrolou přístupu.
- **Integrita (Integrity):** Zajištění, že data nebyla neoprávněně změněna nebo poškozena.
- **Dostupnost (Availability):** Zajištění, že data budou v případě potřeby rychle dostupná oprávněným osobám.

### Archivace dat

- **Cíl:** Dlouhodobé uchovávání lékařských záznamů a dalších důležitých dat.

**Aspekty:**

- **Formát:** Výběr vhodných formátů pro dlouhodobou čitelnost.
- **Bezpečnost:** Prevence neoprávněného přístupu.
- **Dostupnost:** Snadný přístup pro budoucí použití (léčba, výzkum, právní účely).

  

  

  

  

  

  

### Zdravotnický profesionalizmus a ochrana osobních údajů

Profesionalizmus ve zdravotnictví zahrnuje nejen odborné a etické chování zdravotníků, ale také respektování práv pacientů:

- Důležitým aspektem je ochrana osobních údajů pacientů (zejména citlivých zdravotních údajů).
- Platí zde přísné právní předpisy (například GDPR), které vyžadují správné nakládání s osobními daty, jejich zabezpečení a minimalizaci rizik zneužití.
- Každý zdravotník je povinen zachovávat mlčenlivost a chránit informace před třetími osobami.

### Standardizace a klasifikační systémy v medicíně

Aby bylo možné efektivně sdílet, analyzovat a porovnávat zdravotnická data, používají se standardy a klasifikační systémy:

- **ICD (International Classification of Diseases):** Mezinárodní klasifikace nemocí pro kódování diagnóz (aktuálně verze ICD-10).
- **ICF (International Classification of Functioning, Disability and Health):** Klasifikace funkčního stavu, disability a zdraví, užitečná pro popis funkčních omezení pacientů.
- **UMLS (Unified Medical Language System):** Integruje různé lékařské terminologie pro snazší komunikaci a vyhledávání.
- **MeSH (Medical Subject Headings):** Strukturovaný slovník pro indexování biomedicínské literatury.
- **SNOMED CT:** Rozsáhlý systém klinických termínů pro detailní popis diagnóz, procedur i zdravotních stavů.

### Elektronický zdravotní záznam (EHR)

**Elektronický zdravotní záznam (EHR, Electronic Health Record)** je digitální verze kompletní dokumentace o pacientovi:

- Obsahuje anamnézu, laboratorní výsledky, diagnózy, léčbu, medikaci, zprávy a další informace potřebné pro péči.
- Umožňuje snadné sdílení informací mezi různými zdravotnickými zařízeními.
- Přináší výhody jako zlepšení kvality péče (dostupnost úplných údajů), zvýšení efektivity a snížení administrativní zátěže a chyb.

### Standardy (OpenEHR, CEN, HL7)

Pro interoperabilitu (vzájemnou komunikaci systémů) a kvalitu dat se využívají mezinárodní standardy:

- **OpenEHR:** Platforma s otevřeným zdrojovým kódem pro EHR, definice archetypů pro klinická data.
- **CEN:** Evropský výbor pro normalizaci, vyvíjí standardy pro zdravotnické IT.
- **HL7 (Health Level Seven):** Globální standard pro výměnu zdravotních informací, definice zpráv a struktury dat.

**Příklad HL7 zprávy:**

```
MSH|^&|EPIC|EPICADT|iFW|SMSADT|199912271408|CHARRIS|ADT^A04|1817457|D|2.5|
PID||0493575^^^2^ID 1|454721||DOE^JOHN^^^^|DOE^JOHN^^^^|19480203|M||B|254 MYSTREET AVE^^MYTOWN^OH^44123^USA||(216)123-4567|||M|NON|4000034031129086|
NK1||ROE^MARIE^^^^|SPO||(216)123-4567||EC|||||||||||||||||||||||||||
PV1||O|168219C~PMA^^^^^^^^^||||277^ALLEN MYLASTNAME^BONNIE^^^^|||||||||| ||2688684|||||||||||||||||||||||||199912271408||||||002376853
```

**HL7 segmenty v tomto příkladu obsahují následující informace:**

- **MSH (Message Header):** Obsahuje informace o samotné zprávě – odesílatel, příjemce, typ zprávy, datum a čas odeslání.
- **PID (Patient Information):** Demografické údaje o pacientovi, jako je jméno, identifikátor a adresa.
- **NK1 (Next of Kin):** Kontaktní údaje na nejbližší příbuzné pacienta.
- **PV1 (Patient Visit):** Informace o hospitalizaci pacienta, například přiřazené umístění a doporučující lékař.

### Systémy pro podporu rozhodování

Systémy na podporu rozhodování (DSS) v medicíně poskytují lékařům nástroje k zlepšení rozhodování. DSS mohou zahrnovat:

- **Klinické algoritmy:** Automatizovaná doporučení na základě údajů o pacientovi.
- **Upozornění a výstrahy:** Upozornění na možné lékové interakce nebo alergie.
- **Analýza údajů:** Pokročilá analýza k identifikaci vzorů a trendů v datech pacientů.

### Medicínské informační zdroje

Mezi lékařské informační zdroje patří databáze, knihovny a online nástroje, které poskytují přístup k vědeckým článkům, klinickým studiím a dalším relevantním informacím:

- **PubMed:** Databáze vědeckých článků z biomedicíny (MEDLINE).
- **Cochrane Library:** Systematické přehledy a metaanalýzy.
- Další specializované databáze (Embase, Scopus atd.).

### Kvalita zdravotnických informací na internetu

Kvalita zdravotních informací na internetu je klíčová pro poskytování správných informací pro pacienty a zdravotnické pracovníky. Hodnocení kvality zahrnuje:

- **Přesnost a spolehlivost:** Informace by měly být vědecky ověřené a aktuální.
- **Autentičnost zdrojů:** Informace by měly pocházet z důvěryhodných a odborných zdrojů.
- **Čitelnost a srozumitelnost:** Informace by měly být prezentovány jasným a srozumitelným způsobem.


# 4. Biologické signály

### Vlastnosti biologických signálů

Biologické signály jsou měřitelné fyziologické projevy živých organismů, které mají nejčastěji elektrický, ale i mechanický či chemický charakter. Tyto signály vznikají jako důsledek aktivit buněk, tkání nebo orgánů a slouží jako cenný zdroj informací pro diagnostiku a sledování zdravotního stavu.

Mezi základní vlastnosti biologických signálů patří:

- **Amplituda** – maximální hodnota signálu, která vypovídá o síle sledovaného jevu (např. napětí u EKG).
- **Frekvence** – udává, kolikrát za sekundu se signál opakuje (Hz), umožňuje rozlišovat typy aktivit (např. srdeční frekvence).
- **Časové trvání** – délka trvání jednotlivé události v signálu (např. QRS komplex u EKG).
- **Dynamika** – rychlost změn a variabilita signálu v čase.
- **Periodicita** – pravidelnost výskytu opakujících se složek signálu.

### Způsoby vzniku, snímání a základní parametry biosignálů

###### Vznik biosignálů

Biosignály mohou vznikat několika způsoby:

- **Elektrofysiologické** – elektrická aktivita buněk, například akční potenciály neuronů, svalových vláken či srdečních buněk.
- **Mechanické** – například pohyby svalů, vibrace, srdeční zvuky.
- **Chemické** – změny koncentrací iontů nebo metabolitů.

###### Snímání biosignálů

- **Elektrody** – nejběžnější způsob snímání elektrických biosignálů; existují povrchové (na kůži), jehlové (do svalu) či intramuskulární.
- **Senzory** – piezoelektrické (měření tlaku/pohybu), optické (měření světla), chemické (detekce koncentrace látek).
- **Zobrazovací metody** – MRI, CT, ultrazvuk pro vizualizaci vnitřních struktur a funkcí.

###### Základní parametry biosignálů pro diagnostiku

- **Amplituda** – síla signálu, důležitá např. pro posouzení síly srdeční kontrakce.
- **Frekvence** – umožňuje rozlišovat různé typy fyziologických dějů (např. EEG pásma).
- **Latence** – doba mezi podnětem a reakcí (např. při nervovém přenosu).
- **Rychlost vedení** – zejména u nervových a svalových signálů (hodnotí rychlost přenosu informace).

### Signály srdce, mozku, svalů a nervového systému

###### Signály srdce (EKG)

**Elektrokardiogram (EKG)** zaznamenává elektrickou aktivitu srdce pomocí elektrod umístěných na těle.

- **SA uzel** generuje pravidelné impulsy, které se šíří srdeční svalovinou.
- Standardní 12-svodové EKG poskytuje informace o elektrické aktivitě srdce z různých směrů.
- Klíčové části záznamu:
    - **Vlna P:** Depolarizace síní
    - **QRS komplex:** Depolarizace komor
    - **Vlna T:** Repolarizace komor
    - Intervaly (PR, QT) a segmenty (ST) umožňují detailní diagnostiku.

###### Signály mozku (EEG)

**Elektroencefalogram (EEG)** zachycuje elektrickou aktivitu mozku, zejména v mozkové kůře.

- EEG snímá slabé elektrické potenciály vznikající synchronní aktivitou neuronů.
- Používají se systémy umístění elektrod (např. 10-20 systém).
- Základní frekvenční pásma EEG:
    - **Delta (0,5–4 Hz):** Hluboký spánek
    - **Theta (4–8 Hz):** Lehký spánek, relaxace
    - **Alfa (8–13 Hz):** Klid, relaxace
    - **Beta (13–30 Hz):** Aktivní myšlení
    - **Gama (>30 Hz):** Složitá kognice
- Další sledované parametry jsou amplituda a synchronizace neuronální aktivity.

###### Signály svalů (EMG)

**Elektromyogram (EMG)** zaznamenává elektrickou aktivitu svalů při kontrakci.

- Při aktivaci svalu vznikají elektrické potenciály, které lze snímat povrchově nebo jehlovými elektrodami.
- Sleduje se zejména amplituda, frekvence, tvar a průběh motorických jednotek.

###### Signály nervového systému (ENG)

**Elektroneurografie (ENG)** měří elektrické impulsy v periferních nervech.

- Snímání probíhá povrchovými elektrodami.
- Hodnotí se rychlost vedení, amplituda akčního potenciálu, latence a refrakterní období.

### Metody a algoritmy zpracování a vyhodnocování biosignálů

###### Předzpracování signálů

- **Filtrace:** Odstraňování nežádoucích složek (šum, artefakty), např. pomocí dolních, horních a pásmových filtrů.
- **Korekce artefaktů:** Např. pomocí analýzy nezávislých komponent (ICA) lze oddělit rušivé signály od užitečné složky.
- **Normalizace a detekce chyb:** Korekce na základě referenčních kanálů, detekce a odstranění chybějících nebo chybných dat.

###### Analýza v časové a frekvenční oblasti

- **Časová analýza:** Statistické výpočty (průměr, směrodatná odchylka, RMS), detekce vrcholů a charakteristických rysů (např. QRS komplex u EKG).
- **Frekvenční analýza:** Převod signálu z časové do frekvenční oblasti pomocí Fourierovy transformace, která umožňuje určit dominantní frekvence (např. spektrální obsah EEG)

###### Nestacionarita EEG

EEG je typický příklad **nestacionárního signálu** – jeho statistické vlastnosti se v čase mění. Pro jeho analýzu jsou vhodné metody, které umí popsat časově-frekvenční dynamiku, např. vlnková transformace nebo krátkodobá Fourierova transformace (STFT).

### Frekvenční rozsahy a pásma biosignálů

Biologické signály se vyskytují v různých frekvenčních rozsazích:

- **Nízké frekvence (0–0,5 Hz):** Dlouhodobé trendy, stacionární složky.
- **Střední frekvence (0,5–40 Hz):** Například většina složek EKG, EEG (alfa, beta pásma).
- **Vysoké frekvence (40 Hz až jednotky kHz):** Svalová aktivita, např. EMG (5–1000 Hz).

### Převod biosignálu do počítače, vzorkování a kvantizace

Aby bylo možné biosignály zpracovávat na počítači, je třeba je **digitalizovat**:

- **A/D převodník** (analogově-digitální převodník) převede spojitý signál na diskrétní řadu čísel.
- **Vzorkovací frekvence** musí být dle **Nyquistova teorému** nejméně dvojnásobek maximální frekvence v signálu – jinak vznikne **aliasing** (falešné složky, zkreslení signálu).
- **Kvantizace** znamená převod spojité amplitudy signálu na diskrétní úrovně – omezená přesnost vede ke **kvantizační chybě**.
- Nedostatečná vzorkovací frekvence či hrubá kvantizace může výrazně zhoršit kvalitu zaznamenaných dat a ovlivnit další analýzu.

### Spektrální analýza biosignálů

Spektrální analýza umožňuje studovat frekvenční složení signálu a identifikovat důležité rytmy či patologie.

- **Neparametrické metody:**
    - **Fourierova transformace:** Převod signálu na spektrum bez předpokladu modelu.
    - **Periodogram:** Odhad výkonového spektra, vizualizuje rozložení energie do frekvencí.
- **Parametrické metody:**
    - Např. **AR (autoregresní) modely** – signál je popsán soustavou rovnic, umožňují přesnější odhad spektra v krátkých úsecích nebo u šumových signálů.
- **FFT (Fast Fourier Transform):** Rychlý algoritmus pro výpočet diskrétní Fourierovy transformace.
- Praktické problémy: Omezená délka záznamu, spektrální únik (leakage), rušení.

### Křížové spektrum, koherence a fáze

Při analýze vícekanálových biosignálů (například EEG z více elektrod):

- **Křížové spektrum:** Popisuje vztah mezi dvěma signály ve frekvenční oblasti.
- **Koherence:** Míra synchronizace mezi dvěma signály v daném frekvenčním pásmu.
- **Fáze:** Informace o časovém zpoždění mezi signály – důležité například pro zkoumání komunikace mezi oblastmi mozku.

### Filtrace a odstranění šumu

K odstranění šumu v biosignálech se používají digitální filtry:

- **FIR (Finite Impulse Response):** Filtry s konečnou impulzní odezvou – mají předvídatelné chování a jsou vždy stabilní.
- **IIR (Infinite Impulse Response):** Filtry s nekonečnou impulzní odezvou – umožňují dosáhnout vyšší selektivity, ale mohou být méně stabilní.
- **Adaptivní filtry, vlnková denoizace:** Umožňují pokročilé odstranění rušení při zachování důležitých složek signálu.

### Vizualizace výsledků analýzy

Vizualizace pomáhá prezentovat a interpretovat výsledky:

- **Spektrogramy:** Zobrazují, jak se frekvenční spektrum mění v čase.
- **CSA (Condensed Spectral Array):** Zobrazuje dynamiku změn výkonu v různých frekvenčních pásmech.
- **Topografické mapování (brain mapping):** Vizualizace prostorového rozložení signálů (zejména EEG) na povrchu hlavy pomocí barevných map.

###### Princip brain mappingu, interpolace a mapování parametrů

- **Brain mapping:** Barevné mapy znázorňují rozložení amplitudy nebo frekvence na povrchu mozku.
- **Interpolace:** K vyhlazení a doplnění hodnot mezi elektrodami se používají matematické metody (např. splajnová interpolace).
- **Mapování amplitudy a frekvence:** Umožňuje lokalizovat oblasti s patologickou nebo charakteristickou aktivitou (diagnostika epilepsie, demence aj.).


# 5. Zpracování obrazových dat

### Zrakový orgán, jasová a kontrastní citlivost oka

Lidské oko je smyslový orgán, který umožňuje vnímání světla a barev. Hlavními částmi oka jsou rohovka, čočka, sítnice a zrakový nerv. Na sítnici jsou fotoreceptory: **tyčinky** (zajišťují vidění za šera, nerozeznávají barvy) a **čípky** (zajišťují barevné vidění a ostrost). 

1. **Rohovka**
2. **Přední komora**
3. **Vlastní čočka**
4. **Sklivec**
5. **Sítnice**

![Anatomie oka](img/anatomieOka.png)

**Jasová citlivost oka** popisuje schopnost oka detekovat různé úrovně osvětlení, nejcitlivější je při středním jasu. Tento fenomén je důležitý pro kalibraci obrazových zařízení a pro design osvětlení tak, aby odpovídal lidskému vnímání.

**Kontrastní citlivost oka** vyjadřuje schopnost rozlišit objekty s různou úrovní jasu – maximální je při středních prostorových frekvencích a klesá při extrémně nízkých či vysokých frekvencích. Tato citlivost není konstantní přes celé viditelné spektrum a závisí na různých faktorech, včetně úrovně osvětlení a vzdálenosti objektu.

### Prostorová a časová rozlišovací schopnost oka

**Prostorová rozlišovací schopnost oka** znamená schopnost rozlišit jemné detaily a blízké objekty v obraze, což je dáno hustotou fotoreceptorů (zejména v oblasti makuly).  
**Časová rozlišovací schopnost** popisuje, jak rychle dokáže oko zachytit změny v čase – lidské oko dokáže vnímat plynulý pohyb při cca 24 snímcích za sekundu a vyšších rychlostech (televize, video).

### Obecné schéma procesu zobrazení

Proces zobrazení zahrnuje několik kroků:

1. **Snímání obrazu** – světlo ze scény je zachyceno snímačem (kamerou, skenerem).
2. **Digitalizace** – převod analogového signálu na digitální (pomocí vzorkování a kvantizace).
3. **Zpracování obrazu** – různé algoritmy zlepšují kvalitu, detekují objekty či analyzují obraz.
4. **Zobrazení** – výsledek je vizualizován na monitoru či jiném zařízení.

![Schéma procesu zobrazení](img/schemaProcesuZobrazeni.png)

### Sběr obrazových dat, vzorkování a kvantizace

Sběr obrazových dat je proces, jehož cílem je převést vizuální scénu do formy, kterou lze dále zpracovávat počítačem. Začíná to snímáním obrazu pomocí zařízení jako jsou kamery, skenery nebo čidla. Výsledkem může být buď analogový obraz (spojitý signál), nebo digitální obraz (diskrétní mřížka pixelů).

Efektivní sběr obrazových dat závisí na kvalitě optiky, vlastnostech použitého senzoru (např. CCD, CMOS), kvalitě osvětlení a stabilizaci obrazu. Důležitou roli hraje i následné zpracování signálu.

###### Co je to pixel?

**Pixel** (zkratka z *picture element*) je základní jednotka digitálního obrazu. Každý pixel představuje malou část obrazu a nese informaci o barvě a/nebo jasu v daném místě.

###### Vzorkování (Sampling Rate)

Vzorkování je první krok při převodu analogového obrazu na digitální. Znamená to, že v pravidelných intervalech „odebíráme vzorky“ hodnoty intenzity světla nebo barvy po celé ploše obrazu.  
Podle Shannonova teorému je nutné vzorkovat alespoň dvojnásobkem nejvyšší frekvence detailu v obraze, aby nedocházelo ke zkreslení (aliasingu).

###### Kvantizace (Quantization)

Po vzorkování následuje kvantizace – převod spojitých hodnot jasů nebo barev na omezený počet diskrétních úrovní, např. 256 odstínů šedi při 8 bitech na pixel.

###### Artefakty při vzorkování a kvantizaci

- **Nedostatečné vzorkování** způsobuje **aliasing** – vznik falešných vzorů, „klikaté“ okraje, ztráta detailů.
- **Hrubá kvantizace** způsobuje **pásmování** (banding) – místo plynulých přechodů jsou vidět skoky mezi odstíny.

### Základní úlohy zpracování obrazu

###### 1. Zlepšení kvality obrazu (image enhancement)

Cílem je **vylepšit vizuální vlastnosti obrazu**:

- **Odstranění šumu** (průměrování, mediánová filtrace)
- **Úprava kontrastu a jasu** (ekvalizace histogramu, gamma korekce)
- **Zaostření (ostření hran)** (zvýraznění hran a detailů)

###### 2. Segmentace a extrakce objektů

- **Segmentace**: rozdělení obrazu na oblasti/objekty se společnými vlastnostmi
- **Extrakce objektů**: oddělení objektů od pozadí (např. prahování, detekce hran, region-growing, k-means, watershed)

###### 3. Komprese obrazu (image compression)

- **Bezeztrátová komprese** (PNG, GIF, RLE, Huffman)
- **Ztrátová komprese** (JPEG)
- Komprese je nutná pro ukládání, přenos videa, práci v omezeném úložišti

###### 4. Rozpoznávání vzorů (pattern recognition)

- **Automatická identifikace objektů, tvarů či struktur**
- Metody: šablonování, detekce hran, extrakce příznaků, strojové učení, deep learning
  
  
  
  
  
  
  
  
  
  
  

### Lineární systémy, impulzní odezva, prostorová invariance

###### Lineární systém

Splňuje principy **superpozice** (součet vstupů → součet výstupů) a **homogenity** (násobení vstupu konstantou → výstup násoben konstantou).  
Základ většiny matematických operací při zpracování signálů a obrazů.

###### Impulzní odezva

Výstup systému na **Diracův impulz** (teoretický bodový podnět).  
Umožňuje předpovědět chování systému pro jakýkoliv vstup.

###### Prostorová invariance

Systém je **prostorově invariantní**, pokud jeho chování je stejné kdekoliv v obraze – umožňuje efektivní aplikaci operací (konvoluce) v celém obraze.

### Konvoluce a Korelace

###### Konvoluce

- Filtr (kernel) „klouže“ po obraze, v každé pozici vypočítá vážený součet pixelů a filtru.
- Při konvoluci se filtr otáčí kolem středu na obou osách.
- Použití: rozmazání, ostření, detekce hran.

###### Korelace

- Podobné konvoluci, ale filtr se **neotáčí**.
- Použití: detekce vzorů, měření podobnosti.
- Pro symetrické filtry je výsledek shodný.

### Princip barevného zobrazení, barevné modely

- **RGB:** Aditivní model (monitory, kamery)
- **CMY(K):** Subtraktivní (tisk)
- **HSV/HLS:** Odstín, sytost, světlost
- **Barevná hloubka:** Počet barev v obraze, běžně 24 bitů (True Color)

### Snímací režimy

- **Čárová grafika:** pouze čáry
- **Polotóny:** simulace odstínů pomocí teček (tisk)
- **Šedotónový režim:** různé úrovně šedi
- **Barevné režimy:** informace o barvě v každém pixelu

### Bodové, lokální a globální operace nad obrazem

- **Bodové operace:** mění každý pixel samostatně (jas)
- **Lokální operace:** používají okolí pixelu (filtrace, vyhlazení)
- **Globální operace:** působí na celý obraz (ekvalizace histogramu)

### Prahování a adaptivní prahování

- **Prahování:** segmentace na základě prahu (objekt vs. pozadí)
- **Adaptivní prahování:** různé prahy v různých částech obrazu

### Úprava kontrastu, ekvalizace histogramu

- **Úprava kontrastu:** zvýraznění rozdílů světlé/tmavé
- **Ekvalizace histogramu:** rozložení jasových hodnot, zvýraznění detailů

### Logaritmický a exponenciální operátor

- **Logaritmická transformace:** zvýraznění tmavých oblastí, stlačení světlých
- **Exponenciální operace:** zvýraznění světlých oblastí

### Vyhlazovací filtry, zaostření, mediánová filtrace

- **Vyhlazovací filtry:** průměrovací, gaussovské – rozmazání, odstranění šumu
- **Zaostřovací filtry:** zvýraznění detailů, ostrosti
- **Mediánová filtrace:** nahrazuje pixel mediánem okolí, odstranění „sůl a pepř“ šumu

### Fourierova transformace, filtrace ve frekvenční oblasti, DCT

###### Fourierova transformace (DFT)

- Převod obrazu do frekvenční domény (analýza složek, kde je šum, kde detaily)
- **Nízké frekvence:** velké oblasti, plynulé přechody
- **Vysoké frekvence:** detaily, hrany, šum

###### Filtrace ve frekvenční oblasti

- Dolní propust: vyhlazení, odstranění šumu
- Horní propust: zvýraznění hran, detailů
- Postup: DFT → filtr → inverzní DFT

###### DCT

- Kosinová transformace (JPEG komprese, bloky 8x8 pixelů)
- Efektivní pro kompresi a potlačení detailů, které oko nevnímá

### Detekce hran, segmentace, Houghova transformace

- **Detekce hran:** Sobel, Prewitt, Canny
- **Segmentace:** rozdělení obrazu na oblasti s podobnými vlastnostmi
- **Houghova transformace:** detekce přímek, kružnic

### Metody komprese obrazu

- **Jednoduché metody:** RLE
- **Statistické:** Huffman
- **Slovníkové:** LZW
- **Transformační:** JPEG, DCT, wavelet

### Matematická morfologie (eroze, dilatace, otevření, uzavření)

###### Základní princip

- Práce s geometrickými strukturami v obrazu pomocí **strukturního elementu**

###### Eroze

- Zmenšuje světlé oblasti, odstraňuje malé detaily a šum

###### Dilatace

- Rozšiřuje světlé oblasti, spojuje objekty, vyplňuje dírky

###### Otevření a uzavření

- **Otevření:** eroze → dilatace (odstranění šumu)
- **Uzavření:** dilatace → eroze (vyplnění děr, spojení fragmentů)

###### Praktické příklady

- Odstranění šumu, spojení fragmentů, vyplnění děr, detekce tvarů, ztenčení objektů

