import os

def ispisi_fajl(putanja):
    ulaz = open(putanja,'r')
    for linija in ulaz:
        print(linija.rstrip())
    ulaz.close()

for naziv_fajla in os.listdir('./proba'):
    ispisi_fajl('./proba/'+naziv_fajla)