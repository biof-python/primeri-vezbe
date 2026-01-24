import os
import subprocess

for naziv_fajla in os.listdir('../cas01/'):
    subprocess.call(['python3','../cas01/'+naziv_fajla])