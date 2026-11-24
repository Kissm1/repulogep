import random 

szabad_helyek = [str(i) for i in range(1, 101)]
foglalt_helyek = []

print("Köszöntjük a NAKMCS Airlines-nál, ön a Lisszaboni közvetlen járatra vesz jegyet")
print("\n")

valasztas = input("véletlenszerűen(1) vagy manuálisan(2) akar helyet választani? ")
tobb_jegy = "igen"

jegyar_random = 2000
jegyar_manual = 4000




if valasztas == "1":
    hely = random.choice(szabad_helyek)
    print(F"{hely}. helyet kapta")
    foglalt_helyek.append(hely)
    szabad_helyek.remove(hely)
    for i, elem in enumerate(szabad_helyek, start=1):
            print(elem, end=", " if i % 10 != 0 else "\n")
    print("\n")   
elif valasztas == "2":   
    while tobb_jegy == "igen":    
        print("Szabad helyek: ")
        
        for i, elem in enumerate(szabad_helyek, start=1):
            print(elem, end=", " if i % 10 != 0 else "\n")
        print("\n")
        hely = input("Melyik helyet választod? ")
        if hely in szabad_helyek:
            foglalt_helyek.append(hely)
            szabad_helyek.remove(hely)
            print(f"{hely} lefoglalva!")
        else:
            print("Ez a hely már foglalt!")
            print("A maradt szabad helyek: ")
        
        for i, elem in enumerate(szabad_helyek, start=1):
            print(elem, end=", " if i % 10 != 0 else "\n")
        print("\n")
        tobb_jegy = input("Szeretne még jegyet venni? ")
        
        
foglalt_db = 0
for i in range(len(foglalt_helyek)):
    foglalt_db += 1

       
print(f"{foglalt_db}db jegy kelt el")
print(F"Az ön helyei: ", *foglalt_helyek, sep="  ")
if valasztas == "1":
    print(F"{foglalt_db * jegyar_random}FT a jegyek ára")
elif valasztas == "2":
    print(F"{foglalt_db * jegyar_manual}FT a jegyek ára")
