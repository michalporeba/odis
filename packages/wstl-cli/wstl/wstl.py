from cmd import Cmd
from urllib import request as r 
import json 

class WstlRequest: 

    def __init__(self, url: str): 
        self.url = url

    def request(self, action: str = '') -> any:
        req = r.Request(self.url + action)
        req.add_header('Content-Type', 'application/json')
        response = r.urlopen(req)

        text = response.read()

        return json.loads(text.decode('utf-8'))['wstl']
        
    
class WstlCli(Cmd):
    prompt = 'wstl> '
    intro = 'Welcome to WSTL CLI'

    def __init__(self):
        super().__init__()
        self.service_url = 'http://127.0.0.1:8001/odis/'
        self.path = ''
        self.actions = {}

    def do_exit(self, args):
        '''Here comes method documentation'''
        print('Hwyl')
        return True 

    do_EOF = do_exit 

    def default(self, args):
        if args == 'x' or args == 'q':
            return self.do_exit(args)

    def do_actions(self, args):
        response = WstlRequest(self.service_url + self.path).request()
        self.actions.clear()
        for a in response['actions']:
            self.actions[a['name']] = a['url']
            print(f"  {a['name']}")

    def do_do(self, args):
        if args not in self.actions.keys():
            self.do_actions(self, None)
            return 

        response = WstlRequest(self.service_url + self.path).request()
        self.actions.clear()
        for a in response['actions']:
            self.actions[a['name']] = a['url']
        
        data = response['data']
        if list == type(data):
            for i in data:
                print(i)
        else: 
            print(data)


if __name__ == '__main__':
    WstlCli().cmdloop()