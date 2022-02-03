import pytest
from ...entities.connection import * 


@pytest.mark.parametrize('fromtoaction', Connection.States.get_valid_transitions())
def test_valid_state_transitions(fromtoaction):
    initial, target, action = fromtoaction
    sut = Connection(state = initial)
    getattr(sut, action)()
    assert sut.state == target