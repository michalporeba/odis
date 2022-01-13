from cmd import Cmd
from polymedia import RestClient
    
class WstlCli(Cmd):
    prompt = '> '
    intro = 'Welcome to Polymedia ReST client'

    def __init__(self):
        super().__init__()
        self.rest_client = None
        
    def do_exit(self, args):
        '''Here comes method documentation'''
        print('Hwyl')
        return True 

    do_EOF = do_exit 

    def default(self, args):
        if args == 'x' or args == 'q':
            return self.do_exit(args)

    def do_actions(self, args):
        print('actions:')
        for a in self.rest_client.poly.actions:
            print(f"  {a.name}")

    def do_connect(self, url):
        self.rest_client = RestClient()
        self.rest_client.get(url)
        WstlCli.prompt = 'WSTL> '
        for d in self.rest_client.poly.data:
            print(d)

        
    def do_do(self, args):
        poly = self.rest_client.do(args)
        for d in poly.data:
            print(d)
        

if __name__ == '__main__':
    WstlCli().cmdloop()