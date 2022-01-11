from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class Package1:
    pass

def function1():
    return 'Hello from Package1'

p1 = 'package1 here'