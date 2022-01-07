from django.conf import settings as dsettings

class SettingDefinition:
    def __init__(self, key: str):
        self.key = key 
        self.throwing = False
        self.has_default = False
        self.default = None
        self.has_explanation = False
        self.explanation = f'''
Looks like you registered a kinder setting for {key}
but forgotten to provide explanation. Find `settings.register("{key}")`
and change it to `settings.register("{key}").with_explanation("your explanation")`
'''

    def with_explanation(self, explanation: str):
        self.has_explanation = True
        self.explanation = explanation
        return self 

    def with_default_value(self, value):
        self.has_default = True
        self.default = value
        return self
    
    def as_throwing(self): 
        self.throwing = True
        return self

    def _to_user_message(self) -> str:
        if self.has_default:
            return f'''
It looks like you tried to access [{self.key}] setting but it was not configured.
The default value [] will be used but it might not be what your project needs.  

{self.explanation}

Even if the default value works for you, it is better to explicitly set it.
If you need more information on how to configure django projects check
https://docs.djangoproject.com/en/4.0/topics/settings/
'''
        else:
            return f'''
It looks like you tried to access [{self.key}] setting but it was not configured.

{self.explanation}

If you need more information on how to configure django projects check
https://docs.djangoproject.com/en/4.0/topics/settings/
'''


class KinderSettings():
    definitions = {}

    def __getattr__(self, name):
        try:
            return getattr(dsettings, name)
        except AttributeError as err:
            if name in KinderSettings.definitions.keys():
                definition = KinderSettings.definitions[name]
                if definition.throwing:
                    raise AttributeError(definition._to_user_message())
                elif definition.has_default:
                    print(definition._to_user_message())
                    return definition.default
                else:  
                    print(definition._to_user_message())
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

    def register_if_missing(self, name: str, default: any = None, explanation: str = None) -> None:
        if not name in KinderSettings.definitions.keys():
            definition = self.register(name)
            if not default is None:
                definition.with_default_value(default)
            if not explanation is None:
                definition.with_explanation(explanation)

    def explain(self, name: str) -> str:
        if name in KinderSettings.definitions.keys():
            definition = KinderSettings.definitions[name]
            if definition.has_explanation:
                return definition.explanation
            else: 
                return f'Sorry, the {name} setting is not explained!'
        return f'Sorry, the {name} setting is not defined!'

    def is_throwing(self, name: str) -> bool:
        if name in KinderSettings.definitions.keys():
            return KinderSettings.definitions[name].throwing
        return None

    def has_default(self, name: str) -> bool: 
        if name in KinderSettings.definitions.keys():
            return KinderSettings.definitions[name].has_default
        return None


settings = KinderSettings()