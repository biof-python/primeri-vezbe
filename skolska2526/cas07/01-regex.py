import re

# AT
# AT?G -> AG ili ATG
# AT(.)?G -> AT bilo sta nula ili jednom pa G
# AT(.)*G -> AT bilo sta nula ili vise  pa G
# ATCG ok, ATTT nije, ATTTG nije ok
# A(T*)G -> A T nula ili vise puta G
# ATG ok, ATCG ok, ATTT nije, ATTTG je ok
# AT+G -> nesto bar jednom izmedju
# ATG nije ok, ATCG ok, ATTTG je ok 
# AT$ -> zavrsava AT
# ^AT* -> pocinje sa A, pa onda ide T nula ili vise puta
# AT[ATCG]G -> ATAG, ATCG, ATTG, ATGG
# AT([ATCG]+)G -> AT(1 ili vise puta nesto od A,T,C,G)G
# AT([ATCG]?)G -> ATAG, ATCG, ATTG, ATGG ili ATG
# AT(AT|CG)?G -> ATATG, ATCGG, ATG
# AT(AT|CG){3,5}G -> ATATCGATG 
# AT((AT){3,5}|(CG)){3,5}G
# (AT(AT){3,5}G)|(AT(CG){3,5}G)
# AT((A|T|C|G)+)G

def ispisi_poklapanja(pattern, input):
    match = re.findall(pattern,input)
    # U slucaju grupe x predstavlja sve matcheve za sve grupe
    # U slucaju da x nema grupu vracen je samo string sa najvecim preklapanjem
    for x in match:
        print(x)

genetski_kod = 'ATGCATATGC'
# ispisi_poklapanja('AT*',genetski_kod)
# ispisi_poklapanja('AT*G',genetski_kod)
# ispisi_poklapanja('AT.*G',genetski_kod)
# ispisi_poklapanja('AT.?G',genetski_kod)
# ispisi_poklapanja('AT[ATGC]G',genetski_kod)
# ispisi_poklapanja('A[TG]{2,5}C',genetski_kod)
# ispisi_poklapanja('(A(TG{1,5})C)',genetski_kod)
ispisi_poklapanja('T*G*C$',genetski_kod)