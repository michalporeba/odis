import callouts
import urllib.request as r
import json


@callouts.base
class WstlContext:
    @callouts.first
    def get_action_url(action: str) -> str:
        return f"ERROR: Undefined URL for action [{action}]!"


# TODO: rename to WstlState?
class Wstl:
    def __init__(self, title: str = ""):
        self._title = title
        self._actions = []
        self._data = []

    def with_get_action(self, name: str, action: str):
        self._actions.append(
            {"name": name, "type": "safe", "url": WstlContext.get_action_url(action)}
        )
        return self

    def add_data_item(self, data):
        self._data += [data]
        return self

    def to_data(self):
        data = {}
        if self._actions:
            data["actions"] = self._actions
        if self._data:
            data["data"] = self._data
        if self._title:
            data["title"] = self._title

        return {"wstl": data}

    def from_data(data: dict) -> None:
        if not "wstl" in data.keys():
            raise ValueError("Not a WSTL document")
        data = data["wstl"]

        wstl = Wstl()
        return wstl


class WstlClient:
    def __init__(self, url: str):
        self.url = url

    def hello(self):
        return self.do("")

    def do(self, action: str) -> any:
        req = r.Request(self.url + action)
        req.add_header("Content-Type", "application/json")
        response = r.urlopen(req)

        text = response.read()

        return Wstl.from_data(json.loads(text.decode("utf-8")))
