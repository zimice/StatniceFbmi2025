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

# 5. Operační systémy

## Metody měření zastoupení OS na trhu

- **Analytické odhady** (Gartner, IDC): Vyhodnocují data o prodejích, tržní statistiky a uživatelské průzkumy.
- **Reporty výrobců** (Microsoft, Apple, výrobci Android zařízení): Údaje o prodejích a instalované bázi.
- **Statistiky přístupu na web** (StatCounter, NetMarketShare): Zaznamenávají, jaké OS používají návštěvníci webových stránek.

## Nejpoužívanější OS

### Desktopové OS

**Windows** (nejčastěji Windows 10, 11)

**macOS** (pro počítače Apple)

**Linux** (různé distribuce, oblíbený pro servery i náročné uživatele)

### Mobilní OS

**Android** (nejrozšířenější pro telefony a tablety od různých výrobců)

**iOS** (pro zařízení Apple)

### Servery

**Linux** (dominuje v oblasti serverů, web hosting, databáze)

**Windows Server** (firemní prostředí s ekosystémem Microsoft)

**Unix** (AIX, HP-UX, Solaris)

### Embedded a real-time OS

**Specializované systémy** pro jednoúčelová zařízení (routery, IoT, průmyslové stroje).

Např. **FreeRTOS**, **VxWorks** apod.
  
  
  
  
  
  
  
  
  
  
  
  
  
## Definice OS a jeho cíle

**Operační systém (OS)** je systémový software, který spravuje hardwarové a softwarové prostředky počítače. Vytváří **abstrakci** pro aplikační programy (API) a **interface** pro uživatele.

**Cíle**:

- Umožňuje uživatelům komunikovat s počítačem prostřednictvím grafického uživatelského rozhraní (GUI) nebo rozhraní příkazového řádku (CLI).
- Přiděluje a spravuje hardwarové zdroje jako jsou procesor, paměť, úložná zařízení a vstupně-výstupní zařízení tak, aby se využívaly efektivně.
- Chrání systém před neoprávněným přístupem a zabezpečuje, aby chyby v jednom programu neovlivnily celý systém.
- Zjednodušuje vývoj softwaru tím, že poskytuje standardizované rozhraní na přístup k hardwaru.

## Komponenty počítačového systému

**Hardware**: CPU, paměť (RAM, HDD, SSD), I/O zařízení (klávesnice, myš, monitor).

**Operační systém (OS)**: Spravuje hardware, poskytuje služby.

**Aplikační programy**: Textové editory, prohlížeče, databáze atd.

**Uživatelé**: Lidé nebo systémy interagující s počítačem.

## Základní funkce OS

**Ovládání počítače**: Spouštění programů, zadávání vstupů, získávání výstupů.

**Abstrakce hardwaru**: Tvorba aplikačních rozhraní (API) pro ovládání zařízení a funkcí.

**Správa prostředků**: Přidělování a uvolňování paměti, CPU času, I/O.

**Zabezpečení systému**: Ochrana proti neoprávněnému přístupu, izolace procesů.

## Základní části OS

**Jádro (Kernel)**: Nejnižší úroveň OS, přistupuje přímo k hardwaru a řídí vše podstatné (správa paměti, procesů, ovladače).

**Systémové služby**: Vyšší úroveň než jádro (např. správa souborů, ověřování uživatelů).

**Pomocné nástroje**: Správce úloh, nástroje pro zálohování, aktualizace, diagnostiku atd.

## Typy OS

- **Single-tasking**: Spouští pouze jednu úlohu (např. starší DOS).
- **Multitasking**: Více procesů (Windows, Linux).
- **Single-user**: Jen jeden uživatel současně (dříve např. DOS).
- **Multi-user**: Více uživatelů sdílí systém (Unix).
- **Distribuované**: OS pro skupinu propojených počítačů (správa síťových zdrojů).
- **Embedded**: Specifické zařízení (routery, IoT).

## Evoluce OS

1. **Dávkové (Batch) systémy**: Zpracování úloh v dávkách (bez interakce uživatele).
2. **Multiprogramové systémy**: Paralelní spuštění více programů sdílením času CPU.
3. **Sdílení času (Time-Sharing)**: Interaktivní režim, více uživatelů připojených přes terminály.
4. **Desktopové a mobilní systémy**: OS pro osobní počítače, notebooky, smartphony.
5. **Cloud a virtualizace, kontejnery**: Trendy v moderním IT (flexibilní využití zdrojů).

