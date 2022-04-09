from ..wstl import Wstl

class OdisNode:
    @property
    def hello(self): 
        return 'Hello'
    

class DemoService(OdisNode):
    pass 



class WstlServiceSerializer:
    def __init__(self, source, request=None):
        pass

    @property
    def data(self):
        return Wstl("ODIS - Hello from WstlServiceSerializer")

class DemoServiceSerializer(WstlServiceSerializer):
    class Meta: 
        model = DemoService
        fields = '__all__'
