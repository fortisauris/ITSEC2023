
CIEM stands for Cybersecurity Incident and Event Management

# A. Incidenty, Prevencia a Opatrenia
#incidentresponse

1. PLAN (DEFINOVANE CSIRT, MENA, KOMPETENCIE, ZDROJE, NASTROJE, CASOVY HARMONOGRAM)

2. REALIZACIA OPATRENI
FAZA 1 -IDENTIFIKÁCIA INCIDENTU
FAZA 2 IZOLÁCIA INCIDENTU
FAZA 3 ANALÝZA DAT O INCIDENTE
FAZA 4 ODSTRÁNENIE NAKAZY
FAZA 5 OBNOVA SYSTEMU 
FAZA 6 POUČENIE, ANALYZA POSTUPOV PLANOV A CHYB


## A.1 DDOS - Distributed Denial of Services

>[!warning]
>IT SEC: Neustale monitorujte mnozstvo komunikacie na vonkajsich portoch serverov v DMZ !!!

>[!info] 
>HACKER:  Utok spociva v navyseni dopytu na server s mnozstva neznamych IP adries cim dochadza k pretazeniu servera a nestiha servovat odpovede. Pre beznych klientov bude Vas server nepristupny a sluzba prestane fungovat. Dlhodobe zatazenie moze sposobit aj dalsie technicke problemy. 

Utok ma dve podoby... jedna je rychlo posielat requesty na server a druha je zdrzovat TCP spojenie a poskytovanie poziadaviek



A.1.1 PREVENCIA

a. Preverte u ISP a poskytovatela hostingu, Cloudu a domeny moznosti tzv. MITIGACIE v pripade utoku. 

b. Pripravte WHITELIST kritickych odberatelov sluzieb

c. Prioritizujte stalych odberatelov

d. Pripravte moznosti presmerovat Traffic na ine zalozne servery a tym kratkodobo navysite kapacitu sluzby. 


UKÁŽKA	
``` bash
hping3 
```

### A.1.2 OPATRENIA

Ak spozorujete masivny nárast prichádzajúceho trafficu na port pokračujte podľa prichystaného plánu. Packety pôjdu z veľkého množstva IP adries a prvá a najväčšia línia obrany vznikne u Vaľeho IS, Webhostingu či  poskytovateľa Internetu alebo Cloud na ktorom beží Váš server. Platí, že čím väčší provider služby tým väčšie sú jeho možnosti Mitigácie a odrazenia útoku.

V tomto momente aktivujte Whitelisty svojich stálych a d§ležitých zákazníkov pre ktorích musíte servis udržať ONLINE.

Navýšte krátkoddobo kapacitu Vašeho servera čo sa týka jeho výkonu aj sieťových rozhraní.

Dokumentujte odkiaľ útok ide a skúste zistiť PREČO.

>[!info] PRIKLAD ANONYMOUS vs. SAUDSKÁ ARÁBIA
>


## A.2 - PHISHINGOVÁ KAMPAŇ

A.2.1 PREVENCIA

>[!info] 
>IT SEC: Cieľom Phishingovej kampaňe je aby užívateľ poskytol útočníkovi bud svoje prihlasovacie údaje k službe, alebo spustenie škodlivého kódu pomocou linku či súboru. 

a. Najefektívnejšou prevenciou je preškolenie USEROV a upozornenie ich na možnosti a ciele útočníkov. Čím je útok viac cielený bude aj náročnejšie odhaliť phishingový mail.

b. Ďalším preventívnym opatrením nepoužívanie Endpointov a Serverov v chránenej sieti na súkromné využitie. Tým sa vyrieši veľa problémov s falošnými prihlasovacími formulármi do Sociálnych sietí , Internetbankingu a pod.

c. Dobrý nápad je aj zakázanie preposielania typov súborov, ktoré môžu obsahovať škodlivý kód.
 
A.2.2 OPATRENIA

a. Preveriť koľko užívateľov dostalo takýto mail.  Kvalita toho Phishingu. Whaling

b. Vylúčiť možnosť, že na neho niekto klikol a to aj pohovorom aj kontrolou sieťovej prevádzky, logov a AV.

