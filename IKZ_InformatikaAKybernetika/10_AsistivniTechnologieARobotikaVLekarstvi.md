---
author: "Šimon Kochánek"
date: "28/6/2025"
output: pdf_document
fontsize: 10.5pt
---

<style type="text/css">
  body{
    font-size: 10.5pt;
  }
</style>

# 10. Asistivní technologie a robotika v lékařství

## Kinematika – základní pojmy a stavba robotických mechanismů

**Kinematická dvojice** je základní stavební jednotka mechanického systému – dvě tělesa jsou spojena tak, že mezi nimi může docházet k přesně definovanému relativnímu pohybu. Dělí se na:

- **Rotační dvojici** (kloub): umožňuje vzájemnou rotaci (např. loket).
- **Translační dvojici**: umožňuje vzájemný lineární pohyb (např. posuvné vedení).

**Kinematický řetězec** je uspořádání několika kinematických dvojic za sebou:

- **Otevřený kinematický řetězec** má nespojené konce (např. lidská paže).
- **Uzavřený kinematický řetězec** má konce spojené (např. nůžkový zvedák).

**Stupně volnosti** (Degrees of Freedom, DOF) vyjadřují, kolik nezávislých pohybů může systém vykonávat – například volná částice v prostoru má 3 DOF (pohyby podle x, y, z).

**Strukturní schéma** zobrazuje, jak jsou komponenty propojeny, zatímco **kinematické schéma** upřesňuje typy kinematických dvojic a počet stupňů volnosti celého mechanismu.

## Kinematika robotů v homogenní souřadné soustavě

Kinematika robotů popisuje pohyb robotů (změny polohy a orientace) bez ohledu na působící síly.

Pro popis pohybu v prostoru se používají **homogenní transformace** a **transformační matice**.

- **Homogenní transformační matice** (4×4) umožňuje reprezentovat současně rotaci i translaci v 3D prostoru a velmi snadno skládat více dílčích transformací do výsledného pohybu.
- Základní pohyby robota jsou rotace kolem os x, y, z a posuvy podél těchto os.
- **Poloha bodu** je pak reprezentována homogenním vektorem (včetně „projektivní“ souřadnice pro snadné operace).

**Rychlostní kinematika** využívá **jakobiánovou matici** (Jacobian), která převádí rychlosti v kloubech na rychlost koncového efektoru (pracovní části robota). Analogicky lze pomocí derivace Jakobiánu získat i zrychlení bodu.
  
  
  
  
  
  
  
## Přímá a inverzní kinematika, matice pohybu

- **Přímá kinematika**: Na základě zadaných kloubových parametrů (úhlů, posuvů) vypočítá polohu a orientaci koncového efektoru robota pomocí sekvenčního násobení transformačních matic.
- **Inverzní kinematika**: Naopak určuje potřebné hodnoty kloubových parametrů, aby koncový efektor dosáhl požadované polohy/orientace.
    
    Řešení je často iterativní, protože rovnice jsou nelineární. Pro řešení se používají např. Newtonovy metody nebo pseudo-inverze Jakobiánu.
    

**Matice inverzního pohybu** slouží k převodu souřadnic z koncového efektoru zpět do základního rámce, nebo obecně pro „zpětnou transformaci“ při skládání pohybů.

Poloha, rychlost a zrychlení koncového bodu vůči rámu a ostatním tělesům se určují právě transformacemi a aplikací Jakobiánu a jeho derivací. Správné určení těchto hodnot je zásadní pro řízení pohybu i interakci robota s prostředím.

## Výpočet Jakobiánu a jeho využití

**Jakobián** je matice, která vyjadřuje vztah mezi rychlostmi v kloubech robota a rychlostí koncového efektoru v prostoru. Má translační a rotační část (podle typu kloubu).

Při řešení inverzní kinematiky (nalezení kloubových úhlů pro dosažení požadované polohy) hraje klíčovou roli – umožňuje dopočítávat malé změny v úhlech podle aktuální chyby v poloze efektoru.

## Dynamika otevřených kinematických řetězců

Dynamika zkoumá síly a momenty působící na jednotlivé části robotického mechanismu v pohybu.

