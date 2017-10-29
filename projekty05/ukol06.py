#Uhodne pohlavi uzivatele podle zadaneho jmena a prijmeni. Mozna.

def zjisti_pohlavi():
    jmeno=input("Jsi holka nebo kluk? Napiš svoje jméno: ")
    prijmeni=input("A teď napiš svoje příjmení: ")

    #holka vs kluk
    koncovka_jmeno=jmeno[-1]
    koncovka_prijmeni=prijmeni[-1]
    if koncovka_jmeno==("a") or koncovka_prijmeni==("á") or koncovka_prijmeni==("a"):
        print("Ty musíš být holka!")
    else:
        print("Čuchám z tebe klukovinu!")

zjisti_pohlavi()

