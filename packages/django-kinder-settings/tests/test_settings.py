#from django.conf import settings as testset
from django_kinder_settings import settings
import pytest

# Simulating the config file
settings.configure()
settings.UNREGISTERED = 'unregistered value'

settings.register('REGISTERED_NOT_DEFINED_NOT_THROWING')
settings.register('REGISTERED_NOT_DEFINED_AND_THROWING')
settings.register('WITH_DEFAULT_VALUE').with_default_value('x')

def test_access_to_defined_properties():
    assert 'unregistered value' == settings.UNREGISTERED

def test_exception_on_undefined_property():
    with pytest.raises(AttributeError):
        settings.NOT_REGISTERED_NOT_DEFINED

def test_registered_not_defined_not_throwing():
    assert None == settings.REGISTERED_NOT_DEFINED_NOT_THROWING

def test_registered_not_defined_and_throwing():
    with pytest.raises(AttributeError):
        settings.NOT_REGISTERED_NOT_DEFINED_AND_THROWING

def test_registered_not_defined_with_default():
    assert 'x' == settings.WITH_DEFAULT_VALUE