## OS pro mainframe

- Typicky **IBM - z/OS**.
- Vysoká **spolehlivost, bezpečnost, škálovatelnost**.
- Používá se ve velkých organizacích (banky, vlády).

## Dávkové (batch) OS

- Zpracovávají velké úlohy bez interaktivního vstupu.
- **Výhody**: Efektivní využití CPU.
- **Nevýhody**: Žádná okamžitá interakce s uživatelem.

## Multiprogramové OS

- Současné vykonávání více programů sdílením času CPU.
- Vylepšuje využití zdrojů, protože CPU není nečinné při čekání na I/O.

## OS se sdílením procesorového času (Time-Sharing)

- Více uživatelů pracuje interaktivně na jednom počítači.
- **Unix** a některé verze **Windows NT** byly navrženy pro tento model.

## Desktopové OS

- Určené pro **osobní počítače a pracovní stanice**.
- Typicky **Windows, macOS, různé Linux distribuce**.
- Zaměření na uživatelské rozhraní a širokou škálu aplikací.

## Jádro OS a jeho funkce

- Zajišťuje základní systémové funkce:
    1. Správa paměti (alokace, paging, segmentace).
    2. Plánování procesů (který proces poběží, kdy se přepne).
    3. Správa I/O (disky, síť, tiskárny).
    4. Komunikace mezi procesy (IPC).
  
  
  
  

## Architektury jádra

Architektura jádra určuje, jak jsou základní komponenty operačního systému organizovány a jak spolu komunikují. Jádro je nejdůležitější část operačního systému: zajišťuje správu paměti, procesů, souborů, ovladačů zařízení a komunikaci s hardwarem.

Rozlišujeme tři hlavní typy architektury jádra:

### 1. Monolitické jádro

- **Charakteristika:**
    
    Všechny základní služby OS (správa paměti, procesů, souborový systém, ovladače) běží **společně ve stejném adresovém prostoru jádra**.
    
- **Výhody:**
    - **Vysoký výkon** – přímé volání funkcí bez nutnosti přepínání kontextu mezi procesy.
    - Všechny služby jsou vzájemně rychle dostupné.
- **Nevýhody:**
    - **Nižší stabilita a bezpečnost** – chyba v jednom modulu (např. ovladači) může shodit celý systém.
    - Změny nebo aktualizace modulů často vyžadují restart systému.
- **Typické použití:**
    - Používá se například v operačním systému **Linux** (většina distribucí), starší verze Unixu.

### 2. Mikrojádro

- Do jádra je zahrnuto **jen minimum funkcí** – nejčastěji správa paměti, plánování procesů a komunikace mezi procesy (IPC).
    
    Ostatní služby (např. ovladače zařízení, souborové systémy) jsou přesunuty do **uživatelského prostoru** a běží jako samostatné procesy.
    
- **Výhody:**
    - **Vyšší stabilita a bezpečnost** – pád nebo chyba služby v uživatelském prostoru neohrozí celé jádro.
    - Snadnější aktualizace a modularita, menší jádro je jednodušší na testování a správu.
- **Nevýhody:**
    - **Nižší výkon** – nutnost častého přepínání mezi jádrem a uživatelskými procesy (vyšší režie při komunikaci).
- **Typické použití:**
    - Mikrojádra se používají například v systémech **MINIX**, QNX, nebo některé verze macOS (XNU má mikrojádrové jádro Mach).

### 3. Hybridní jádro

- **Charakteristika:**
    
    Kombinuje vlastnosti **monolitického i mikrojádra** – některé služby běží v jádře, jiné v uživatelském prostoru.
    
    Snaží se spojit **výkon** monolitického jádra s **modularitou a bezpečností** mikrojádra.
    
- **Výhody:**
    - Může nabídnout **vyšší výkon** než čisté mikrojádro a zároveň větší stabilitu/modularitu než čistě monolitické jádro.
- **Nevýhody:**
    - Pokud není dobře navržené, může nést nevýhody obou přístupů – např. složitost nebo vyšší riziko chyb.
- **Typické použití:**
    - Používá jej například **Windows NT** (a tedy i všechny moderní Windows), nebo macOS (kombinuje Mach mikrojádro a BSD subsystém).

## Kritická chyba jádra operačního systému

