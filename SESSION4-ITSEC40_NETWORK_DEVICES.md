

## 1. ROUTERS

Typicky je ROUTER zariadenie prideľujúce IP adresy a preto je na 3 sieťovej vrstve

Pokiaľ riešime malú sieť SOHO (SMALL OFFICE \ HOME OFFICE) približne do 10 zariadení tak si vystačíme s obyčajným routrom s WiFi alebo bez. 

Typicky takýto router obsahuje:
1. 4x RJ45 porty LAN
2. 1x RJ45 port WAN
3. DHCP server
4. DNS server pre LAN
5. Wifi s rôznymi bezpečnostnými protokolmi WEP, WPA1 až WPA3, WPS a pod.
6. Firewall rôznej kvality.
7. Autonómna sieť pre Hostí GUEST NETWORK
8. DMZ Demilitarizovaná zóna

Pri výbere zohľadňujeme okrem rýchlosti, množstva ENDPOINTOV a premávky Trafficu aj softvérový základ. 
OpenWRT je routerová verzia odľahčeného Linuxu a je OPEN SOURCE.
Kvalita a frekvencia UPDATOV A PATCHOV

SINGLE POINT OF FAILURE

## 2. SWITCHES AND HUBS

2.1  ACCESS LAYER

HUB je LEGACY zariadenie = SEN KAŽDÉHO HACKERA
Typicky je SWITCH zariadenie rozdeľujúce PACKETY na Layer 2 

2.2 DISTRIBUTION LAYER 

MULTI LAYER SWITCH a Layer 3 Switche
Su manazovatelne switche s webovym rozhranim a ssh, ktore mozno nakonfigurovat na zrkadlenie portov, pokrocile smerovanie a pod. Su ovela drahsie a vykonnejsie ako klasicke switche.


2.3 CORE LAYER

SUPER SWITCHE Tbps


## 3. DYNAMIC FIREWALLS

V Session4 sme nastavovali softvérový firewall v počítači. Okrem tohto Firewallu aj Router väčšinou obsahuje nejakú formu Firewallu rôznej kvality. Pre serióznu ochranu siete však budeme potrebovať špecializovaný sieťový komponent, ktorý zvládne odfiltrovať veľkú časť škodlivého kódu a pozná množstvo hrozieb z internetu. 

Množstvo výrobcov vyrába takéto SECURITY zariadenia pod rôznymi názvami ZyWall, SonicWall, Turris, pfSense, Fortinet, Juniper ... Tieto firewally okrem schopnosti kontrolovať aj obrovské množstvo sieťovej prevádzky majú jednu spoločnú vlastnosť.

Dynamicky menia RULES podľa najnovších známych hrozieb a za týmto procesom je práca množstva ITSEC špecialistov. Väčšina korporátnych Firewallov preto vyžaduje ročný poplatok za tento servis. Zaplatiť ho je podmienkou vysokej ochrany, ktorú zariadenie sieti poskytuje. 

V našich zemepisných šírkach máme k dispozícií Firewall vyvíjaný ako OPEN SOURCE v ČR firmou TURRIS. Jej Firewally sa vyznačujú prijateľnou cenou  a bez ročných poplatkov. Firewall sa upgraduje niekoľkokrát za deň a poskytuje množstvo užitočných informácií pre IT SEC. 


 ![ ](.jpeg)

## 4. VPN (VIRTUAL PRIVATE NETWORK)

Najpoužívanejším softvérovým riešením pripojenia cez VPN do našej lokálnej siete je OpenVPN. Budeme potrebovať.

4.1 ABY NAS INTERNET POZNAL >

DDNS - Dynamicka DNS
alebo verejna staticka IP

4.2 SPOJIT VPNserver s externymi klientami

1. Vygenerovať certifikáty a kryptografické kľúče.
2. Aktivovať OpenVPN server na našom routri.
3. Nahrať kľúče a nastavenie na cieľový počítač.
4. Stiahnuť a aktivovať OpenVPN klienta na ENDPOINTE z ktorého sa chceme prihlasovať do počítača. 

