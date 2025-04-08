import kNN
import LoadData



dokladnosc = kNN.przeprowadzKlasyfikacje('train-set.csv', 'test-set.csv', 3)
print(f"Dokładność klasyfikacji: {dokladnosc}%")



wybor = "y"
while(wybor == "y"):
    print(kNN.zgadnijKwiatek(kNN.pobierzDaneDoKwiatka(),LoadData.zamienPlikNaListe(LoadData.wczytajPlik('train-set.csv')),5))
    wybor = input("Czy chcesz kontynuowac? [y/n]: ")

