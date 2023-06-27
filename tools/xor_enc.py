# xor_enc.py
'''
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


# 3DES - stary algoritmus

# SYMETRICKE SIFROVANIE  1 KLUC OBE STRANY

# AES256 - INDUSTRIALNY STANDARD SIFROVANIA (Rjijandel)
# ECC - ELIPTICKA KRIVKY
# CHACHA 

PERMABOXY = {"A":'V', "B": "X"}
'''
SBOX = [12, 56, 67,95]  # 1 KLUC a musia ho mat obe strany

text = 65 # ASCII A
enc = 0
for i in SBOX:
	enc = i ^ enc
	print(enc)
print('KONECNA HODNOTA PO APLIKACII SBOXOM', enc)

