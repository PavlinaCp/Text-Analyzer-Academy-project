"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavlína Čepcová
email: cepcovap@gmail.com
"""
import sys
import string
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#Autorizace a heslo
cara = 40 * "-"
autorizovany_seznam = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
uzivatel_username = input("Enter username: ")
uzivatel_password = input("Enter password: ")
print(cara)
for jmeno, heslo in autorizovany_seznam.items():
    if uzivatel_username == jmeno and uzivatel_password == heslo:
        print(f"Welcome to the app, {jmeno},\nWe have 3 texts to be analyzed.")
        print(cara)
        volba_textu = input("Enter a number btw. 1 and 3 to select: ")
        if not volba_textu.isnumeric():
            print("Invalid choice. You did not choose a number.")
            print("Terminating the program.")
            sys.exit()
        elif (
            volba_textu.isnumeric() 
            and int(volba_textu) > 3 or int(volba_textu) == 0
        ):
            print("Invalid choice. You did not choose a number between 1-3.") 
            print("Terminating the program.")
            sys.exit()
        elif volba_textu.isnumeric() and 0 < int(volba_textu) < 4:
            cislo_volby = int(volba_textu)
        break
else:
    print(f"Username: {uzivatel_username}\nPassword: {uzivatel_password}")
    print("Unregistered user, terminating the program.")
    sys.exit()

#Analyza textu
delka_slov = dict()
velke_pismeno = 0
velka_pismena = 0
mala_pismena = 0
pocet_cisel = 0
soucet_cisel = 0
pocet_slov = 0

for poradi, text in enumerate(TEXTS, start=1):
    if poradi == cislo_volby:
       for slova in text.split():
            slova = slova.strip(string.punctuation)
            pocet_slov += 1
            delka_klic = len(slova)
            if delka_klic in delka_slov:
                delka_slov[delka_klic] += 1
            else:
                delka_slov[delka_klic] = 1
            if slova.istitle():
                velke_pismeno += 1
            if slova.isupper():
                velka_pismena += 1
            if slova.islower():
                mala_pismena += 1
            if slova.isnumeric():
                pocet_cisel += 1
                soucet_cisel += int(slova)
print(cara)
print (f"""
There are {pocet_slov} words in the selected text. 
There are {velke_pismeno} titlecase words.
There are {velka_pismena} uppercase words. 
There are {mala_pismena} lowercase words.
There are {pocet_cisel} numeric strings.
The sum of all the numbers {soucet_cisel}
       """)
#Sloupcovy graf
print(cara)
print(f" {"LEN|":>3} {"OCCURRENCES":>20}{"|NR.":>14}")
print(cara)
for klic in sorted(delka_slov):
    symbol_graf = delka_slov[klic] * "*"
    print(f"{klic:>2}{"|":>3} {symbol_graf:<29} {"|"}{delka_slov[klic]}")
     