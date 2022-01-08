from .aplugin import APlugin

class FirstA(APlugin):
    def get_id() -> int:
        return 1

    def get_many() -> list:
        return [10, 11]

class SecondA(APlugin):
    def get_id() -> int:
        return 2

    def get_name() -> str:
        return 'a second'

    def get_many() -> list: 
        return 12

class ThirdA(APlugin):
    def get_id() -> int:
        return 3

    def get_name() -> str:
        return 'a thrid'

    def get_many() -> list: 
        return 'and more'
