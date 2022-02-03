import itertools

class TextState:
    valid_transitions = []
    properties = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)    
        transitions = []

        for p in [p for p in dir(cls) if not p.startswith('_')]:
            attribute = getattr(cls, p)
            if not type(attribute) == tuple:
                continue

            value,label,next = attribute
            cls.properties[value] = p
            transitions += [(value, n) for n in next]
            p = setattr(cls, p, (value,label))

        for transition in transitions: 
            source, target = transition
            cls.valid_transitions += [(
                getattr(cls, cls.properties[source]), 
                getattr(cls, cls.properties[target])
                )]

    @classmethod 
    def get_invalid_transitions(cls):
        pass
        #return itertools.product(cls.properties.keys, cls.properties.keys)

    @classmethod
    def is_valid_transition(cls, source, target):
        return (source, target) in cls.valid_transitions

class Test(TextState):
    ONE = ('1', 'one', ['2','3'])
    TWO = ('2', 'two', ['3'])
    THREE = ('3', 'three', [])


t = Test()

print(t.TWO)
print(Test.valid_transitions)
print(Test.is_valid_transition(Test.ONE, Test.TWO))
print(Test.is_valid_transition(Test.TWO, Test.ONE))
print(Test.get_invalid_transitions())