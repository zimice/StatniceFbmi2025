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
