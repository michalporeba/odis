import callouts 

@callouts.base 
class WstlContext:
    @callouts.first
    def get_action_url(action: str) -> str:
      return f'ERROR: Undefined URL for action [{action}]!'

class Wstl():
  def __init__(self, title: str = ''):
    self._title = title
    self._actions = []
    self._data = []

  def with_get_action(self, name: str, action: str):
    self._actions.append({
        'name': name, 
        'type': 'safe',
        'url': WstlContext.get_action_url(action)
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

