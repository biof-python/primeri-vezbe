fajl = open('01.txt') #isto kao open('01.txt','r')

tekst = fajl.read()
tekst_bez_novog_reda_na_kraju = tekst.rstrip();
print('Ovo je tekst iz fajla: ' + 
      tekst_bez_novog_reda_na_kraju + ': Kraj teksta')
print('Tekst ima:' + str(len(tekst_bez_novog_reda_na_kraju))+' karaktera')