OpenVPN nám poskytne šifrované pripojenie do našej LAN s možnosťou využívania pripájania sa na lokálne servery a služby. 

POZOR OpenVPN aj napriek tomu, že rieši bezpečnosť prenosu nesie so sebou množstvo iných bezpečnostných problémov. Napríklad možnosť zneužitia prístupu z ENDPOINTU, ktorý nemáme plne pod kontrolou. 

ZERO CONFIG VPN - TAILSCALE, ZEROTIER

INE RIESENIA: CLOUDFLARE TUNNEL, ZyXEL NEBULA

ZERO TRUST RIESENIE - TWINGATE

> [!warning] 
> POZOR - NESPRAVNA KONFIGURACIA SERVERA ALEBO NEDOSTATOCNA OCHRANA KLIENTA MOZE OHROZIT CELU LAN.
> 
>ZERO TRUST NETWORKS - NEDOVERUJ NIKOMU

DNS uniky dns zaznamov
WebRTC uniky IP adries
IPv6 uniky IP adries
VPN protokol zranitelnosti

NSA ExtraBacon Exploit cez SNMP protocol


>[! info] 
>Vzdy zvazuj CLOUDOVE RIESENIE, ktore znizuje naklady na zelezo, bezpecnost a zalohovanie.



## 5. KVM SWITCH

Keyboard Video Mouse - zariadenie pre ovládanie väčšieho počtu Headless Serverov cez jednu klávesnicu, myš a displej.

## 6. SERVER ANATOMIA

Každý počítač sa môže stať serverom no nie každý počítač je stavaný ako server.

Server je špeciálny počítač poksytujúci svoje služby klientom 24 \ 7 za každých okolností a počasia. Od klasického PC sa líši

2x a viac 1Gbps RJ45 NIC
Vysoký výpočntový výkon procesora Intel Xeon, AMD Opteron, AMD Epyc a pod
Viac pamäťových slotov RAM
RAID radič pre viacero supervýkonných diskov
HOTSWAP vyberanie diskov za chodu servera
Redundantné napájanie viacero zdrojov
IPMI, iDRAC, ILO systém na diaľkový manažment a monitorovanie prevádzky.

>[! warning] 
>!!!POZOR FYZICKA BEZPECNOST, server treba fyzicky skontrolovat a poznat jeho presny obsah, zapecatit skrinku proti neopravnenemu vniknutiu !!!

>[!info] PREVADZKA SERVERA STOJI NEMALE PENIAZE - VZDY BY STE JEHO NAKUP A OPODSTATNENIE MALI ZVAZIT


### 7. WIFI Wireless 802.11x

#### 7.1 FREKVENCIE A POCET KANALOV
2.4GHz a 5 GHz

#### 7.2 RYCHLOSTI:
802.11b - 11Mbps
802.11g - 54Mbps
802.11n az 600Mgps {5GHz pasmo}
802.11ac - WIFI5 az 3.46Gbps
802.11ax - WIFI 6 az 9.6Gbps cez cviacero kanalov
802.11be WIFI7 az teoretickych 46Gbps

#### 7.3 PRVA VYSTRAHA - IDENTITA
Vsetky MAC Adresy vo vzduchu
SIGINT - Signalne spravodajstvo

#### 7.4 DRUHA VYSTRAHA - VERBOZITA
Nepoznate moju siet ? SOm doma? Som v hoteli ?

#### 7.3 TRETIA VYSTRAHA -RYCHLY ALGORITMUS - SLABE SIFROVANIE
Problem s kryptom

Zranitelnosti v WPA2
WPS PIN prihlasovanie pomocou PINu

#### 7.4 POSLEDNA VYSTRAHA - ZLE DVOJCA

Zle dvojca je kopia wifi routeru na ktory sa prihlasuju klienti


#### 7.1 DOSAH A RYCHLOST SU PROBLEM

RADIUS LOGIN SCHEME

PAP Password Authentification Protocol
CHAP Challenge Handshake Authentification protocol


#### 7.2 RADIUS SERVER (Remote Authentification Dial-In User Service)

<li>Authentification</li>
<li>Authorization</li>
<li>Accounting</li>




