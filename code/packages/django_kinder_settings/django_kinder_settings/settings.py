from django.conf import settings

class KinderSettings:
    definitions = {}

class _SettingDefinition:
    def __init__(self, key: str):
        self.key = key 
        self.throwing = False
        self.has_default = False
        self.default = None
        self.explanation = f'''
        Looks like you registered a kinder setting for {key}
        but forgotten to provide explanation. Find `kindly_register("key")`
        and change it to `kindly_register("key").with_explanation("your explanation")`
        '''

    def with_explanation(self, explanation: str):
        self.explanation = explanation
        return self 

    def with_default_value(self, value):
        self.has_default = True
        self.default = value
        return self
    
    def as_throwing(self): 
        self.throwing = True
        return self

    def to_user_message(self):
        return f'''
        It looks like you tried to access [{self.key}] setting but is not defined in the settings file.
        {self.explanation}
        '''

def kindly_register(key: str) -> _SettingDefinition:
    definition = _SettingDefinition(key)
    KinderSettings.definitions[key] = definition

def kindly_get(key: str):
    if key in dir(settings):
        return getattr(settings, key)

    if key in KinderSettings.definitions.keys():
        definition = KinderSettings.definitions[key]
        if definition.throwing:
            raise Exception(definition.to_user_message())
        elif definition.has_default:
            return definition.default_value
        else:  
            print(definition.to_user_message())
            print('returning default value')
            return None
    
    return getattr(settings, key)