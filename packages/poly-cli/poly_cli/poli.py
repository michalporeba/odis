from cmd import Cmd
from polymedia import RestClient
from alps import Descriptor
from diogi.functions import get_if_exists
import argparse
import json

parser = argparse.ArgumentParser(description='')
parser.add_argument('-o', '--odis',
                    help='the ODIS start endpoint')
parser.add_argument('-k', '--knowledge',
                    help='file containing the knowledge')


class WstlCli(Cmd):
    prompt = '> '
    current_alps = None
    knowledge = None

    def __init__(self):
        super().__init__()
        self.new_request = True
        self.rest_client = None

    def preloop(self):
        print()
        if args.odis is not None:
            print(f'Connection to: {args.odis}')
            self.do_connect(args.odis)

    def postcmd(self, stop: bool, line: str) -> bool:
        print()
        return stop

    def do_exit(self, args):
        print('Hwyl')
        return True

    do_EOF = do_exit

    def default(self, args):
        if args == 'x' or args == 'q':
            return self.do_exit(args)

    def do_actions(self, args):
        self._show_actions()

    def do_connect(self, url):
        self.rest_client = RestClient()
        self.rest_client.connect(url)
        self._check_alps(self.rest_client.alps)
        WstlCli.prompt = f'{self.rest_client.format.upper()}> '

        for d in self.rest_client.poly.data:
            if d is not None:
                print(d)

        self._show_actions()

    def do_do(self, args):
        poly = self.rest_client.do(args, resolver=self._parameter_resolver)
        print()
        if 0 == len(poly.data) or (1 == len(poly.data) and poly.data[0] is None):
            print('Action returned non data')
        else:
            print('Response: ')
            for d in poly.data:
                print(d)

        self.new_request = True
        self._show_actions()

    def _check_alps(self, new_alps):
        if new_alps is not None:
            self.current_alps = new_alps
            print(f'Got new ALPS definition: {self.current_alps.title}')

    def _show_actions(self):
        print()
        print('Available actions:')
        for a in self.rest_client.poly.actions:
            print(f"  {a.name}")

    def _parameter_resolver(self, descriptor: Descriptor) -> any:
        if self.new_request:
            print('Request parameters:', )
            self.new_request = False
        print((' ' * 20 + f'  {descriptor.id} = ')[-20:], end='')
        value = self._check_knowledge(descriptor.id)
        if value is None:
            return input()
        else:
            print(value)
            return value

    def _check_knowledge(self, key: str) -> any:
        if self.knowledge is None and args.knowledge is not None:
            try:
                with open(args.knowledge, 'r') as f:
                    self.knowledge = json.load(f)
            except:
                print(f'ERROR: unable to open {args.knowledge} : ', end='')

        return get_if_exists(self.knowledge, key, None)


if __name__ == '__main__':
    args = parser.parse_args()
    WstlCli().cmdloop()
