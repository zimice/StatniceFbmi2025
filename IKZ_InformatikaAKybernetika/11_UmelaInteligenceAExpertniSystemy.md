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

# 11. Umělá inteligence a expertní systémy

## Stav, stavový prostor a prohledávání stavového prostoru

**Stav** v kontextu umělé inteligence reprezentuje aktuální konfiguraci systému, obvykle jako vektor hodnot, které popisují určitou situaci nebo systém v daném čase. 

**Stavový prostor** je množina všech možných stavů, do kterých se může systém dostat v rámci řešení určitého problému. V mnoha úlohách AI je cílem najít cestu (tj. posloupnost akcí) z počátečního stavu do jednoho z cílových stavů.

### Prohledávání stavového prostoru

Pro řešení problémů ve stavovém prostoru se využívají algoritmy prohledávání, které lze rozdělit na **neinformované** (slepé) a **informované** (heuristické) metody podle toho, zda využívají nějaké znalosti o cíli nebo prostředí.

### Neinformované metody

**Prohledávání do šířky (BFS)**: Tento algoritmus prozkoumává nejprve všechny možné přechody ze současného stavu (vrstvy), než se posune hlouběji. Zajišťuje nalezení nejkratší cesty (s minimálním počtem kroků), ale je náročný na paměť.

**Prohledávání do hloubky (DFS)**: Postupuje vždy co nejdále v aktuální větvi, teprve po jejím vyčerpání se vrací zpět a zkouší jiné větve. Výhodou je nízká paměťová náročnost, nevýhodou riziko uvíznutí v nekonečné větvi.

### Informované metody

**Gradientní algoritmy (hill climbing, gradient descent):** Využívají znalosti o tvaru cílové funkce, vždy postupují ve směru největšího zlepšení (gradientu). Jsou užitečné při optimalizaci, například při učení neuronových sítí.

**Metoda větví a mezí (Branch and Bound):** Kombinuje systematické rozdělování problému na menší části (větve) a používá mezí (hranice), aby eliminovala cesty, které nemohou vést k optimálnímu řešení.

**A* algoritmus:** Heuristický algoritmus, který hledá optimální cestu podle hodnotící funkce f(n) = g(n) + h(n), kde g(n) je aktuální cena cesty a h(n) je heuristický odhad nákladů do cíle. Najde optimální řešení, pokud je heuristika „admisibilní“ (nepřeceňuje skutečné náklady).
  
  
  
## Strojové učení: základní pojmy, příznakové a strukturální metody, regrese, klasifikace, shlukování

Strojové učení je disciplína, která umožňuje počítačům učit se ze zkušenosti (dat) bez explicitního naprogramování pravidel. Základní rozdělení metod je podle typu vstupních dat a cíle úlohy.

### Příznakové a strukturální metody

**Příznakové metody** pracují s daty, která lze vyjádřit jako vektory příznaků (číselné hodnoty, kategorie) – typické například pro tabulková data.

**Strukturální metody** využívají komplexnější struktury dat, jako jsou grafy, stromy, sekvence či texty, a pracují i s vnitřními vztahy v těchto datech.

### Regrese

**Regrese** je úloha, při které předpovídáme spojitou číselnou hodnotu na základě vstupních dat. Nejznámější je **lineární regrese**, která předpokládá lineární vztah mezi vstupy a výstupy. Cílem je najít takovou funkci, která co nejlépe vystihuje závislost mezi proměnnými.

### Klasifikace

**Klasifikace** rozděluje objekty do diskrétních tříd na základě jejich příznaků. Hlavní metody:

- **k-NN (k nejbližších sousedů):** Objekt je zařazen do třídy, která je nejčastější mezi jeho k nejbližšími sousedy v trénovací množině.
- **Rozhodovací stromy:** Stromová struktura, kde vnitřní uzly reprezentují podmínky na hodnotu příznaků, větve možné hodnoty a listy konečné třídy. Výhodou je přehlednost, rychlost a odolnost k chybějícím hodnotám.
- **Naivní Bayesovský klasifikátor:** Pravděpodobnostní model, který předpokládá nezávislost příznaků a pomocí Bayesovy věty přiřazuje pravděpodobnost třídám.

