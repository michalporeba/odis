from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class SubB:
    pass

def function_b():
    return 'Hello from Sub B'

sub_b = 'Sub B here'