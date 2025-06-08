# Modelování a simulace

**Modelování** je proces vytváření zjednodušeného obrazu reálného systému s cílem jej lépe pochopit, analyzovat nebo předvídat jeho chování.

**Simulace** je metoda, jak tento model použít k předpovědi vývoje systému v čase – tedy k testování hypotéz, analýze scénářů nebo podpoře rozhodování v situacích, kde není možné nebo vhodné zkoumat reálný systém přímo. Modelování a simulace jsou široce využívány ve vědě, technice, ekonomii i medicíně.

## Spojité a diskrétní modely

**Spojité modely** popisují systémy, jejichž stav se mění plynule v čase, obvykle pomocí diferenciálních rovnic. Typicky se používají pro fyzikální, chemické či biologické procesy, kde jsou veličiny, jako je koncentrace nebo rychlost, spojité.

- **Příklad:** Elektrické obvody, proudění tekutin, růst populace v čase bez skokových změn.
- **Výhoda:** Umožňují přesný popis kontinuálních jevů.
- **Nevýhoda:** Analytické řešení může být složité nebo nemožné, často je nutné použít numerické simulace.

**Diskrétní modely** pracují se systémy, jejichž stav se mění v oddělených časových okamžicích (v krocích) nebo v důsledku jednotlivých událostí. Stav systému je popsán diskrétními hodnotami (např. počet jedinců, vozidel, zákazníků).

- **Příklad:** Simulace dopravy, front v obchodě, modely populační dynamiky s diskrétními generacemi.
- **Výhoda:** Přirozeně popisují systémy, kde změny nastávají v určitých bodech (např. narození, úmrtí).
- **Nevýhoda:** Hůře se s nimi popisují procesy, které jsou ve skutečnosti spojité.

## Pozorování a experiment

**Pozorování** znamená sledování a zaznamenávání chování systému v jeho přirozeném prostředí bez aktivního zásahu do jeho chodu. Umožňuje pochopit základní vlastnosti systému a často slouží jako podklad pro návrh modelu.

- **Příklad:** Sledování migrace zvířat ve volné přírodě, monitorování vývoje nemocnosti v populaci.

**Experiment** spočívá v aktivním zásahu do systému, kdy výzkumník mění jednu nebo více proměnných a sleduje, jak tyto změny ovlivní chování systému. Experimenty lze provádět v laboratoři nebo v simulovaném prostředí.

- **Příklad:** Testování účinku nové léčivé látky na skupinu pacientů, měření účinku různých opatření na šíření infekce.

## Metodika vytváření modelu a způsoby popisu modelů

**Metodika vytváření modelu** je strukturovaný proces, který zahrnuje několik kroků:

1. **Definice problému:** Jasně stanovit, co chceme modelem zkoumat a jaký je cíl modelování.
2. **Sběr a analýza dat:** Získání informací o reálném systému.
3. **Formulace konceptuálního modelu:** Návrh základní struktury modelu, vztahů mezi proměnnými a procesy.
4. **Matematická formulace:** Vyjádření modelu pomocí rovnic, grafů či algoritmů.
5. **Implementace modelu:** Realizace modelu ve formě počítačového programu či simulačního prostředí.
6. **Validace a verifikace:** Ověření, zda model odpovídá reálnému systému a správně počítá.
7. **Analýza a interpretace výsledků:** Použití modelu k odpovědi na původní otázky nebo k optimalizaci systému.

**Způsoby popisu modelů** zahrnují:

- **Matematické modely:** Rovnice, algoritmy, statistické vztahy.
- **Grafické modely:** Schémata, diagramy toků, grafy závislostí.
- **Simulační modely:** Algoritmy, které opakovaně simulují běh systému v čase.
- **Symbolické dynamické popisy:** Například pomocí Petriho sítí nebo stavových diagramů.

## Kompartmentové modely

Kompartmentové modely jsou specifickým typem matematických modelů používaných k popisu dynamiky systému rozdělených do diskrétních částí (kompartmentů).

Přenosy mezi kompartmenty představují tok sledované veličiny mezi kompartmenty.

Model může rovněž může obsahovat vnější příjem (injekce) a výstupy (vylučování).

## Příklady použití kompartmentových modelů v biologii a medicíně

**Kompartmentové modely** jsou hojně používány v:

- **Epidemiologii:** Popis šíření infekčních onemocnění (např. model SIR rozděluje populaci na náchylné, infikované a uzdravené).
- **Farmakokinetice:** Sledování pohybu léčiva v těle, např. dvoukompartmentový model (centrální a periferní kompartment).
- **Ekologii:** Modelování migrace jedinců mezi různými oblastmi nebo populačních změn v závislosti na přechodech mezi stádiemi života.

## Spojité a diskrétní modely jednodruhových populací, Malthusův model, model kooperace a kompetice

### Spojité modely jednodruhových populací

