import os
import shutil
# os.remove('./1.txt')

# remove je samo za fajlove
#os.remove('./podaci')

# rmdir moze da obrise folder, ali samo ako je prazan
# os.rmdir('./podaci')

shutil.rmtree('./podaci')
