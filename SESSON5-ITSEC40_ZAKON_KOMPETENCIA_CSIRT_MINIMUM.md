# ZAKON_KOMPETENCIA_CSIRT_MINIMUM

1. ZAKON: 
[Kybernetická bezpečnosť -NBU (gov.sk)](https://www.nbu.gov.sk/urad/pravne-predpisy/pravne-predpisy/kyberneticka-bezpecnost/index.html)

2. VYHLASKY  NBU:
[165/2018 Z.z. - Vyhláška Národného bezpečnostného ú... - SLOV-LEX](https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/2018/165/#paragraf-2.odsek-2)
[362/2018 Z.z. - Vyhláška Národného bezpečnostného ú... - SLOV-LEX](https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/2018/362/20190101)

>[!warning] 
>ZAKONY TREBA DODRZIAVAT !!! AJ KED NIE SU DOKONALE A ICH SPLNENIE MOZE BYT TECHNICKY, PERSONALNE AJ MATERIALNE NAROCNE. 
 

3. ZAKON URCUJE POVINNOSTI :
<li>POSKYTOVATELOM ZAKLADNYCH SLUZIEB (KRITICKA INFRASTRUKTURA, OBLASTI DOPRAVA, BANKY...)</li>

<li>POSKYTOVATELOM DIGITALNYCH SLUZIEB</li>

<li>A - ma viac ako 50 zamestnancov</li>
<li>B - ma obrat alebo rocnu bilanciu 10.000.000,00 EUR</li>

poskytuje:
A. ONLINE TRHOVISKO 
B. INTERNETOVY VYHLADAVAC
C. CLOUD COMPUTING

>[!warning]
>TO ZE ZAKON  PRIAMO NEURCUJE POVINNOST VASEJ ORGANIZACII ALEBO FIRME NEZNAMENA, ZE NA VASEJ SIETI BUDE NEPORIADOK A NEBUDETE MAT PLAN KYBERNETICKEJ OCHRANY !!!!

4. CYBER SECURITY INCIDENT RESPONSE TEAM
[CSIRT.SK | Vládny CSIRT | Governmental CSIRT](https://www.csirt.gov.sk/index.html)

Vyplati sa sledovat tuto stranku kvoli novym zranitelnostiam a odporucaniam

SCANY VEREJNYCH IP ADRIES A DOMEN:
[Registrácia Achilles | CSIRT.SK (gov.sk)](https://www.csirt.gov.sk/registracia-achilles.html?csrt=2754219148926585670)


1. NAHLASOVANIE INCIDENTOV
2. NAHLASOVANIE ZRANITELNOSTI



## MINIMUM REQUIREMENTS

## A. INTERNA LEGISLATIVA A CHAIN OF COMMAND

a) organizácie kybernetickej bezpečnosti a informačnej bezpečnosti,  DELEGOVANIA A KOMPETENCIE INA
b) riadenia rizík kybernetickej bezpečnosti a informačnej bezpečnosti,  DELEGOVANIE A KOMPETENCIE INA
c) personálnej bezpečnosti,  HR A IT
d) riadenia prístupov,  AJ FYZICKYCH AJ ELEKTRONICKYCH
e) riadenia kybernetickej bezpečnosti a informačnej bezpečnosti vo vzťahoch s tretími stranami,  PRAVNE A IT
f) bezpečnosti pri prevádzke informačných systémov a sietí,   IT SEC
g) hodnotenia zraniteľností a bezpečnostných aktualizácií,  IT SEC
h) ochrany proti škodlivému kódu,  SYSADMIN DEVOPS
i) sieťovej a komunikačnej bezpečnosti, SYSADMIN
j) akvizície, vývoja a údržby informačných sietí a informačných systémov,  DEV, DEVOPS, SYSADMIN
k) zaznamenávania udalostí a monitorovania,  IT SEC
l) fyzickej bezpečnosti a bezpečnosti prostredia,  IT SEC
m) riešenia kybernetických bezpečnostných incidentov,  IT
n) kryptografických opatrení,  KLUCE A CERTIFIKATY, HESLA
o) kontinuity prevádzky, ADMINls -
p) auditu, riadenia súladu a kontrolných činností.

