

# A. SKUMANIE INCIDENTU ON SITE

Dnes bude rušný deň Ranný telefonát neveští nič dobrého. Kybernetický zločin bujnie na našej sieti. Podľa plánu zvozu sa IRT (Náš Incident Response Tým) dáva do pohybu smer serverovňa. Cestou sa ešte zastavujeme na kávu ... TakeAway :)

## A.1 PASÍVNY PRIESKUM 
#live_forensics

Rozdeľujeme sa do trosch skupín s cieľom zhromaždiť pasívne to znamená bez zásahu do LAN čo najviac informácií o INCIDENTE. Jedna skupina kontruluje `eve.json`  dátový výstup zo Suricaty IDS. ďalšia skupina prehrabáva Logy. Akonáhle sa niečo dozvieme informujeme ostatné skupiny a zapíšeme si čas a miesto kde sa udalosť stala ako aj IP či MAC adresy aktérov.
Posledná skupina má na starosti záznamy v .pcap. Vyzerá to tak, že útok sa udial v čase keď väčšina Endpoitov bola vypnutá. To znamená, že komunikácie bude menej ako vo všedný pracovný deň. Vďaka IDS a centralizovaným logom neprešlo od napadnutia veľa času a je možné, že malware alebo hackeri sú v RECON fáze a zatiaľ nebrnkli na žiaden náš HONEYPOT v chránených segmentoch LAN. 

ZDROJE PASIVNEHO PRIESKUMU:
<li>nahrate .pcap na Suricate, alebo 24/7 nahravky </li>
<li>Log Management, logy, Event-Log</li>
<li>suricata eventy</li>



KOMPROMITACIA SYSTEMU:
Neobvykla komunikacia zo siete
Neobvykla komunikacia medzi klientami
Neobvykle pouzitie Privilegovanych prav
Aktivita Usera z neobvyklych IP
Viacero nepodarenych loginov  (4625, 4771, 4772)
Neobvykle zadania SQL do databazy - netypicke pokusy o ziskanie info z tabuliek
Zmeny v Registri a v suborovom systeme
Neobvykle poziadavky na DNS
Neobvykle casy Patchov a Updatov (Nie podla harmonogramu)
Nevysvetlitelne subory na DMZ produkcnych serveroch Zasifrovane subory!!!
Neobvykle vyuzitie browsera - vela requestov za min, Pulzne vyuzitie, Dlhe URL
Zmeny v spustenych servisoch - PRESNY ZOZNAM
Nahle vytvaranie, zmeny  USEROV, ADMINOV - PRIVILEGE ESCALATION

Teraz máme začíname predstavu, kedy a ako sa dostal útočník na LAN.


## A.2 AKTIVNY PRIESKUM
#live_forensics

### A.2.1  MEMORY DUMP BEZIACEHO POCITACA
#live_forensics
Ak je na napdnutom počítači nejaký škodlivý kód aktívny bude určite spustený v nejakom bežiacom procese, alebo schovaný niekde v pamäti počítača. Najrozumnejšie preto je, skôr ako podnikneme ďalšie kroky získať kópiu pamúti pomocou špecálneho forenzného nástroja pre Windows alebo v Linuxe pomocou príkazu:

``` bash
cat /dev/mem  
memdump -h

```



Ak beží počítač vo VM v Sandboxe môžeme ho spustiť v tzv. Debugger móde a skúmať jeho obsah.
``` powershell
C:\Program Files\Oracle\VirtualBox>vboxmanage startvm "kali_nessus" -E VBOX_GUI_DBG_AUTO_SHOW=true -E VBOX_GUI_DBG_ENABLED=true
```

DEVOPS: DEBUGGER je program, ktorý nám umožňuje pomocou BREAKPOINTOV a KROKOVANIA umožňuje zastavovať a skúmať vnútro bežiaceho programu. Tieto programy sa používajú na nájdenie chýb v kóde, ale aj na pochopenie jeho aktivít ako je to pri REVERZNOM INŽINIERSTVE. 

