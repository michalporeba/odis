import pytest
from odis.entities.connection import Connection

def test_test():
    import pathlib
    pathlib.Path().resolve()
    assert 1 == 1

@pytest.mark.parametrize('fromtoaction', Connection.States.get_valid_transitions())
def test_valid_state_transitions(fromtoaction):
    initial, target, action = fromtoaction
    sut = Connection()
    sut.state = initial
    getattr(sut, action)()
    assert sut.state == target