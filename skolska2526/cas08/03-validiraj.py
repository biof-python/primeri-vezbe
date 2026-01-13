import re

genetski_kod = 'ATAGATAGAGAGATAGAACACA'

# ATGC - grupe 3 (kodoni) tada je kod
# A241351345
def validiraj_kod(kod):
    if (len(kod)%3==0):
        for karatker in kod:
            if karatker != 'A' and karatker != 'T' and karatker != 'C' and karatker != 'G':
                return False
        return True
    
    return False

def validiraj_kod_regex(kod):
    if re.fullmatch('([ATGC]{3})+',kod):
        return True
    return False

if validiraj_kod(genetski_kod):
    print(genetski_kod)
if validiraj_kod_regex(genetski_kod):
    print(genetski_kod)
