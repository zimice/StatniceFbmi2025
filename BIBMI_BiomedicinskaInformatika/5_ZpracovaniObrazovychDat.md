# Zpracování obrazových dat

## Zrakový orgán, jasová a kontrastní citlivost oka

Lidské oko je smyslový orgán, který umožňuje vnímání světla a barev. Hlavními částmi oka jsou rohovka, čočka, sítnice a zrakový nerv. Na sítnici jsou fotoreceptory: **tyčinky** (zajišťují vidění za šera, nerozeznávají barvy) a **čípky** (zajišťují barevné vidění a ostrost). 

1. **Rohovka**
2. **Přední komora**
3. **Vlastní čočka**
4. **Sklivec**
5. **Sítnice**

![Anatomie oka](https://prod-files-secure.s3.us-west-2.amazonaws.com/ee12890e-52c6-4cd6-ab27-fac900210de5/5a35bcce-e079-433a-89f5-c29153602484/Untitled.png)

**Jasová citlivost oka** popisuje schopnost oka detekovat různé úrovně osvětlení, nejcitlivější je při středním jasu. Tento fenomén je důležitý pro kalibraci obrazových zařízení a pro design osvětlení tak, aby odpovídal lidskému vnímání.

**Kontrastní citlivost oka** vyjadřuje schopnost rozlišit objekty s různou úrovní jasu – maximální je při středních prostorových frekvencích a klesá při extrémně nízkých či vysokých frekvencích. Tato citlivost není konstantní přes celé viditelné spektrum a závisí na různých faktorech, včetně úrovně osvětlení a vzdálenosti objektu.

## Prostorová a časová rozlišovací schopnost oka

**Prostorová rozlišovací schopnost oka** znamená schopnost rozlišit jemné detaily a blízké objekty v obraze, což je dáno hustotou fotoreceptorů (zejména v oblasti makuly).  
**Časová rozlišovací schopnost** popisuje, jak rychle dokáže oko zachytit změny v čase – lidské oko dokáže vnímat plynulý pohyb při cca 24 snímcích za sekundu a vyšších rychlostech (televize, video).

## Obecné schéma procesu zobrazení

Proces zobrazení zahrnuje několik kroků:

1. **Snímání obrazu** – světlo ze scény je zachyceno snímačem (kamerou, skenerem).
2. **Digitalizace** – převod analogového signálu na digitální (pomocí vzorkování a kvantizace).
3. **Zpracování obrazu** – různé algoritmy zlepšují kvalitu, detekují objekty či analyzují obraz.
4. **Zobrazení** – výsledek je vizualizován na monitoru či jiném zařízení.

![Schéma procesu zobrazení](https://prod-files-secure.s3.us-west-2.amazonaws.com/ee12890e-52c6-4cd6-ab27-fac900210de5/9d9652c6-ccb7-4998-9863-50e4c6b9d3fa/Untitled.png)

## Sběr obrazových dat, vzorkování a kvantizace

Sběr obrazových dat je proces, jehož cílem je převést vizuální scénu do formy, kterou lze dále zpracovávat počítačem. Začíná to snímáním obrazu pomocí zařízení jako jsou kamery, skenery nebo čidla. Výsledkem může být buď analogový obraz (spojitý signál), nebo digitální obraz (diskrétní mřížka pixelů).

Efektivní sběr obrazových dat závisí na kvalitě optiky, vlastnostech použitého senzoru (např. CCD, CMOS), kvalitě osvětlení a stabilizaci obrazu. Důležitou roli hraje i následné zpracování signálu.

### Co je to pixel?

**Pixel** (zkratka z *picture element*) je základní jednotka digitálního obrazu. Každý pixel představuje malou část obrazu a nese informaci o barvě a/nebo jasu v daném místě.

### Vzorkování (Sampling Rate)

Vzorkování je první krok při převodu analogového obrazu na digitální. Znamená to, že v pravidelných intervalech „odebíráme vzorky“ hodnoty intenzity světla nebo barvy po celé ploše obrazu.  
Podle Shannonova teorému je nutné vzorkovat alespoň dvojnásobkem nejvyšší frekvence detailu v obraze, aby nedocházelo ke zkreslení (aliasingu).

### Kvantizace (Quantization)

Po vzorkování následuje kvantizace – převod spojitých hodnot jasů nebo barev na omezený počet diskrétních úrovní, např. 256 odstínů šedi při 8 bitech na pixel.

### Artefakty při vzorkování a kvantizaci

- **Nedostatečné vzorkování** způsobuje **aliasing** – vznik falešných vzorů, „klikaté“ okraje, ztráta detailů.
- **Hrubá kvantizace** způsobuje **pásmování** (banding) – místo plynulých přechodů jsou vidět skoky mezi odstíny.

## Základní úlohy zpracování obrazu

### 1. Zlepšení kvality obrazu (image enhancement)

Cílem je **vylepšit vizuální vlastnosti obrazu**:

- **Odstranění šumu** (průměrování, mediánová filtrace)
- **Úprava kontrastu a jasu** (ekvalizace histogramu, gamma korekce)
- **Zaostření (ostření hran)** (zvýraznění hran a detailů)

### 2. Segmentace a extrakce objektů

- **Segmentace**: rozdělení obrazu na oblasti/objekty se společnými vlastnostmi
- **Extrakce objektů**: oddělení objektů od pozadí (např. prahování, detekce hran, region-growing, k-means, watershed)

### 3. Komprese obrazu (image compression)

- **Bezeztrátová komprese** (PNG, GIF, RLE, Huffman)
- **Ztrátová komprese** (JPEG)
- Komprese je nutná pro ukládání, přenos videa, práci v omezeném úložišti

### 4. Rozpoznávání vzorů (pattern recognition)

- **Automatická identifikace objektů, tvarů či struktur**
- Metody: šablonování, detekce hran, extrakce příznaků, strojové učení, deep learning

## Lineární systémy, impulzní odezva, prostorová invariance

### Lineární systém

Splňuje principy **superpozice** (součet vstupů → součet výstupů) a **homogenity** (násobení vstupu konstantou → výstup násoben konstantou).  
Základ většiny matematických operací při zpracování signálů a obrazů.

### Impulzní odezva

Výstup systému na **Diracův impulz** (teoretický bodový podnět).  
Umožňuje předpovědět chování systému pro jakýkoliv vstup.

### Prostorová invariance

Systém je **prostorově invariantní**, pokud jeho chování je stejné kdekoliv v obraze – umožňuje efektivní aplikaci operací (konvoluce) v celém obraze.

## Konvoluce a Korelace

### Konvoluce

- Filtr (kernel) „klouže“ po obraze, v každé pozici vypočítá vážený součet pixelů a filtru.
- Při konvoluci se filtr otáčí kolem středu na obou osách.
- Použití: rozmazání, ostření, detekce hran.

### Korelace

- Podobné konvoluci, ale filtr se **neotáčí**.
- Použití: detekce vzorů, měření podobnosti.
- Pro symetrické filtry je výsledek shodný.

## Princip barevného zobrazení, barevné modely

- **RGB:** Aditivní model (monitory, kamery)
- **CMY(K):** Subtraktivní (tisk)
- **HSV/HLS:** Odstín, sytost, světlost
- **Barevná hloubka:** Počet barev v obraze, běžně 24 bitů (True Color)

## Snímací režimy

- **Čárová grafika:** pouze čáry
- **Polotóny:** simulace odstínů pomocí teček (tisk)
- **Šedotónový režim:** různé úrovně šedi
- **Barevné režimy:** informace o barvě v každém pixelu

## Bodové, lokální a globální operace nad obrazem

- **Bodové operace:** mění každý pixel samostatně (jas)
- **Lokální operace:** používají okolí pixelu (filtrace, vyhlazení)
- **Globální operace:** působí na celý obraz (ekvalizace histogramu)

## Prahování a adaptivní prahování

- **Prahování:** segmentace na základě prahu (objekt vs. pozadí)
- **Adaptivní prahování:** různé prahy v různých částech obrazu

## Úprava kontrastu, ekvalizace histogramu

- **Úprava kontrastu:** zvýraznění rozdílů světlé/tmavé
- **Ekvalizace histogramu:** rozložení jasových hodnot, zvýraznění detailů

## Logaritmický a exponenciální operátor

- **Logaritmická transformace:** zvýraznění tmavých oblastí, stlačení světlých
- **Exponenciální operace:** zvýraznění světlých oblastí

## Vyhlazovací filtry, zaostření, mediánová filtrace

- **Vyhlazovací filtry:** průměrovací, gaussovské – rozmazání, odstranění šumu
- **Zaostřovací filtry:** zvýraznění detailů, ostrosti
- **Mediánová filtrace:** nahrazuje pixel mediánem okolí, odstranění „sůl a pepř“ šumu

## Fourierova transformace, filtrace ve frekvenční oblasti, DCT

### Fourierova transformace (DFT)

- Převod obrazu do frekvenční domény (analýza složek, kde je šum, kde detaily)
- **Nízké frekvence:** velké oblasti, plynulé přechody
- **Vysoké frekvence:** detaily, hrany, šum

### Filtrace ve frekvenční oblasti

- Dolní propust: vyhlazení, odstranění šumu
- Horní propust: zvýraznění hran, detailů
- Postup: DFT → filtr → inverzní DFT

### DCT

- Kosinová transformace (JPEG komprese, bloky 8x8 pixelů)
- Efektivní pro kompresi a potlačení detailů, které oko nevnímá

## Detekce hran, segmentace, Houghova transformace

- **Detekce hran:** Sobel, Prewitt, Canny
- **Segmentace:** rozdělení obrazu na oblasti s podobnými vlastnostmi
- **Houghova transformace:** detekce přímek, kružnic

## Metody komprese obrazu

- **Jednoduché metody:** RLE
- **Statistické:** Huffman
- **Slovníkové:** LZW
- **Transformační:** JPEG, DCT, wavelet

## Matematická morfologie (eroze, dilatace, otevření, uzavření)

### Základní princip

- Práce s geometrickými strukturami v obrazu pomocí **strukturního elementu**

### Eroze

- Zmenšuje světlé oblasti, odstraňuje malé detaily a šum

### Dilatace

- Rozšiřuje světlé oblasti, spojuje objekty, vyplňuje dírky

### Otevření a uzavření

- **Otevření:** eroze → dilatace (odstranění šumu)
- **Uzavření:** dilatace → eroze (vyplnění děr, spojení fragmentů)

### Praktické příklady

- Odstranění šumu, spojení fragmentů, vyplnění děr, detekce tvarů, ztenčení objektů
