
## 1. OPERACNE SYSTEMY

### 1.1 MS-DOS / WINDOWS 95


### 1.2 WIN10 s  integraciou WSL2 (Windows Subsystem for Linux)

### 1.3 PODIEL NA TRHU PC
WIN10 74% trhoveho podielu PC
MacOS cca 17% ostatne LINUX a pod

### PODIEL NA TRHU SERVEROV
SERVERY viac ako 80% su LINUX

> [!info] 
> SPECIALNE LINUX DISTRIBUCIE :
> KALI, 
> PARROT, 
> SECURITYONION
> 
> AJ VO VERZII *LIVE* S FORENSIC MODOM MOZETE MAT NA USB KLUCI VSADE SO SEBOU A MAT VSETKY POTREBNE NASTROJE NA DIAGNOSTIKU, DETEKCIU A PENETRACNE TESTOVANIE

[! war]

## 2. PATCHE A UPDATE PRE SOFTVER A HARDVER

### 2.1 FAKTY:
1. Neupdatovany a nezapatchovany pocitac je plny bezpecnostnych dier CAS BEZI
2. Tisice developerov pracuju na stabilite a bezpecnosti systemov KAZDY DEN
3. Nespoliehajte sa na uzivatelov - PATCH MANAGEMENT  ITARIAN

### 2.2 PROBLEM S PATCHOVANIM PRODUKCNYCH SERVEROV

DEVELOPER > DEVOPS > SYSADMIN

Predstavujeme DEVOPS - partia ktora ma na starosti testovanie softveru skor ako ho pustime na produkcny server


Security Patche a Updaty su klucovym faktorom ochrany Vaseho pocitaca 
CYKLUS SOFTVERU - ISSUES AND TICKETS

Preco nie su updatovane a patchovane pocitace ENDPOINTY A SERVERY 

UZIVATELIA ENDPOINTOV NEZNASAJU UPDATE A POVAZUJU ICH ZA ZBYTOCNE

ZRANITELNOSTI
https://github.com/CVEProject/cvelist.git

ZERO DAY ZRANITELNOSTI A EXPLOITY

WIN10 najnapadanejsia platforma  - uzavrety system, tlak developerov a hackerov



## 2. UZIVATELIA A ICH PRISTUPOVE PRAVA

>[!warning]
>ROOT je absolutny vladca pocitaca - !!! POZOR nikomu inemu nedavaj root pristup
>SUDO je zemepan - v skupine sudo moze byt viac uzivatelov, ktori mozu administrovat system


### 2.1 Spravime si uzivatela:

``` bash
sudo adduser test
sudo usermod -aG sudo test
sudo deluser test

```

``` powershell
$password = Read-Host -AsSecureString
$date = Get-Date -Year 2022 -Month 06 -Day 10
$username = 'test'
# Creating the user
New-LocalUser -Name "$username" -Password $password -AccountExpires $date -FullName "$username" -Description "Novy uzivatel"
Set-LocalUser -name '$username' -Description 'Jozo z uctovneho'
```


``` python
-Name : meno uzivatela max 20 characters|
-Password : Heslo
-Description : popis noveho uzivatela
-AccountExpires : Datum kedy user expiruje
-AccountNeverExpires: Nastavenie uzivatel nikdy neexpiruje
-Disabled : nastavenie uctu ako vypnuty
-FullName : Zobrazuj plne meno uzivatela
-PasswordNeverExpires : Heslo nikdy neexpiruje
-UserMayNotChangePassword : Uzivatel si nemoze nastavit heslo
```

### 2.2 SKUPINY
``` bash
groups
groups jozo
```


WINDOWS:
``` powershell
Get-LocalGroup
Get-LocalGroupMember Users
Add-LocalGroupMember -Group Users -Member "test"
```

### 2.3 PRISTUP K SUBOROM

``` sql
d - directory
r - read
w - write
x - execute

(USER GROUP OTHERS)  = ugo
```

``` bash
chown jozo SUBOR
chgrp GROUP SUBOR


chmod u+w SUBOR

chmod 777 SUBOR  # daj vsetko vsetkym
```

``` powershell
takeown /F '.\archive (1).csv'
$Acl = Get-Acl "FILE"  # premenna s pristupmi
$Ar = New-Object  System.Security.AccessControl.FileSystemAccessRule("forti","FullControl","Allow")
$Acl.SetOwner([System.Security.Principal.NTAccount]"forti")
$Acl.SetAccessRule($Ar)
Set-Acl "FILE" $Acl

```


## 3. OCHRANA HESLOM 2FA, BIOMETRIA, FIDO KEY

3.1 Silne a zapamatatelne heslo:
``` sql
K@5d1_8tvrtoK_HLADAM_p@pucE
```

3.2 POUZITIE PASSWORD MANAGERA: 
KeePass, 
1PASSWORD, 
LastPass

STACI SI POTOM PAMATAT MASTER PASSWORD

>[! warning]
>Akonahle sa hacker dozvie kde mate svoje hesla pokusi sa ich ziskat !!!





3.3 DARKWEB OBCHODOVANIE S HASHMI
Vacsina uniknutych hesiel pochadza z kradezi u velkych poskytovatelov sluzieb ako FB, Adobe atd.

