import os             
all_files = os.listdir("../../jeux_de_donnees/dyn2l")  
print(all_files) 

import os

for i in zip(all_files):
    os.system('py progdyn2.py ../../jeux_de_donnees/dyn2l/%s -r' % (i))