(4) Bezpečnostné opatrenia musia zahŕňať najmenej MINIMUM
a) určenie manažéra kybernetickej bezpečnosti, ktorý je pri návrhu, prijímaní a presadzovaní   
bezpečnostných opatrení nezávislý od štruktúry riadenia prevádzky a vývoja služieb
informačných technológií a ktorý spĺňa znalostné štandardy pre výkon roly manažéra
kybernetickej bezpečnosti, SKUSKA NBU -- 

>[! warning] VYTIAHNE SERVER ZO ZASUVKY - NAJHORSI VARIANT PRE MANAZERA (NIEKEDY TO NAOPAK USETRI CAS A SIRENIE MALWARE)

MANAZER KYBERNETICKEJ BEZPECNOSTI RIESI: 
b) detekciu kybernetických bezpečnostných incidentov,  
c) evidenciu kybernetických bezpečnostných incidentov,
d) postupy riešenia a riešenie kybernetických bezpečnostných incidentov,
e) určenie kontaktnej osoby pre prijímanie a evidenciu hlásení,  SKUTOCNE DOLEZITY BOD
f) pripojenie do komunikačného systému pre hlásenie a riešenie kybe



## B. IMPLEMENTACIA HW A SW RIESENI

#### B.1 MONITOROVANIE ZRANITELNOSTI

> [!warning]
> BUDTE PODOZRIEVAVI !!! KLADTE OTAZKY !!! GREP HARDER !!!

Technické zraniteľnosti informačných systémov ako celku sa identifikujú prostredníctvom :

a) nástroja určeného na detegovanie existujúcich zraniteľností programových prostriedkov a ich
častí,   AV, NMAP, NESSUS
b) nástroja určeného na detegovanie existujúcich zraniteľností technických prostriedkov a ich častí, HARDWARE DIAGNOSTICS - [[SESSION1_HARDWARE_DEVICES_AND_DIAGNOSTICS-ITSEC40]]
c) využitia verejných a výrobcom poskytovaných zoznamov, ktoré opisujú zraniteľnosti
programových a technických prostriedkov.  DOKUMENTACIA

## C. SIETE MINIMALNE POZIADAVKY

#### C.1. PRISTUPOVE PRAVA UZIVATELOV PERMISSIONS

> [! warning] VZDY MINIMALNE POTREBNE !

Linux Permissions UGO - RWX GROUPS - NASTAVENIE MAX PERMISSIONS PRE VSETKYCH

``` bash
chmod 777 SUBOR
chmod ugo+rwx SUBOR
```

GROUPS limituje Device, pristupy do DB 
 
#### C.2. SEGMENTACIA SIETE --- DMZ a ZONY BEZPECNOSTI
{prostredníctvom riadenia bezpečného prístupu medzi vonkajšími a vnútornými sieťami
a informačnými systémami, a to najmä využitím nástrojov na ochranu integrity sietí
a informačných systémov, ktoré sú zabezpečené segmentáciou sietí a informačných systémov;
servery so službami priamo prístupnými z externých sietí sa nachádzajú v samostatných
sieťových segmentoch a v rovnakom segmente musia byť len servery s rovnakými
bezpečnostnými požiadavkami a rovnakej bezpečnostnej triedy a s podobným účelom,}
[[SESSION3_NETWORK_LAYERS_AND_PROTOCOLS-ITSEC40]]

#### C.3. PREPOJENIA SEGMENTOV CHRANENYCH FIREWALLMI S PRINCIPOM NAJNIZSICH PRIVILEGII
{tým, že prepojenia medzi segmentmi a externými sieťami, ktoré sú chránené firewallom
a všetky spojenia sú povoľované na princípe zásady najnižších privilégií,}
[[SESSION4-ITSEC40_NETWORK_DEVICES]]


#### C.4. VPN a dvojfaktorova autentifikacia pre mobilne pripojenie