Kritická chyba jádra (kernel panic v Linuxu, BSOD ve Windows) je situace, kdy selže jádro OS. Způsobuje pád systému a vyžaduje obvykle restart. Nejčastějšími příčinami jsou chyby ovladačů, poškození paměti nebo hardwaru.

## Proces v OS

- **Proces**: Instanci běžícího programu se svým vlastním adresním prostorem.
- Má **programový kód**, data a **stav** (registr, program counter).

## Stavy procesů a jejich přechody

Proces během svého života přechází mezi několika stavy:

- Nový (new): vytváří se.
- Připravený (ready): čeká na přidělení CPU.
- Běžící (running): právě vykonává instrukce na CPU.
- Čekající (waiting): čeká na I/O nebo událost.
- Ukončený (terminated): proces skončil a jeho prostředky jsou uvolněny.

## Vlákno vs. proces

- **Proces**: Má vlastní adresní prostor, prostředky (files, paměť).
- **Vlákno**: „Lehčí“ jednotka; vlákna se dělí o paměť procesu.
- Rychlejší **přepínání kontextu** u vláken než mezi procesy.

## Přepínání kontextu

- Uložení stavu (registrů, PC, paměťových map) aktuálního procesu a načtení stavu jiného procesu/vlákna.
- Umožňuje **multitasking** a sdílení CPU.

## Multitasking

- Schopnost operačního systému provozovat více úloh současně. Rozlišujeme:
- **Preemptivní multitasking**: OS může proces kdykoli přerušit (Windows, Linux).
- **Kooperativní multitasking**: Proces předává řízení sám (starší macOS).

## Plánování procesu

- **Algoritmy**: FCFS, SJF, Round Robin, prioritní plánování.
- Určuje **pořadí** a **alokaci CPU** pro procesy (kdo poběží jako první, jak dlouho).

## Přerušení (interrupt)

- Signál pro CPU, že nastala nějaká událost (I/O, timer, software).
- **Hardwarová přerušení**: např. klávesnice, síťová karta.
- **Softwarová přerušení**: system call, výjimky.

## Privilegovaný režim

- Režim pro **jádro OS** s neomezeným přístupem k hardwaru.
- Aplikace běží v **uživatelském režimu**, aby neohrozily chod systému.

## **Paralelní vs. distribuované OS**

- **Paralelní** – více procesorů sdílí jednu paměť (SMP).
- **Distribuovaný** – více počítačů propojených sítí, sdílení zdrojů.

## **Multiprocessing**

- Více procesorů nebo jader vykonává úlohy současně.
- **Symetrický (SMP)** – všechny CPU rovnocenné.
- **Asymetrický (AMP)** – hlavní CPU řídí ostatní.

## **Multicore procesory a hyperthreading**

- **Multicore** – více jader v jednom fyzickém CPU, každý může běžet paralelně.
- **Hyperthreading** (Intel) – každé jádro zpracovává více vláken najednou.

## **Základní operace Task Manageru v OS Windows**

- Monitorování výkonu (CPU, RAM, disk, síť).
- Správa procesů (ukončení, změna priority).
- Zobrazení a správa služeb (services).

## **Služby (Windows Service)**

- Programy běžící na pozadí (např. DHCP Client, Windows Update).
- Mohou se spouštět automaticky po startu systému nebo manuálně.

## Kybernetická bezpečnost a mechanismy zabezpečení OS

Kybernetická bezpečnost zahrnuje ochranu OS proti útokům, virům, malwaru.

Základními mechanismy jsou:

- Antivir, firewall, řízení uživatelských účtů.
- Pravidelné aktualizace a záplaty.
- Dodržování bezpečnostních zásad (hesla, šifrování).

## **Trusted Platform Module (TPM)**

- Kryptografický čip pro bezpečné uložení klíčů.
- Podpora šifrování disku (BitLocker), bezpečného bootování.

## **Implementace bezpečnostních mechanismů v OS Windows**

- Windows Hello (biometrika, PIN).
- BitLocker (šifrování disku).
- Windows Defender Firewall (síťová ochrana).
- Windows Defender (antivirus).
- Event Log (audit přihlášení a událostí).

## **Virtualizace hardware a OS**

- Spouštění více virtuálních strojů na jednom fyzickém serveru.
- Efektivní využití zdrojů, snadná správa, izolace jednotlivých VM.
- Hypervizor (Type 1 nebo Type 2) řídí virtuální stroje.