[Have I Been Pwned: Check if your email has been compromised in a data breach](https://haveibeenpwned.com/)


3.4 BRUTEFORCE, SLOVNIKOVY UTOK, RAINBOW TABLES

> [! info]
> Naco vylamovat zamky ked mate od chaty kluc ?

``` bash
echo -n heslo | md5sum
md5sum SUBOR
```

>[!warning]
>HACKER - JA MAM MORE CASU


>[! warning] TOOLBOX>KALI LINUX : johntheripper - tradicny password cracker


``` bash
john --format=raw-md5 pwd.txt

john --incremental=ASCII --format=raw-md5 pwd.txt
cat .john/john.pot
```
POZNAMKA: Vyhodou johna je automaticka detekcia formatu a kodovania

>[! warning] TOOLBOX>KALI LINUX : hashcat - password cracker s vyuzitim automatickeho vykonu jadier Grafickych kariet 

``` bash
hashcat -b. # benchmark pocitaca
hashcat -m 0 -a 3 --show md5.txt
hashcat -m 0 -a 3 --show md5.txt ?l?d ?1?1?1?1?1
hashcat -m 0 -a 0 --show md5.txt /usr/share/wordlists/rockyou.txt

cat /local/share/hashcat/hashcat.potfile
```

>[!info] TOOLBOX>KALI LINUX : rockyou.txt je dlhy wordlist v adresari [/usr/share/wordlists/]. Je standardne kompressovany v archive .gz
>

``` bash
cd /usr/share/wordlist/
sudo gzip -d rockyou.txt.gz
```

>[! warning] TOOLBOX>KALI LINUX : hydra - Slovnikovy utok priamo  priamo na REMOTE SERVER

``` bash
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt IP ssh
```

### RAINBOW TABLES
Databaza Vsetky hashe vsetkych hesiel v roznych formatoch


3.5 MULTI FACTOR AUTHENTIFICATION

Google Authentificator  APPKA
Microsoft Authentificator APPKA

Yubi Key DEVICE  
[yubikey.sk – oficiálny predajca](https://yubikey.sk/)
[YubiKey.cz](https://yubikey.cz/)

Windows Hello : )
BIOMETRIA : )

>[! info]
>APPLE vs. FBI a zablokovany iPhone



## 4. LOGOVANIE

Windows Log je pristupny cez eventViewer alebo cez Powershell:

``` powershell
Get-EventLog -list
Get-EventLog -LogName Systemn -Newest 10
Get-EventLog -LogName System -After '6/5/23 0:00'
Get-EventLog -LogName System -Message '*login*'
Get-EventLog -LogName Security -InstanceId 4624 -Newest 50 | Select-Object TimeGenerated, Message | Format-Table -AutoSize
```


``` powershell
Get-EventLog System -Source Microsoft-Windows-WinLogon -Newest 10
```
Get-EventLog System -Source Microsoft-Windows-WinLogon -Newest 10


Ukazka skriptovania v Powershell:
``` powershell

for ($i=1; $i -le 5; $i++) {
    if ($i -eq 3) {
        Write-Host "The value of i is $i. This is the third iteration."
    }
    else {
        Write-Host "The value of i is $i."
    }
}
```

``` python

for i in range(1,5):
	if i == 3:
		print(f'Hodnota i je {i} TOTO JE TRETIE V PORADI')
	else:
		print(f'Hodnota i je {i}')
```

LINUX ma viacero systemov ako zachytit logy.

najjednoduchsi je skopirovat vsetko z adresara :

``` bash
cp -R /var/log/*  /kamtochceme
cat /etc/passwd
```

DVA SYSTEMY PRISTUPU K LOGOM
``` bash
dmesg
journalctl
```


``` bash
dmesg | tail -n 150 | grep root
```

## 5. OCHRANA SYSTEMU POMOCOU HASH ALGORITMOV

VYPOCITAME HASHSTRINGY PRE JEDNOTLIVE SUBORY AJ CELE ADRESARE

``` powershell
Get-FileHash SUBOR -Algorithm md5
Get-FileHash SUBOR -Algorithm SHA256 | Out-File -FilePath SUBOR
Get-FileHash SUBOR -Algorithm SHA256 | Out-File -FilePath SUBOR -Append
Get-ChildItem -Path .\ADRESAR\ -Recurse -Filter *.* | Get-FileHash -Algorithm md5 | Out-File -FilePath .\pwd.hashes -Append
```

POROVNAME ICH POMOCOU JEDNODUCHEHO ALGORITMU
``` powershell
$hashe_stare = Get-FileHash C:\hashes1.txt
$hash_nove = Get-FileHash C:\hashes2.txt

if ($hashe_stare -eq $hashe_nove) {
    Write-Host "The files are identical."
} else {
    Write-Host "The files are different."
}
```

``` powershell
Compare-Object (Get-Content .\pwd.hashes) (Get-Content .\pwd2.hashes)
```



``` linux
md5sum ADRESAR/* > hashes.txt
find ADRESAR -type f -exec md5sum {} \; > hashes.txt
```

``` bash
diff hashes1.txt hashes2.txt
vimdiff hashes1.txt hashes2.txt
```

## 6. USB KLUCE, KABLE A ZARIADENIA  - HUMAN INTERFACE DEVICE 

### 6.1 RUBBER DUCKY

>[!warning] 
>VYZERA TO AKO KACKA + 
>KVAKA TO AKO KACKA =
>TAK TO BUDE KACKA !

### 6.2 AUTOMOUNT - AUTORUN - SLUZBA ALEBO PREKLIATIE

``` linux
sudo fdisk -l
mkdir USB_KLUC
mount /dev/sd?1 /USB_KLUC
umount USB_KLUC
```

pico ducky github.com




