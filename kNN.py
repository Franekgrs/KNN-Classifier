import math
import LoadData

def odlegloscEuklidesowa(vec1, vec2):
    odleglosc = 0.0
    for i in range(len(vec1)-1):
        odleglosc += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(odleglosc)


def znajdzKNajblizszychIndeksow(train_list, test_list, k):
    wyniki = []
    for test_vec in test_list:
        odleglosci = []
        for idx, train_vec in enumerate(train_list):
            odleglosc = odlegloscEuklidesowa(test_vec, train_vec)
            odleglosci.append((odleglosc, idx))
        odleglosci.sort()
        k_najblizszych_indeksow = [indeks for _, indeks in odleglosci[:k]]
        wyniki.append(k_najblizszych_indeksow)
    return wyniki

def indeksyNaNazwyKwiatkow(listaIndeksow, train_set):
    listaNazwKwiatkow = []
    for wektorIndeksow in listaIndeksow:
        wektorNazw = [train_set[indeks][-1] for indeks in wektorIndeksow]
        listaNazwKwiatkow.append(wektorNazw)
    return listaNazwKwiatkow


def klasyfikuj(train_list, k_najblizszych_indeksow):
    przewidywane_etykiety = []
    nazwy_sasiadow = indeksyNaNazwyKwiatkow(k_najblizszych_indeksow, train_list)
    for etykiety_sasiadow in nazwy_sasiadow:
        najczestsza_etykieta = max(set(etykiety_sasiadow), key=etykiety_sasiadow.count)
        przewidywane_etykiety.append(najczestsza_etykieta)
    return przewidywane_etykiety



def obliczDokladnosc(przewidywane_etykiety, rzeczywiste_etykiety):
    poprawne = 0
    total = 0
    for i in range(len(przewidywane_etykiety)):
        total += len(rzeczywiste_etykiety[i])
        for etykieta in rzeczywiste_etykiety[i]:
            if przewidywane_etykiety[i] == etykieta:
                poprawne += 1
    dokladnosc = (poprawne / total) * 100
    return dokladnosc



def pobierzDaneDoKwiatka():
    input_str = input("Podaj wymiary kwiatka: ")
    return input_str
def zgadnijKwiatek(input_str, train_set, k):
    wymiaryKwiatka = [float(x) for x in input_str.split(';')]
    wymiaryKwiatka = [wymiaryKwiatka]
    dane = znajdzKNajblizszychIndeksow(train_set, wymiaryKwiatka, k)
    klasyfikacja = klasyfikuj(train_set, dane)
    return klasyfikacja

def przeprowadzKlasyfikacje(train_file, test_file, k):
    train_list = LoadData.zamienPlikNaListe(LoadData.wczytajPlik(train_file))
    test_list = LoadData.zamienPlikNaListe(LoadData.wczytajPlik(test_file))
    k = int(k)
    k_najblizszych_indeksow = znajdzKNajblizszychIndeksow(train_list,test_list,k)
    przewidywane_etykiety = klasyfikuj(train_list,k_najblizszych_indeksow)
    cosik = indeksyNaNazwyKwiatkow(k_najblizszych_indeksow,train_list)
    dokladnosc = obliczDokladnosc(przewidywane_etykiety,cosik)
    return dokladnosc


















