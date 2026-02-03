# Saberi sve cele brojeve koji su argumenti komandne linije

import sys
import re

sum = 0
sabirci = sys.argv[1:]
for argument in sabirci:
    if re.fullmatch('-?\\d+',argument):
        sum += int(argument)

print(sum)

