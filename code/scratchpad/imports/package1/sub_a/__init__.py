from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class SubA:
    pass

def function_a():
    return 'Hello from Sub A'

sub_a = 'Sub A here'