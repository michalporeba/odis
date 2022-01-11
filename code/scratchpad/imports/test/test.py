import sys
sys.path.append('../')

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from package1 import *
import package2 

print(package2.p2)
print(type(package2)) 
print(p1)