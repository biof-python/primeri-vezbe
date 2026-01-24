import os

def ispisi_fajlove(putanja):
    print(putanja+':')
    for naziv_fajla in os.listdir(putanja):
        print(naziv_fajla)

ispisi_fajlove('./podaci')
# os.rename('./podaci/01.txt','./podaci/1.txt')
print('Promenjen naziv')
ispisi_fajlove('./podaci')
os.rename('./podaci/1.txt','./1.txt')
ispisi_fajlove('./podaci/')
ispisi_fajlove('./')