c. Identifikovať ZDROJ odkiaľ prišiel a zakázať ho na Firewalle alebo Filtroch.

d. Zachovať kópiu mailu a prílohy na forenzné skúmanie.

>[!warning] 
>ITSEC: AK SA ODHODLATE VYSKÚŠAŤ SVOJE SCHOPNOSTI A SKÚMAŤ ROB TO OPATRNE VO SVOJOM HACKLABE = NA ŠPECIÁLNE VYTVORENOM PC VO VM IZOLOVANOM SANDBOXE.

>[! demo]
>SET - SOCIAL ENGENEERING TOOLKIT - zrodenie Phishingoveho mailu.

 
## A.3 - MALWARE / RANSOMWARE infekcia

INFO: Cieľom hackera je získať prístup k informáciám, výpočtového výkonu, kryptomene či znehodnotiť dáta a vypýtať si odmenu za ich opätovné sprístupnenie. RANSOMWARE sa väčšinou prihlási po zašifrovaní dát a vypíta si odmenu. PENIAZE NIKOMU NEDÁVAJTE 

### A.3.1 PREVENCIA

a. BIOS Ochrana proti zapisu - pravdepodobnost mala ale treba najnovsi FIRMWARE

b. BROWSER na firemne veci(vypnuta Java, ActiveX a pod) a iny na sukromne

c. Virtualizacia aplikacii  

>[! demo]
>DOCKER  - SANDBOXING - kontajner s vlastnym VOLUME (diskom)


d. IDS, IPS, AV, Logy a všetko čo nám pomôže kedy a ako sa dostal Malware do siete a určí aj rozsah infekcie.

e. Systém rýchlej obnovy z BACKUPOV

>[!info]
>AK  STE BOLI NAPADNUTÝ RANSOMWARE  neklesajte na duchu - KAVALERIA JE UZ NA CESTE. Desiatky ľudí pracujú na tom aby Vaše dáta zachránili. Títo neviditeľní hrdinovia hľadajú cestičku ako prelomiť šifrovanie a väčšinou to chvíľu trvá. DISK OZNAČTE A ODLOŽTE DO SKRINE. O NEJAKÝ ČAS HO POMOCOU NEJAKÉHO NÁSTROJA ODŠIFRUJETE.


### A.3.2 OPATRENIA :


1. Identifikacia MALWARE a infikovanych HOSTOV

2. Izolacia IZOLACIA INFIKOVANEJ CASTI SIETE - zabranenie sirenia

>[ !toolbox ] 
>POUŽI NÁSTROJE: CONTENT FILTER, IPS na LAN, BLACKLIST, 
>vypnutie sluzieb, portov,
>odpojenie zo siete - COMMAND AND CONTROL

Sledovanie jeho komunikacie pomocou IDS - CUSTOM SIGNATURE

3. Dezinfekcia pomocou AV

4.  REINSTALACIA - Admin pristup, Manipulacia so systemovymi subormi, Backdoor, nestabilita, Pochybnosti

5. ANALYZA UCINNOSTI A PLANU

## A.4 - HACKER NA CHRANENEJ SIETI

FYZICKA VRSTVA - SNIFFING 
DATA LINK - SPOOFING
SIETOVA - MITM
TRANSPORTNA - RECON  (PRIESKUM)
SESSION - HIJACKING (UNOS)
PREZENTACNA - PHISHING
APLIKACNA - EXPLOITACIA

>[!info] PENETRACNE TESTY !!!
PRISTUP DO USERA>ZISKAJ ROOT PRAVA>PREHLADAJ>ZABETONUJ (ABY ZOSTAL TVOJ)

>[! warning] 
>AK CHCETE UROBIŤ PENETRAČNÉ TESTY MUSÍTE MAŤ PISOMNE POVOLENIE SO ŠPECIFIKÁCIOU TESTOV A ČASOVÝM OBDOBÍM KEDY BUDÚ VYKONANÉ!!!



PREVENCIA:

Vsetko co sme sa doposial ucili. 

