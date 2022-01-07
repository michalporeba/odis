from django.conf import settings as dsettings

class SettingDefinition:
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

class KinderSettings():
    definitions = {}

    def __getattr__(self, name):
        try:
            return getattr(dsettings, name)
        except AttributeError as err:
            print('xxxxxxxxx')
            if name in KinderSettings.definitions.keys():
                definition = KinderSettings.definitions[name]
                if definition.throwing:
                    raise AttributeError(definition.to_user_message())
                elif definition.has_default:
                    return definition.default
                else:  
                    print(definition.to_user_message())
                    print('returning default value')
                    return None  
            raise err 
        
    def __setattr__(self, name: str, value: any) -> None:
        setattr(dsettings, name, value)

    def __delattr__(self, name: str) -> None:
        delattr(dsettings, name)

    def register(self, name: str) -> SettingDefinition:
        definition = SettingDefinition(name)
        KinderSettings.definitions[name] = definition
        return definition


settings = KinderSettings()