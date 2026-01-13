import re
genetski_kod = 'ATGCGAATTGCA'

# .findall() -> vraca grupe
# findall, match, search, finditer
print(re.findall('(AA)|(TT)|(GG)|(CC)',genetski_kod))
for match in re.finditer('(AA)|(TT)|(GG)|(CC)',genetski_kod):
    print('Pronadjen je match: ' + match.group() + ' na poziciji '+ str(match.start()))

