import uuid
from django.db import models

MAX_URL_LENGTH = 256

class OdisModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cts = models.DateTimeField(auto_now_add=True)
    uts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TextState():
    _valid_transitions = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)    
        transitions = []
        properties = {}

        for p in [p for p in dir(cls) if not p.startswith('_')]:
            attribute = getattr(cls, p)
            if not type(attribute) == tuple:
                continue

            if len(attribute) == 2: 
                value, label = attribute 
                previous = []
            elif len(attribute) == 3: 
                value,label,previous = attribute
            else: 
                continue 

            properties[value] = p
            transitions += [(p, value) for p in previous]
            p = setattr(cls, p, (value,label))

        for transition in transitions: 
            source, target = transition
            cls._valid_transitions += [(
                getattr(cls, properties[source]), 
                getattr(cls, properties[target])
                )]

    @classmethod 
    def get_states(cls):
        return [p for p in [
            getattr(cls,n) for n in dir(cls) if not n.startswith('_')
            ] if type(p) == tuple
        ]

    @classmethod 
    def get_valid_transitions(cls):
        return cls._valid_transitions

    @classmethod 
    def get_invalid_transitions(cls):
        states = cls.get_states()
        possible = [[(a,b) for b in states] for a in states]
        result = []
        for set in possible: 
            result += [p for p in set if not p in cls.get_valid_transitions()]
        return result
       
    @classmethod
    def is_valid_transition(cls, source, target):
        return (source, target) in cls.get_valid_transitions()