1. neopravneny scan  - ids, pcap, logy

2. brute force attack - ids, pcap, logy  KODY /etc/passwd, /etc/shadow

3. neopravnena wifi - aircrack-ng


#### LINUX PYTHON SKRIPT NA VYPISANIE NAJDENYCH WIFI SIETI
```python
import subprocess

def scan_wifi():
    cmd = "nmcli dev wifi list"
    networks = subprocess.check_output(cmd, shell=True)
    networks = networks.decode("utf-8")
    return networks

print(scan_wifi())
```
SPUSTIME:
``` bash
spustime python3 wifi_scan_linux.py
```

LINUX BASH SKRIPT NA SKENOVANIE WIFI kazdych 300 sekund {5 minut} uklada do suboru
``` bash
#!/bin/bash

while true; do
    nmcli dev wifi list >> wifi_list.txt
    sleep 300
done
```

SPUSTIME NA POZADI:

``` bash
sh ./wifi_scan_bash.sh &
```

>[!info] 
>Uloha spustena na pozadi sa objavi v zozname procesov pomocou prikazov ```ps```, ```top``` alebo pomocou prikazu ```jobs```. <br><br> Do popredia ulohu dostaneme pomocou prikazu ```fg``` a ukoncime `Ctrl-c` alebo ju nechame `Ctrl-z`. <br><br>Ak mame PID mozeme proces ukoncit `kill PID`




4.neopravnene zariadenie na LAN - nmap
``` bash
nmap IP/24 > zoznam_zariadeni.scan  # scanuje subsiet 254 zariadeni
```


5. privilege escalation - logy

>[! warning ]
>HACKER: PRIVILEGE ESCALATION je technika pomocou ktorej utocnik ziskava vyssie PERMISSIONS a tym pristup k sluzbam a suboro. Cielom je samozrejme byt ROOT.  


OPATRENIA:

a. Identifikacia pocitacov kde bol hacker uspesne pripojeny

b. Izolacia siete a analyza aktivit hackera

c. Dezinfekcia a reinstalacia

>[!warning] 
>AK BOL HACKER NA POCITACI A NIE SME SI ISTY CO SA MU PODARILO A CO NIE... AK SA DA. SPRAVTE KOMPLET REINSTALACIU NA NOVY HDD ALEBO SDD {NAJLEPSIE ESTE ZABALENY} !!! <br>
>VYMONTOVANY HACKNUTY DISK ODLOZTE PRE POTREBY POLICIE A FORENZNEHO SKUMANIA !!!  OZNACTE HO AKO JED AJ S ID CISLOM POCITACA :)

## B. METASPLOIT FRAMEWORK- UKÁŽKA 

METASPLOIT je exploitačný framework obsahujúci tisíce možností ako sa nabúrať do Vašeho počítača. Jeho použitie zvládne aj začiatočník. Vie na diaľku využiť zraniteľnosť Vašeho počítača a získať do neho prístup. Vie vytvárať škodlivé kódy, ktoré na Vašom počítači vytvoria backdoory, reverzné shelly, získajú informácie či prístup do shellu. 

auxiliary = rozne nastroje ako scannery, 
exploit = vyuzitie zranitelnosti systemu na ziskanie kontroly alebo informacii
payload  = skodlivy kod ktory treba spustit u USERA
post- CITTE SA AKO DOMA
NOP = Maskovanie pred AV a IDS

``` metasploit

search windows
use module
show info
set RHOST
CMD: exploit, run, payload

sessions -l
sessions -i <CISLO>
background
```



msfvenom = softver na vytvaranie suborov infikovanych PAYLOADOM

meterpreter = VIAC AKO SSH SHELLt

>[! warning ]
>VYBRANE PRIKAZY METERPRETERU:
>keyscan_start = spustenie KeyLoggera, ktorý zaznamenáva všetky stlačené klávesy
>migrate PID = meterpreter sa schová do iného bežiaceho procesu
>screenshot = spraví screenshot obrazovky
>clearev - vymaže všetky zmienky o prítomnosti Hackera z logov. 


## C. KRYPTOGRAFIA

