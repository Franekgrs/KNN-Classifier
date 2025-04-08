
def wczytajPlik(FileName):
    list1 = []
    with open(FileName, 'r') as csvFile:
        for linia in csvFile:
            list1.append(linia)
    return list1

def zamienPlikNaListe(linie):
    zamienioneDane = []
    for linia in linie:
        podzielonalinia = linia.split(';')
        cechy = [float(x) for x in podzielonalinia[:-1]]
        etykiety = podzielonalinia[-1].strip()
        cechy.append(etykiety)
        zamienioneDane.append(cechy)
    return zamienioneDane

# train_list = zamienPlikNaListe(wczytajPlik('train-set.csv'))
# test_list = zamienPlikNaListe(wczytajPlik('test-set.csv'))