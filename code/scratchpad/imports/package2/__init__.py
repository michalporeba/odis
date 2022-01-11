from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class Package2:
    pass

def function2():
    return 'Hello from Package2'

p2 = 'package2 here'