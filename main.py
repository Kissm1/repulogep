import random 

szabad_helyek = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
foglalt_helyek = []

valasztas = input("véletlenszerűen(1) vagy manuálisan(2) akar helyet választani? ")

if valasztas == "1":
    hely = random.choice(szabad_helyek)
    print(F"{hely}. helyet kapta")
    foglalt_helyek.append(hely)
    szabad_helyek.remove(hely)
    print(szabad_helyek)