## **Hypervizor**

- **Typ 1** – běží přímo na hardwaru (např. Hyper-V, VMware ESXi).
- **Typ 2** – běží nad hostitelským OS (VirtualBox, VMware Workstation).

## **Nested virtualizace**

- Možnost spustit virtuální stroj uvnitř dalšího virtuálního stroje.
- Důležité pro testování a komplexní vývojové prostředí.

## **Virtualizační komponenty v OS Windows**

- **Hyper-V** – nativní hypervizor, dostupný ve vyšších edicích Windows.
- **Windows Subsystem for Linux (WSL)** – umožňuje spouštění aplikací Linuxu.
- **Windows Sandbox** – bezpečné izolované prostředí pro testování.
  
  
  
  
  
## **Windows Subsystem for Linux**

- Umožňuje provozovat linuxové distribuce na Windows.
- Překládá linuxové volání jádra do prostředí Windows, není to plná virtuální mašina.

## **Nejrozšířenější virtualizační platformy pro OS**

- Hyper-V (Microsoft)
- VirtualBox (Oracle)
- VMware (Workstation, ESXi)
- KVM (Linux)

## **Windows Sandbox**

- Lehká virtualizace pro otestování nedůvěryhodných aplikací.
- Při zavření se prostředí resetuje do původního stavu.

## **Modernizace monolitických aplikací**

- Přechod k mikroslužbám pro lepší škálovatelnost a flexibilitu.
- DevOps přístupy (CI/CD), rychlejší nasazování verzí.

## **Kontejnery**

- Odlehčená virtualizace na úrovni operačního systému.
- Docker, Kubernetes – nejznámější platformy.
- Rychlé nasazení, izolace, snadné přesouvání aplikací.

## **Typy perzistentních úložišť**

- Souborové systémy (lokální disky).
- Blokové úložiště (SAN).
- Objektové úložiště (Amazon S3).

## **Souborový systém**

- Způsob organizace a ukládání dat na disku.
- Podpora žurnálování, šifrování, přístupových práv, verzování.

## **Uspořádání dat na HDD a SSD**

- HDD – magnetické plotny, sekvenční čtení/zápis, pomalejší vyhledávání.
- SSD – paměť NAND flash, žádné pohyblivé části, rychlý náhodný přístup.

## SAN vs. NAS

- **SAN (Storage Area Network)** je vysokorychlostní síť spojující bloková úložiště se servery, vhodná pro velké podnikové aplikace.
- **NAS (Network Attached Storage)** je zařízení poskytující sdílený přístup k souborům přes síť, vhodné pro domácnosti a menší firmy.

## FAT, exFAT, NTFS, ReFS, EXT a Apple souborové systémy

- **FAT**: Jednoduchý FS, omezená velikost, vhodný pro starší média.
- **exFAT**: Vylepšený FAT, podporuje větší soubory, populární u flash disků.
- **NTFS**: Pokročilý FS pro Windows s podporou šifrování, žurnálování, přístupových práv.
- **ReFS**: Odolný proti chybám, pro servery a velká datová úložiště.
- **EXT2/EXT3**: Linuxové FS, EXT3 s žurnálováním.
- **Apple**: HFS+ (starší), APFS (moderní, podpora šifrování, snímků).

## Fragmentace souborového systému

Fragmentace znamená rozdělení souborů do více nesouvislých částí, což zpomaluje čtení na HDD. Defragmentace je proces, který uspořádá soubory do souvislých bloků.

## Atributy souborů v OS Windows vs. oprávnění souborů v POSIX

- **Windows**: Atributy jako Read-only, Hidden, System, plus Access Control List (ACL) pro detailní nastavení práv.
- **POSIX**: Práva na čtení, zápis a spuštění pro uživatele, skupinu a ostatní, spravovaná pomocí příkazů chmod a chown.

## Access Control List (ACL)

ACL je seznam přesně definovaných oprávnění pro soubor nebo adresář, umožňuje granularitu přístupových práv pro konkrétní uživatele nebo skupiny, využíván jak v systémech Windows, tak v POSIX.

## Správa uživatelských účtů v OS Windows

Správa uživatelů zahrnuje vytváření, mazání účtů, správu hesel a oprávnění. Nástroje jako User Account Control (UAC) zvyšují bezpečnost omezením práv běžných uživatelů, Microsoft Management Console (MMC) umožňuje pokročilou správu účtů a skupin.