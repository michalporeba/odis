from .entities.connection import Connection
from django.db.models import Q
import callouts 

@callouts.base
class OdisComponent:
    @callouts.flat
    def get_usable_connections_for(action: str):
        pass

class CoreOdisComponent(OdisComponent): 
    def get_usable_connections_for(action: str):
        print('getting usable connections')
        return [
            (c.uuid, c.type, c.url) 
            for c 
            in Connection.objects.filter(
                state=Connection.States.REQUESTED
            ).filter(
                Q(type__startswith=f'{action}:') | Q(type=action) | Q(type='odis')
            )
        ]
    
     