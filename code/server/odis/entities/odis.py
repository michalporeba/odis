from ..wstl import Wstl

class OdisNode:
    @property
    def hello(self): 
        return 'Hello'
    

class DemoService(OdisNode):
    pass 


class WstlSerializer:
    pass


class WstlServiceSerializer(WstlSerializer):
    def __init__(self, source, request=None):
        self.request = request

    @property
    def data(self):
        return [
            self.request.build_absolute_uri(),
            self.request.get_full_path()
        ]
        return Wstl("ODIS - Hello from WstlServiceSerializer").to_data()


class WstlModelSerializer(WstlSerializer):
    pass 


class DemoServiceSerializer(WstlServiceSerializer):
    class Meta: 
        model = DemoService
        fields = '__all__'