#### C.5. ZABLOKOVANE PORTY S PRESNE SPECIFIKOVANYM PRISTUPOM IS
{tým, že sieťam alebo informačným systémom sú umožnené len špecifikované služby
umiestnené vo vyhradených segmentoch siete počítačovej siete,}
[[SESSION3_NETWORK_LAYERS_AND_PROTOCOLS-ITSEC40]]

#### C.6. PRIPOJENIE NA EXTERNU SIET IBA CEZ FIREWALL A IDS  INTRUSION DETECTION SYSTEM / IPS 
[[SESSION5-INTRUSION DETECTION SYSTEM]]


#### C.7. PRIPOJENIE SERVEROV NA EXTERNU SIET Z DMZ PODLA ODPORUCANI VYROBCOV -- PRODUKCIA, 
Hlavne webservery, api, servery, ktore maju poskytovat informacie na internet a maju byt viditelne pre okolite prostredie ci uz statickou IP alebo Domenou

#### C.8. AKTUALIZOVANYM ZOZNAMOM VSTUPOV A VYSTUPOV BODOV DO A ZO SIETE
DOKUMENTACIA

#### C.9. MONITOROVANIE POKUSOV O VNIKNUTIE DO SIETE  - LOGOVANIE A ANALYZOVANIE
Okrem IDS je dolezite mat k dispozicii aj dalsie udaje, ktore mozu smerovat k odhaleniu a zachyteniu zacinajuceho alebo prebiehajuceho utoku
[[SESSION5-LOG MANAGEMENT]]

#### C.10. BLOKOVANIE SPOJENIA ZO ZNAMYCH ADRIES
Tuto funkciu nam zabezpeci Dynamicky Firewall na vstupe do siete.
[[SESSION4-ITSEC40_NETWORK_DEVICES]]


#### C.11. SPOJENIE APLIKACII MEDZI SEBOU IBA CEZ POVOLENE PORTY
Nastavenie Firewallov na Endpointoch a Serveroch... vsetko ostatne zakazat ak sa da :)
Vid ukazku komunikacie PC vo Wiresharku vystupny port si voli pocitac !
[[SESSION3_NETWORK_LAYERS_AND_PROTOCOLS-ITSEC40]]

#### C.12. DPI A ZAZNAM PACKETOV NA VSTUPE DO SIETE
DEEP PACKET INSPECTION JE VACSINOU FUNKCIA SECURITY APPLIANCE - Funkcia Firewallu alebo SUPERSWITCHA 
[[SESSION4-ITSEC40_NETWORK_DEVICES]]


#### C.13. IDS A IPS  INTRUSION DETECTION SYSTEM A INTRUSION PREVENSION SYSTEM
[[SESSION5-INTRUSION DETECTION SYSTEM]]
suricata, snort 

#### C.14. NA VYSTUPE FILTROVANIE PACKETOV
Pri IT bezpecnosti je dolezite nielen byt obozretny smerom do siete ale aj zo siete ! 
Pokusy o EXFILtraciu chranenych dokumentov a udajov mozu mat na svedomi nielen nezodpovedni uzivatelia, ale aj reverzne shelly, SPYWARE alebo MALWARE. 
<li>Kos na spinave pradlo</li>


#### C.15. 2FA na kazdy vzdialeny ADMIN pristup do siete  SSH, Admin konzoly

Je nebezpecne pri vzdialeno pristupe pouzivat admin hesla chranenej LAN. Vzdialeny pristup cez RDP alebo VPN treba obmedzit !!!


#### C.16 SCAN VULNERABILITIES

netlas, shodan, nmap, nessus, burp suite - webapp a webove servery
vykonávaním pravidelného alebo nepretržitého posudzovania technických zraniteľností, najmä
identifikácie možnej prítomnosti škodlivého kódu zariadenia, ktoré sa vzdialene pripája do
internej siete, alebo zmluvného zaručenia vrátane preukázania plnenia tejto povinnosti.