### Učení bez učitele (shlukování, clustering)

Učení bez učitele nevyužívá předem známé třídy. **Shlukování (clustering)** sdružuje objekty do skupin (shluků) podle jejich vzájemné podobnosti. Například **k-means** rozděluje data do k skupin tak, aby vzdálenost mezi body a středem skupiny byla minimální.
  
  
  
  
  
  
  
  
  
  
  
  
## Neuronové sítě: model neuronu, vícevrstvý perceptron (MLP)

**Neuronové sítě** jsou matematické modely inspirované fungováním biologických mozků, skládající se ze vzájemně propojených umělých neuronů.

### Matematický model neuronu

Umělý neuron přijímá několik vstupů x₁, x₂, …, každý vynásobí vahou w₁, w₂, …, výsledný součet sečte s biasem b a aplikuje aktivační funkci f. Výstup neuronu je:

y = f(Σ(wᵢ·xᵢ) + b)

Typické aktivační funkce:

- **Sigmoid:** f(x) = 1 / (1 + e^(-x))
- **ReLU:** f(x) = max(0, x)

### Vícevrstvý perceptron (MLP)

**MLP** je síť s minimálně jednou skrytou vrstvou neuronů mezi vstupní a výstupní vrstvou. Každý neuron v jedné vrstvě je propojen se všemi neurony ve vrstvě následující (plně propojená síť). MLP lze použít jak pro klasifikaci, tak pro regresi a učí se pomocí algoritmu **backpropagation** – zpětného šíření chyby, který postupně upravuje váhy, aby minimalizoval chybu na trénovacích datech.

## Expertní systémy: složky, báze znalostí, báze pravidel, inferenční mechanismus

**Expertní systémy** jsou programy, které napodobují rozhodování odborníka v určité oblasti pomocí znalostní báze a inferenčního mechanismu. Cílem je řešit úlohy, které by jinak vyžadovaly zkušeného specialistu (diagnóza, plánování, interpretace apod.).

### Složky expertního systému

**Báze znalostí:** Obsahuje fakta, pravidla a heuristiky potřebné k rozhodování.

**Fakta:** Objektivní informace o problému.

**Pravidla:** IF-THEN podmínky (například "Pokud má pacient teplotu > 37,5 °C, pak má horečku").

**Heuristiky:** Zkušenostní postupy a rady, které nejsou přesně formalizované.

**Báze pravidel:** Formálně zapsaná rozhodovací pravidla; podmnožina báze znalostí.

**Inferenční mechanismus:** "Mozek" systému, který na základě faktů a pravidel vyvozuje závěry (dopředné/zpětné řetězení, řešení konfliktů mezi pravidly).

**Vysvětlovací modul:** Umožňuje uživateli zjistit, jak a proč systém k závěru došel.

**Komunikační modul:** Rozhraní pro komunikaci s uživatelem.

## Tvorba expertního systému a získávání znalostí od experta

Tvorba expertního systému je komplexní proces zahrnující:

1. **Analýzu problému:** Identifikace oblasti a typů úloh, pro které má být systém navržen.
2. **Specifikaci systému:** Definice požadavků, architektury a použitých technologií.
3. **Získávání znalostí:** Klíčová fáze, kdy znalostní inženýr sbírá znalosti od expertů pomocí rozhovorů, introspekce, pozorování, simulací nebo strukturovaných metod (například třídění karet, Repertory Grid, Matrix Analysis).
4. **Vývoj báze znalostí:** Získané znalosti se převádějí do formálního zápisu, často ve formě IF-THEN pravidel.
5. **Implementaci systému:** Kódování pravidel a logiky, vývoj uživatelského rozhraní.
6. **Testování a ladění:** Ověřování správnosti a efektivity systému, úpravy na základě zpětné vazby.
7. **Údržbu a aktualizaci:** Průběžná aktualizace báze znalostí podle nových poznatků.

Kvalita a úspěšnost expertního systému do značné míry závisí na efektivním získání a formalizaci znalostí od lidského experta.