class Action:
    def __init__(self, name: str, url: str):
        self.name = name 
        self.url = url 

    def get_url_for(action: str) -> str:
        return 'test://home'

class Home(Action):
    def __init__(self, action: str):
        super().__init__('home', Action.get_url_for(action))

class Poly():
    def __init__(self, title: str=None):
        self.title = title 
        self.actions = []

    def set_title(self, title: str):
        self.title = title
        return self 

    def add_action(self, action: Action):
        self.actions.append(action)
        return self

    def to(self, formatter: any) -> dict: 
        return formatter.format(self)
        