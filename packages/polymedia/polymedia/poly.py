import callouts

@callouts.base
class PolyContext:
    @callouts.first
    def get_action_url(action: str):
        # TODO: log it too
        return 'ERROR: There is no implementation for PolyContext.get_action_url'


class Action:
    def __init__(self, name: str, url: str):
        self.name = name 
        self.url = url 

    def get_url_for(action: str) -> str:
        return PolyContext.get_action_url(action)


class Get(Action):
    def __init__(self, name: str, action: str = None):
        action = name if action is None else action
        super().__init__(name, Action.get_url_for(action))


class Home(Get):
    def __init__(self, action: str):
        super().__init__('home', action)


class Self(Get):
    def __init__(self, action: str):
        super().__init__('self', action)


class Poly():
    def __init__(self, title: str=None):
        self.title = title 
        self.actions = []
        self.data = []

    def set_title(self, title: str):
        self.title = title
        return self 

    def add_action(self, action: Action):
        self.actions.append(action)
        return self

    def add_data_item(self, obj: any): 
        self.data.append(obj)
        return self

    def to(self, formatter: any) -> dict: 
        return formatter.format(self)
        