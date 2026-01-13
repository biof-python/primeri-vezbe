import re

genetski_kod = 'ATAGATAGAGAGATAGAACACAAA'

def ispisi_kodone(kod):
    print(re.findall('[ATGC]{3}',kod))    
    for match in re.findall('[ATGC]{3}',kod):
        print(match)

ispisi_kodone(genetski_kod)