#### ZERO TRUST - UZIVATEL MA PRISTUP LEN K PRESNE DEFINOVANYM ZDROJOM - KAZDA SIETOVA AKTIVITA JE SKUMANA 


## D. FYZICKA BEZPECNOST

1. UMIESTNENIE SIETE - BEZPECNOSTNE ZAMKY A MANAZMENT KLUCOV A PRISTUPU
2. PRAVIDLA PRACE - ZONIFIKACIA PRACOVISKA, ODDELENIE SUKROMIA A PRACE
3. DODRZIAVANIE UCELU IT - ZARIADENIA SA NESMU POUZIVAT NA INE VECI
4. UPS  - ZALOZNE ZDROJE NA SIET A SERVERY
5. EVIDENCIA A OZNACENIE PROSTRIEDKOV -
6. VYMAZAVAVIE A LIKVIDACIA PROSTRIEDKOV - #DUMPSTERDIVING
7. FYZICKY PRENOS MIMO PRIESTOROV - PRAVIDLA
8. MANIPULACIA S DOKUMENTACIOU A PAMATOVYMI MEDIAMI - USKLADNENIE/LIKVIDACIA

?? dimenzovanie a fyzické parametre sietí a hardvéru, ktoré priamo alebo nepriamo ovplyvňujú
najväčšiu prípustnú dobu výpadku siete a informačného systému ??  ZALOZNA INFRASTRUKTURA - UPS, Nahradne servery


## E. PLANOVANIE REAKCIE
### E.1 PLANOVANIE A KRIZOVE PLANY

<li>krizove plany na najpravdepodobnejsie scenare</li> 
<li>reakcne doby</li> 

### E. 2 ZDROJE  A FINANCIE
<li>krizove plany na najpavdepodobnejsie scenare</li> 

### E.3 KOMUNIKACNY PLAN
<li>zvolavanie a pohotovost</li>
<li>komunikacne prostriedky a kanaly</li>
<li>externa pomoc</li>
<li>nahlasovanie incidentov</li> 

### E.5 CASOVY HARMONOGRAM NA OBNOVU FUNGOVANIA NA MINIMALNU FUNKCNOST
<li>obnovenie v krizovej minimalnej prevadzke s monitorovanim v HODINACH</li>

### E.6 CASOVY HARMONOGRAM NA OBNOVU A FUNGOVANIE NA NORMAL
<li>obnovenie v krizovej plnej prevadzke s monitorovanim v HODINACH</li> 

### E.7 TESTOVANIA A VYHODNOCOVANIA PLANOV OBNOVY S CIELOM VACSEJ EFEKTIVITY
<li>Vyhodnotenie INCIDENTU, FUNKCNOST PLANOV, CHYB A MOZNEHO ZLEPSENIA - CENA</li> 

## F. BACKUPY A DOKUMENTACIA

### F.1 V PRAVIDLACH
a) frekvenciu a rozsah jej dokumentovania a schvaľovania,
b) určenie osoby zodpovednej za zálohovanie, BACKUP MANAGER :)
c) časový interval, identifikáciu rozsahu údajov, dátového média zálohovania a požiadavku
zabezpečenia vedenia dokumentácie o zálohovaní,
d) požiadavku umiestnenia záloh v zabezpečenom prostredí s riadeným prístupom,
e) požiadavku zabezpečenia šifrovania záloh obsahujúcich aktíva klasifikačného stupňa chránené
a prísne chránené,
f) požiadavku na vykonávanie pravidelného preverenia záloh, testovanie obnovy záloh
a precvičovanie zavedených krízových plánov najmenej raz ročne

### F.2 OPTIMALNY MODEL OSOBNEHO ZALOHOVANIA:

3 kopie v roznych lokalitach  USB
2 na roznych mediach
1 kopia na Cloude (ZASIFROVANA) *  mimo lokacie

* podla internych predpisov a charakteru informacii v IS

### F.3 SYSTEM RYCHLEJ OBNOVY POMOCOU REPLIK A SNAPSHOTOV

[[SESSION5 - SYSTEM RYCHLEJ OBNOVY]]