### C.1 Historické šifry
a.  Scytale 
b. Cézarova šifra a ROT13
c. Albertiho Sifrovaci disk 
d. Vernamova šifra

### C.2 ENIGMA - STROJ vs ČLOVEK

Enigma bola elektromechanický šifrovací stroj používaný na šifrovanie komunikácie medzi jednotkami Nacistického Nemecka. Problémom boli predovšetkým útoky nemeckých ponoriek v Atlantiku. 

Alan Turing a tým jeho kryptoanalytikov v Bletchley Park,  postavil prvý počítač, ktorý dokázal túto šifru prelomiť a čítať tieto správy. Operácia ULTRA bola prísne utajená.

### C.3 ADVANCED ENCRYPTION STANDARD

Elektromechanické šifry na báze rotorov slúžili až do 70tych rokov. Potom ich postupne nahrádzala počítačová kryptografia v podobe algoritmu DES a neskôr Triple DES. V 1997 roku NIST (National Institute of Standard and Technology) vypísala súťaž o nový šifrovací štandard. Do súťaže sa prihlásilo viacero kryptografických algoritmov. Vyhral algoritmus menom Rjijandel od Belgických autorov, druhý bol Serpent.

AES256 sa stalo štandardom šifrovania pre priemysel a ochranu utajovaných skutočností. 

V súčasnosti sa uvažuje už o novom štandarde šifrovania. Favoritom sa stáva algoritmus ChaCha.

### C.4 PRINCIPY MODERNÝCH ALGORITMOV
Moderné šifrovanie je založené na jednoduchých matematických a logických operáciach ako je XOR, posun bitov, miešanie matric a podobne. Tieto operácie sa opakujú niekoľkokrát aby ich nebolo možné bez kľúča prelomiť.

#### C.4.1   OPERACIA XOR A NAHODNE CISLA

Ukážeme si jednoduchú operáciu XOR v Pythone
``` python

import random   # NEPOUZIVAT NA KRYPTOGRAFIU !!! 


def apply_xor_operation(value : str, key : str):
    """
    Funkcia aplikuje vypocet bitwise XOR hodnoty a kluca hexadecimalne cislo 0x00 do 0xff v STRINGU.
    Vysledkom je hexadecimalne cislo od 00 do FF tj. 0 do 255.
    parameter::: value - STRING s hex cislom od 0x00 do 0xff
    parameter::: key - STRING s hex cislom od 0x00 do 0xff
    return ::: vysledok vypoctu - hex cislom od 0x00 do 0xff
    """
    value = eval(value)
    key = eval(key)
    return hex(value ^ key)  # tuto sa deju zazraky 


if __name__ == "__main__":
    value = hex(random.randint(0,255))
    key = hex(random.randint(0,255))
    print("VALUE : ", value, " KEY : ", key," RESULT : ",apply_xor_operation( value, key))
```

Aby moderné šifry správne fungovali a kľúče ktoré sa používajú sú tvorené z vygenerovaných náhodných čísel. Ak by čisla neboli dostatočne náhodné dal by sa vytvoriť vzorec a množstvo pravdepodobných kľúčov by sa nám podstatne zúžilo. Preto treba používať generátory pseudonáhodných čísel určené na kryptografiu a nie python modul `random` .


#### C.4.2 VYSOKÉ PRVOČÍSLA

Vysoké prvočísla majú v modernej kryptografii špecifickú úlohu. Ich vlastnosťou je, že sú všade rovnako vypočítateľné a pritom jedinečné. 

#### C.4.3 RYCHLE SIFROVANIE DATOVYCH STREAMOV

AES256 je algoritmus, ktorý môžeme použiť na šifrovanie súboru, disku USB kľúča, mailu a pod. Nie je však vhodný na šifrovanie obrovských streamov dát z jednej IP na druhú ako je VIDEO, ZVUK a pod. Napriek tomu potrebujeme tieto dáta ochrániť. Použijeme jednoduchšie a rýchlejšie formy šifrovania.

