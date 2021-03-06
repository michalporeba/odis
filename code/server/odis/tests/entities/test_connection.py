import pytest
from odis.entities import StateTransitionError
from odis.entities.connection import Connection


@pytest.mark.parametrize('fromtoaction', [
    (Connection.States.REQUESTED, Connection.States.DENIED, 'reject'),
    (Connection.States.REQUESTED, Connection.States.ACTIVE, 'approve'),
    (Connection.States.DENIED, Connection.States.ACTIVE, 'approve'),
    (Connection.States.ACTIVE, Connection.States.SUSPENDED, 'suspend')
])
def test_valid_state_transitions(fromtoaction):
    initial, target, action = fromtoaction
    sut = Connection()
    sut.state = initial
    sut.do(action)
    assert sut.state == target
    

def test_state_transition_error_on_invalid_transition():
    with pytest.raises(StateTransitionError):
        sut = Connection()
        sut.state = Connection.States.REQUESTED
        sut.do('suspend')

