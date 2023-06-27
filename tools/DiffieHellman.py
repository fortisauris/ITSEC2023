#DiffieHellman.py

# 2 privatne a 2 verejne

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