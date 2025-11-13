#################################################################################################
#Zadanie 1
print("\n\nZadanie 1\n")
age = input("Podaj rok urodzenia:")
age = int(age)
dateTimeYearNow = 2025

if dateTimeYearNow - age >= 18:
    print("Jesteś pełnoletni")
else:
    print("Nie jesteś pełnoletni")

#################################################################################################
#Zadanie 2
print("\n\nZadanie 2\n")
route = input("Podaj długość trasy: ")
fuelCons= input("Podaj średnie spalanie auta (l/100 km): ")
price= input("Podaj cenę za litr paliwa: ")
passengers= input("Podaj ilość pasażerów (łączenie ze sobą): ")

fuelCons = float(fuelCons)/100

routeFuel = float(route)*fuelCons
routePrice = routeFuel*float(price)
costPerPassenger = routePrice/int(passengers)

if float(route)>=500.0:
    print(f"\n\nZużyjesz {routeFuel:.2f} litrów paliwa o wartości {routePrice:.2f}zł\nMając {passengers} pasażerów wychodzi po {costPerPassenger:.2f}zł na osobę.")
    print("Długa trasa – zaplanuj przerwy na odpoczynek!")
else:
        print(f"\n\nZużyjesz {routeFuel:.2f} litrów paliwa o wartości {routePrice:.2f}zł\nMając {passengers} pasażerów wychodzi po {costPerPassenger:.2f}zł na osobę.")

#################################################################################################
#Zadanie 3
print("\n\nZadanie 3\n")
wyniki = (45, 67, 82, 90, 55, 74, 100, 61)
sum = 0.0
count = 0
ifExcellent = False
for e in wyniki:
    sum+=float(e)

avg = sum/len(wyniki)
print(f"Średnia ocen: {avg}")
print("Wszystkie wyniki powyżej średniej: ")
for e in wyniki:
    if e>=avg:
        print(e)
    if e>=float(60):
        count+=1
    if e==float(100):
        ifExcellent = True
print(f"Wynik powyżej 60 otrzymało {count} osób")

if ifExcellent:
    print("Gratulacje dla najlepszego uczestnika!")

#################################################################################################
#Zadanie 4
print("\n\nZadanie 4\n")
produkty = ("mleko", "chleb", "masło", "ser", "jabłka", "banan", "jogurt", "pomarańcza", "woda", "kakao")
koszyk = []
dodaneProdukty = 0
print(f"Produkty w sklepie:: {produkty}")
while dodaneProdukty < 3:
    zakupy = input("Podaj produkt, który chcesz kupić: ")
    if zakupy in produkty:
        koszyk.append(zakupy)
        dodaneProdukty+=1
    else:
        print(f"Produkt {zakupy} jest niedostępny.")
koszyk.sort()
print(f"Twoja lista zakupów: {koszyk}")

#################################################################################################
#Zadanie 5
print("\n\nZadanie 5\n")
def analizuj_tekst():
    tekst = input("Podaj tekst: ")
    tekst = tekst.strip()
    tekst = tekst.lower()
    tekst = tekst.replace("python","PYTHON")
    liczenieLiterTekst = tekst.replace(" ", "")
    litery = {}
    for litera in liczenieLiterTekst:
        if litera in litery:
            litery[litera] += 1
        else:
            litery[litera] = 1
            
    podzialTekst = tekst.split()
    reverseTekst = []
    for wyraz in podzialTekst:
        reverseTekst.append(wyraz[::-1])
        
    reverseTekst=" ".join(reverseTekst)
    
    print(f"Sformatowany tekst: {tekst}\nOdwrócony tekst: {reverseTekst}\nLicznik liter: {litery}\n")
    wynik_tekst = {"tekst_sformatowany":tekst,"tekst_odwrócony":reverseTekst,"licznik_liter":litery}
    return wynik_tekst
analizuj_tekst()

#################################################################################################
#Zadanie 6
print("\n\nZadanie 6\n")
def student_info():
    imie = input("Podaj swoje imie: ")
    nazwisko = input("Podaj swoje nazwisko: ")
    rokStud = input("Na którym roku jesteś?: ")
    kierunek = input("Podaj kierunek na jakim jesteś: ")
    listaOcen = input("Podaj swoje oceny (np. 5 5 4 3 6): ")
    listaOcen = listaOcen.strip()
    listaOcen = listaOcen.split()
    daneStudenta = {"imie":imie, "nazwisko": nazwisko, "rok":int(rokStud), "kierunek": kierunek, "oceny": listaOcen}
    
    sredniaOcen = 0.0
    for oceny in listaOcen:
        sredniaOcen+=int(oceny)
    
    sredniaOcen=sredniaOcen/len(listaOcen)
    daneStudenta["srednia"] = sredniaOcen
    
    bokA = input("Podaj bok a: ")
    bokB = input("Podaj bok b: ")
    pole = float(bokA)*float(bokB)
    daneStudenta["poleKwadratu"] = pole
    return daneStudenta

print(student_info())