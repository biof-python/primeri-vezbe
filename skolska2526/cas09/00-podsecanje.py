import re

ulaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas09/00-podsecanje-ulaz.txt','r')
izlaz = open('/home/miloje/Desktop/Vezbe/2025/OPP/primeri-vezbe/skolska2526/cas09/00-podsecanje-izlaz.txt','w')

for linija in ulaz:
    # ATAT, ATATAT
    # ATAG, AGAGAG
    if re.search(r'(A(T|G)){2,3}', linija) != None:
        izlaz.write(linija)

ulaz.close()
izlaz.close()