Nejjednodušší je **Malthusův model**, kde velikost populace roste exponenciálně:

$\frac{dN}{dt} = rN$

kde $N$ je počet jedinců, $r$ je míra růstu. Tento model však nerespektuje omezené zdroje.

**Logistický model** zavádí omezenou nosnou kapacitu prostředí:

$\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$

kde $K$ je maximální možná velikost populace.

### Diskrétní modely jednodruhových populací

U druhů s diskrétními generacemi (např. hmyz s roční generací) se používají rekurentní rovnice:

$N_{t+1} = rN_t$

nebo obdobné modifikace včetně logistické regulace.

### Modely kooperace a kompetice

- **Kooperace:** Jednotlivci spolupracují, což může vést ke zvýšení míry přežití a růstu populace.
- **Kompetice:** Jedinci nebo druhy soupeří o omezené zdroje, což omezuje růst populace.

## Modely dvoudruhových populací

Dvoudruhové modely se zaměřují na interakci mezi dvěma různými populacemi, například konkurence o zdroj nebo vztah dravec–kořist.

- **Model konkurence:** Oba druhy soupeří o stejný omezený zdroj. Model je rozšířením logistické rovnice a zahrnuje vzájemné ovlivňování růstu obou populací.

## Model dravec–kořist (model Lotky–Volterry)

Model Lotky–Volterry je klasickým příkladem nelineárního systému dvou diferenciálních rovnic pro vztah dravců a kořisti:

$\frac{dN}{dt} = rN - aNP$ 

$\frac{dP}{dt} = baNP - mP$

kde $N$ je počet kořisti, $P$ počet dravců, $r$ je růst kořisti, $a$ je míra predace, $b$ je účinnost využití kořisti, $m$ je úmrtnost dravců.

Model zachycuje cyklické výkyvy obou populací – když je mnoho kořisti, roste počet dravců, což vede k poklesu kořisti, následně i dravců, což umožní obnovu kořisti atd.

## Epidemiologické modely

**Epidemiologické modely** popisují, jak se infekční nemoc šíří v populaci. Nejčastěji rozdělují populaci do skupin (tzv. „kompartmentů“) a sledují, jak mezi nimi nemoc přechází.

### Model SIR (Kermack–McKendrickův model)

**SIR model** dělí populaci na tři skupiny:

- **S (Susceptible, náchylní)** – zdraví lidé, kteří se mohou nakazit
- **I (Infected, nakažení)** – aktuálně nemocní, kteří mohou šířit nemoc
- **R (Recovered, uzdravení)** – lidé, kteří se uzdravili a jsou imunní

**Přechody:**

Z náchylných (S) se po setkání s nakaženým (I) mohou stát nakažení. Z nakažených (I) se po čase stávají uzdravení (R).

**Typické použití:** Šíření chřipky nebo jiných nemocí s imunitou po uzdravení.

### Další varianty epidemiologických modelů

**SI model:**

Lidé jsou buď náchylní (S), nebo nakažení (I). Jakmile se jednou nakazí, zůstávají nakažení navždy (např. u některých chronických infekcí).

**SIS model:**

Nakažený člověk se může uzdravit a stát se znovu náchylným, tj. po uzdravení není imunní, ale může se opakovaně nakazit. (Typické pro nemoci bez trvalé imunity, např. některé bakteriální infekce.)

**SIR s přenašeči:**

Do modelu je přidána skupina „přenašeči“ (např. komáři u malárie), kteří nemoc šíří, ale sami nejsou nemocní.

**SIR s vakcinací:**

Přidává účinek očkování – očkovaní lidé přecházejí rovnou do skupiny imunních (R), takže se nemohou nakazit ani nemoc šířit.

## Modely farmakokinetiky a dávkování léčiv

**Farmakokinetika** zkoumá, co se děje s lékem v těle – jak rychle a kam se rozptyluje, jak je odbouráván a vylučován.

### Základní modely

**Jednokompartementový model:**

Představuje tělo jako jeden „kompartment“ (prostředí), ve kterém se lék rychle a rovnoměrně rozptýlí.

Po podání dávky koncentrace léku v těle klesá postupně v důsledku odbourávání (např. v játrech) a vylučování (močí).

**Použití:** Jednoduché léky s rychlou distribucí (některá antibiotika).

**Dvoukompartementový model:**

Tělo je rozděleno na „centrální kompartment“ (např. krevní oběh) a „periferní kompartment“ (tkáně).

Lék se nejprve dostane do krve, odkud se postupně dostává do tkání, a pak se z těla odbourává a vylučuje.

**Použití:** Léky, které se v těle šíří pomaleji nebo mají tendenci se ukládat v určitých tkáních (např. některá anestetika).

**Proč modely potřebujeme?**

Pomáhají určit optimální dávkování léku – kdy a kolik léku podat, aby byl účinný, ale neškodil (například zabránění předávkování nebo naopak nedostatečnému účinku).