``` python
# PRINCIP SBOXU
sbox = [45, 12, 56,9,11,78,120,]
znak_na_zasifrovanie = 65 # ASCII HODNOTA A

def sbox_enc(sbox, znak_na_zasifrovanie)
	'''
	Funkcia SBOX prechadza SBOXOM a zakazdym hodnotu XORuje s dalsim cislom v SBOXE
	SBOXOV byva niekolko za sebou a operacii vela. Vysledkom je totalne
	modifikovana hodnota 65
	'''
	enc = znak_na_zasifrovanie # 
	for i in sbox:
		enc = enc ^ i
	print('VYSLEDOK JE: ', enc)
	# NA DESIFROVANIE STACI OTOCIT PORADIE SBOXU A PREHNAT HODNOTU NASPAT
	return enc

def jednoduchy_permutacny_box(hex_cislo):
	'''
	Hexadecimalna hodnota vstupuje do PERMABOXU nemodifikovana a podla nastavenej 
	modifikacie vychadza z PERMABOXU pozmenena. Opakovaniami v kombinacii s
	dalsimi operaciami mozno vstupnu hodnotu zmenit niekolkokrat. Funguje podobne
	 ako Enigma PLUGBOARD
	'''
	if hex_cislo == '0x0':
		return '0x5'
	if hex_cislo == '0x1':
		return '0xa'
	if hex_cislo == '0x2':
		return '0x3'
	if hex_cislo == '0x3':
		return '0xa'
	if hex_cislo == '0x4':
		return '0xf'
	else:
		return hex_cislo
	
if __name__ == "__main__":
	sbox_enc(sbox, znak_na_zasifrovanie)
	jednoduchy_permutacny_box('0x4')

```


#### C.4.4 ASYMETRICKÁ VÝMENA KĽÚČOV

Problém symetrického šifrovania je, že obe strany musia disponovať rovnakým kľúčom. TO je celkom technická výzva ako tento kľúč doručiť niekomu bez toho aby nemohlo dôjsť ke jeho kompromitácii. 

Asymetricke šífrovanie je postavené na pároch vygenerovaných kľúčov a pomocou zložitého matematického výpočtu si vedia počítače dohodnúť spoločný kľúč. Pomocou neho môžu prejsť na symetrické šifrovanie, ktoré je oveľa rýchlejšie.

PUBLIC = verejný kľúč môžete poslať hocikomu
PRIVATE = súkromný kľúč musíte chrániť ako oko v hlave.

``` python
# ASYMETRICKA VYMENA KLUCOV DIFFIE-HELLMAN

# ALICA
AlicineTajomstvo = 75433

# BOB
BoboTajomstvo = 56575

# Server
g = 5472437625635634658438583468564336543654365346546534 # nahodne vybrane cislo
n = 911 # prvocislo

# Alica ide poslat Bobovi kluc
A_posiela =(g ** AlicineTajomstvo) % n
print("ALICA POSIELA", A_posiela)
# Bob ide poslat kluc Alici
B_posiela = (g ** BoboTajomstvo) % n
print("BOB POSIELA", B_posiela)

# Alica otvara Bobov kluc
Bobov_kluc = (B_posiela ** AlicineTajomstvo) % n
print("Bobov zdielany kluc",Bobov_kluc)

# Bob otvara Alicin kluca
Alicin_Kluc = (A_posiela ** BoboTajomstvo) % n
print("Alicin Zdielany kluc",Alicin_Kluc)
```


#### C.4.5 BUDUCNOST


Moderné metódy šifrovanie strážia nielen naše tajomstvá, ale aj súkromie, biometrické dáta či zdravotné záznamy. V súčasnosti sme si hovorili o ZERO TRUST trende v IT SEC. Aká je budúcnosť šifrovania ? Šifrovanie bude naďalej zohrávať kľúčovú rolu v našom živote. 

Kvantové počítače len zvýšia tlak na vytváranie nových a mocnejších šifier. Šifrovacie algoritmy sú obávaným nepriateľom Autokratických systémov kde je ľuďom upieraná sloboda. Často sú za použitie šifrovacieho algoritmu vysoký trest. Preto slobodne šifrujte ... 