Ak sa nám podarilo získať kópiu pamäte môžeme ju preskúmať úžasným pythonovským nástrojom Volatility:
https://github.com/volatilityfoundation/volatility


### A.2.2  NMAP ATTACK MODE

Na zistenie zmien na sieti môžeme použiť NMAP nastavená v Attak móde. Zistí nám všetky podrobnosti o počítačoch pripojených v segmente siete. 

``` bash
nmap -T4 -A -v IP/24
```

### A.2.3 WINDOWS FORENSIC TOOLKIT A INE STARINY

Aby sme mali predstavu ako funguje zbieranie dát z jednotlivých počítačov 
UKAZKA - WFT Windows Forensic Toolchest  posledna verzia z 2014

>[!warning]
>POZOR NA STARY SOFTVER
WFT, WinPE a podobne sú staré nástroje, ktoré už nemusia slúžiť ako by mali.


### A.2.4 GOOGLE GRR

Tento nástroj slúži na automatizované skúmanie počítačov na diaľku

Vzdialeny monitoring systemu pomocou Python Clien/Server
https://github.com/google/grr

1. POTREBUJEME MYSQL ALEBO MARIADB SERVER S PRAZDNOU DATABAZOU
``` bash
sudo apt install mysql-server  # ALEBO mariadb-server

sudo mysql -u root -p
HESLO: *****

```


``` sql
CREATE USER 'grr'@ 'localhost' IDENTIFIED BY 'password';
CREATE DATABASE grr;
GRANT ALL ON grr.* to 'grr' @ 'localhost';
exit
```

2. NAINŠTALOVAŤ GRR Z GOOGLEAPIS
``` bash
wget https://storage.googleapis.com/releases.grr-response.com/grr-server_3.4.6-7_amd64.deb   # alebo 3.2.4-6
sudo dpkg -i grr-server_3.2.4-6_amd64.deb
sudo apt-get install -fsudo dpkg
systemctl status grr-server

```
3. GRR SERVER Môžeme nainštalovať aj do Docker kontajneru
``` bash & powershell

docker run --name grr-server --ip 172.17.0.1 -e EXTERNAL_HOSTNAME=localhost -e ADMIN_PASSWORD=demo -p 0.0.0.0:8080:8080 ghcr.io/google/grr:v3.4.6.7
```

warning POZOR NA ŠIFROVANIE. POUŽITIE GRR VYŽADUJE NASTAVENIE ŠIFROVANIA MEDZI KLIENTO A SERVEROM 

4. GRR obsahuje inštalačny pre všetky druhov klientov od Windows, Linux až po MacOS. Tieto inštalačky stiahneme a spustíme na klientovi. 

5. Vytvorime kontajner s klientom:

``` bash & powershell

docker run --name grr-server --ip 172.17.0.2 -e EXTERNAL_HOSTNAME=localhost -e ADMIN_PASSWORD=demo -p 0.0.0.0:8080:8080 ghcr.io/google/grr:v3.4.6.7
```

DEBIAN KLIENTA SKOPIRUJEME DO URCENEHO DEBIAN ALEBO UBUNTU DOCKER KONTAJNERU:
``` bash & powershell
docker cp '.\grr_3.4.6.7_amd64.deb' ID_CONTAINER:/home/user/
```

# TOTO BUDE POKRACOVAT...



### A.2.5 DALSIE UZITOCNE PRIKAZY PRE WINDOWS

``` Powershell
netstat -naob
Taskmgr.exe
wmic qfe list
wmic product list
sigverif

```



## A.4  DERATIZACIA
UKAZKA - MALWAREBYTES A SPYBOT Search and Destroy

DEZINFEKCIA TOOLS
malwarebytes.com
SPYBOT Search and Destroy -  safer-networking.com
SOPHOS
ClamAV



### A.5  UROBENIE KOPIE NAKAZENEHO SYSTEMU
WINDOWS : Passmark ImageUSB a potom  winiso
KALI - GUYMAGER robi specialne dd alebo svoje kopie

