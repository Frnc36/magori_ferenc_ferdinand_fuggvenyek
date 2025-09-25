def relacio(szam1:int, szam2:int):
   
    
    if szam1 > szam2:
        jel = ">"
    
    elif szam1 < szam2:
        jel = "<"
    
    else:
        jel = "=" 
    
    return jel
        

def kiiras():       
    szam1:int = int(input("Szám1: "))
    szam2:int = int(input("Szám2: "))

    er = relacio(szam1, szam2)
    print(er)

kiiras()