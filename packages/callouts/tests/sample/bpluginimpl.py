from .bplugin import BPlugin

class FirstB(BPlugin):
    def get_id() -> int:
        pass 

    def get_name() -> str:
        return 'b first'

    def do_your_maths(*args):
        result = 0
        for a in args:
            result += a
        return result 

class SecondB(BPlugin):
    def get_id() -> int:
        pass 
    def get_name() -> str:
        return 'b second'
    def do_your_maths(*args):
        result = 1
        for a in args:
            result *= a 
        return result 