``` bash
dd if=/disk.dd of=/disk.iso bs=512
```



# B. FORENZIC MODE v KALI
#reverse_eng 

### B.1  HASHDEEP  - KRAL HASHOV

Pomocou hashovacích algoritmov vieme urobiť otlačok každého spistiteľného súboru v počítači. Hashdeep vie aj analyzovať a porovnávať súbory, adresáre či v nich nedošlo k zmene. 

``` bash
hashdeep -r ADRESAR > subor_s_hashmi
hashdeep -a -k subor_s_hashmi -r ADRESAR
```


### B.2 BINWALK - POROVNAVANIE DUMPOV

Ak sme vytvorili zoznam modifikovaných súborov a ak máme niekde originál súboru s inštalačky systému, môžeme ich porovnať pomocou programu BINWALK. Tento program nám dokáže rýchlo nájsť rozdiely  a zozbraziť ich v požadovanom formáte.

binwalk -W FILE FILE

BINWALK vie porovnávať viacero súborov naraz.

POZOR NA ROZNE VERZIE TOHO ISTEHO PROGRAMU. MUSIME VŽDY POROVNAVAŤ ROVNAKÉ VERZIE 


### B.3 AUTOPSY

Na forenzné prezeranie diskov a ich imidžov použijeme AUTOPSY. Tento softvér je určený pre profesionálov akými sú súdni znalci a pod. VIeme prechádzať disk po sektorov, robiť si poznámky, vyhľadávať reťazce a súbory (ÁNO AJ TIE VYMAZANÉ) a pod. 



# C. REVERSE ENGENEERING

Reverzné inžinierstvo sa zapodieva spätným rozoberaním programov, ktoré by mohli obsahovať škodlivý kód alebo zraniteľnosť. 

STROJOVÝ KÓD  > ASSEMBLY > C > JAVA >  PYTHON

KOMPILOVANÝ KÓD je keď zdrojový kód programu pomocou kompilera preložíme do strojového kódu.


C.1 NASM - NETWIDE ASSEMBLER

TO čo je pre normálneho hackera Python3 je pre reverzného inžiniera C a ASSEMBLY. Znalosť týchto jazykov a použitia Debuggerov nám pomôže rozoberať programy na drobné a analyzovať ich zraniteľnosti aj účel. 

[NASM](https://nasm.us/)
ROZNA ARCHITEKTURA = ROZNA SADA INSTRUKCII


``` asm

## Hello World

section	.text
	global _start       ;must be declared for using gcc
_start:                     ;tell linker entry point
	mov	edx, len    ;dlzka spravy
	mov	ecx, msg    ;sprava na zapisanie
	mov	ebx, 1	    ;co s tym (stdout)
	mov	eax, 4	    ;systemove volanie (sys_write)
	int	0x80        ;zavolaj kernel a vykonaj
	mov	eax, 1	    ;systemove volanie (sys_exit)
	int	0x80        ;zavolaj kernel a vykonaj

section	.data

msg	db	'Hello, world!',0xa	;nas text ulozeny v bytoch
len	equ	$ - msg			;vypocitana dlzka naseho textu

```

``` bash 
nasm -f elf64 -o hello.o hello.asm  # skompiluje objekt file
xxd hello.o
ld -s -o hello hello.o  # zlinkuje objekt file na executable
./hello
binwalk -W hello hello.o
```

info ARCHITEKTÚRA 


### C.2 RADARE2 = SKUMANIE BINARNYCH SUBOROV A PROCESOV

DOBRÝ TUTORIÁL:
https://github.com/ifding/radare2-tutorial




rabin2 -I FILE.bin

JEDNORIADKOVY ASSEMBLER SKÚMA KÓD 
rasm2 -a x86 -b 64 "mov eax, 4"
rasm2 -a x86 -b 64 b804000000




Prepnut do vizual modu V

r2 -d FILE alebo PID

-aa

pdf @ funkcia

eco matrix




p sa prepinam medzi printovacimo modami
shift q quit

ma to vselikake debuggeyr a ine nastroje

