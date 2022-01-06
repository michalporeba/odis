class Wstl():
  def __init__(self, title: str = ''):
    self._title = title
    self._actions = []
    self._data = []

  def with_get_action(self, name: str, action: str):
    self._actions.append({
        'name': name, 
        'type': 'safe',
        'url': WstlContextProvider.get_first_action_url(action)
    })
    return self

  def to_data(self):
    data = {}
    if self._actions:
      data['actions'] = self._actions
    if self._data:
      data['data'] = self._data
    if self._title:
      data['title'] = self._title

    return { "wstl": data }

class WstlContextProvider:
    instances = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.instances.append(cls())

    def get_action_url(self, name:str) -> str:
        return []

    def get_first_action_url(name: str) ->list:
        for i in WstlContextProvider.instances:
            url = i.get_action_url(name)
            if url: 
                return url
        
        return 'ERROR: Action ' + name + ' has no defined URL'
