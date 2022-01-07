#from django.conf import settings as testset
from django_kinder_settings import settings
import pytest

# Simulating the config file
settings.configure()
settings.UNREGISTERED = 'unregistered value'

settings.register('REGISTERED_NOT_DEFINED_NOT_THROWING')
settings.register('REGISTERED_NOT_DEFINED_AND_THROWING')
settings.register('WITH_DEFAULT_VALUE').with_default_value('x')
settings.register('THROWING_WITH_CUSTOM_EXPLANATION').\
    with_explanation('abcdef').\
    as_throwing()

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

def test_registered_not_defined_throwing_with_custom_explanation():
    with pytest.raises(AttributeError) as err: 
        settings.THROWING_WITH_CUSTOM_EXPLANATION
    assert 'abcdef' in str(err.value)

def test_multiple_registrations():
    settings.register('MULTIPLE').with_default_value('1')
    assert '1' == settings.MULTIPLE
    settings.register('MULTIPLE').with_default_value('2')
    assert '2' == settings.MULTIPLE

def test_if_missing_registration():
    settings.register('NOT_MISSING').with_default_value('i_am_here')
    assert 'i_am_here' == settings.NOT_MISSING
    settings.register_if_missing('NOT_MISSING', 'a_factory_default')
    assert 'i_am_here' == settings.NOT_MISSING

def test_if_missing_does_not_stop_registration():
    settings.register_if_missing('WITH_FACTORY_DEFAULT', 'default')
    assert 'default' == settings.WITH_FACTORY_DEFAULT
    settings.register('WITH_FACTORY_DEFAULT').with_default_value('custom')
    assert 'custom' == settings.WITH_FACTORY_DEFAULT

def test_if_missing_registrations_can_be_repeated():
    settings.register_if_missing('IF_MISSING', '1')
    assert '1' == settings.IF_MISSING
    settings.register_if_missing('IF_MISSING', '2')
    assert '1' == settings.IF_MISSING