Pro přesné modelování je třeba znát **rozložení hmotnosti** a setrvačné vlastnosti každého článku (členu řetězce).

**Potenciální energie** je dána polohou článků vůči gravitačnímu poli, **kinetická energie** rychlostí a rotačním pohybem článků.

**Lagrangeovy rovnice II. druhu** umožňují odvodit pohybové rovnice systému ze znalosti jeho energie (potenciální i kinetické), aniž by bylo nutné explicitně počítat všechny síly a momenty v kloubech.

Výsledkem jsou dynamické rovnice v maticovém tvaru:

**D(q)·q¨ + C(q, q˙)·q˙ + G(q) = τ**,

kde:

- D(q) je matice momentů setrvačnosti,
- C(q, q˙) je matice odstředivých a Coriolisových sil,
- G(q) je matice gravitačních sil,
- τ je vektor kloubových momentů (akčních zásahů),
- q jsou vektory kloubových úhlů (nebo posuvů).

## Paradigmata silového řízení otevřených řetězců, Matlab simulace

**Silové řízení** znamená, že robot aktivně kontroluje sílu nebo moment působící na okolní prostředí, což je klíčové např. při manipulaci s křehkými předměty.

**Impedanční řízení** – robot reaguje „pružně“ na kontakt, umožňuje změnit trajektorii, když narazí na překážku, čímž snižuje riziko poškození.

**Admitanční řízení** – robot aktivně upravuje svou polohu podle vnější síly (například víko krabice je zavíráno s definovanou silou).

Tyto strategie lze ověřovat v simulačním prostředí **Matlab/Simulink** – simuluje se model robota, navrhují a ladí se řídicí algoritmy, analyzují se výsledky.

## Využití senzorů a aktuátorů v rozhraní člověk-stroj

Robotické systémy využívají **senzory** (například snímače síly, momentu, polohy, tlaku) k získávání zpětné vazby o stavu robota i okolí.

**Aktuátory** (motory, hydraulika, pneumatika) provádějí pohyb na základě pokynů řídicího systému.

### Předzpracování a využití signálů

Signály z uživatelských zařízení je potřeba:

- **Filtrování signálu** – odstranění šumu a artefaktů pro zvýšení spolehlivosti detekce vstupů.
- **Normalizace** – převedení hodnot do vhodného rozsahu pro další zpracování.

Tyto principy se používají například pro:

- Řízení pohybu invalidního vozíku (joystick, detekce síly, hlasové pokyny)
- Ovládání polohovatelného lůžka (snímače, ovladače, bezpečnostní prvky)
- Ovládání počítačové myši bez použití rukou (kamerové nebo EEG snímače)
- Ovládání externí robotické ruky (např. pomocí pohybových snímačů na jiných částech těla)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
## Využití embedded systémů

**Embedded systémy** jsou malé, specializované počítače navržené k plnění jednoho nebo omezeného okruhu úkolů.

Používají se pro:

- Zpracování senzorických dat
- Real-time řízení robotických mechanismů
- Implementaci ovládacích algoritmů
- Spolehlivý provoz v prostředí s omezenými zdroji

Programování a algoritmizace embedded systémů je často silně optimalizovaná na rychlost, odezvu a energetickou nenáročnost.

## Alternativní komunikační systémy pro hendikepované

Cílem je umožnit komunikaci a ovládání zařízení osobám s omezenou schopností pohybu nebo řeči.

Příklady technologií:

- **Text-to-speech** – převod psaného textu na mluvenou řeč (např. komunikátory pro osoby bez hlasu).
- **Brain-computer interface (BCI)** – rozhraní snímající mozkovou aktivitu (EEG), která je převedena na ovládací signály pro počítače, invalidní vozíky nebo jiné pomůcky.
- Ovládání pohybu zařízení pomocí zbytkových pohybů, pohybu očí, dechu nebo jiných bio-signálů.

Alternativní komunikační a asistenční systémy významně zvyšují kvalitu života hendikepovaných osob tím, že rozšiřují jejich možnosti samostatného ovládání prostředí a komunikace s okolím.