hossz = 30 #globális változó az eljárásokon kivűl van definiálban, ebben a fileban látszik minden hol

def nyugta():
    disz_sor("*") #disz_sor("*", hossz)
    szoveg_kozepre("NYUGTA")
    disz_sor("*")
    tetle_ar("kaja", 1234)
    tetle_ar("alma", 234)
    tetle_ar("körte", 234.2)
    er = osszeg(1234, 234, 234.2)
    disz_sor("=")
    #disz_sor("@")
    tetle_ar("Összesen: ", er)
    disz_sor("=")
    datum_nev("-")
    disz_sor("*")
    szoveg_kozepre("CÉG")
    disz_sor("*")


def disz_sor(kar:str = "*"): #alapértelmezett érték
    # kar - lokális változó, csak ebben az eljárásban látszik
    print(kar*hossz)

def szoveg_kozepre(felirat:str):
    # kar - lokális változó, csak ebben az eljárásban látszik
    print(f"*{felirat:^{hossz-2}}*")

def tetle_ar(tetel:str, ar:float, penznem:str = "Ft"):
    #print(f"tétel{tetel+1}")
    #print(f"{tetel_ar:>30}FT")
    hossz2 = hossz-len(tetel)-1-len(penznem)
    print(f"{tetel}{ar:>{hossz2}.2f} {penznem}")


def osszeg(ar1:float, ar2:float, ar3:float):
    eredmeny = ar1+ar2+ar3
    #függvény van visszatérési értéke
    return eredmeny

def datum_nev(dat:str = "-"):
    print()

