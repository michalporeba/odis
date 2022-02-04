from odis.entities import TextState

class Sut(TextState):
    FIRST = ('one', 'the first state', [])
    SECOND = ('two', 'the second state', ['one'])
    THIRD = ('three', 'the third state', ['one','two','three'])
    SHORTER = ('s', 'two part tuple')

def test_states_are_reduced_to_two_element_tuples():
    assert Sut.FIRST == ('one', 'the first state')
    assert Sut.SECOND == ('two', 'the second state')
    assert Sut.THIRD == ('three', 'the third state')
    assert Sut.SHORTER == ('s', 'two part tuple')

def test_valid_transitions_collection():
    assert (Sut.FIRST, Sut.SECOND) in Sut.get_valid_transitions()
    assert (Sut.FIRST, Sut.THIRD) in Sut.get_valid_transitions()
    assert (Sut.SECOND, Sut.THIRD) in Sut.get_valid_transitions()
    assert (Sut.THIRD, Sut.THIRD) in Sut.get_valid_transitions()
    
def test_validation_of_transitions():
    assert True == Sut.is_valid_transition(Sut.FIRST, Sut.SECOND)
    assert True == Sut.is_valid_transition(Sut.FIRST, Sut.THIRD)
    assert True == Sut.is_valid_transition(Sut.SECOND, Sut.THIRD)
    assert True == Sut.is_valid_transition(Sut.THIRD, Sut.THIRD)
    assert False == Sut.is_valid_transition(Sut.FIRST, Sut.FIRST)
    assert False == Sut.is_valid_transition(Sut.SECOND, Sut.SECOND)
    assert False == Sut.is_valid_transition(Sut.SECOND, Sut.FIRST)
    assert False == Sut.is_valid_transition(Sut.THIRD, Sut.FIRST)
    assert False == Sut.is_valid_transition(Sut.SHORTER, Sut.FIRST)
    assert False == Sut.is_valid_transition(Sut.SHORTER, Sut.SECOND)
    assert False == Sut.is_valid_transition(Sut.SHORTER, Sut.THIRD)

def test_get_states():
    assert Sut.FIRST in Sut.get_states()
    assert Sut.SECOND in Sut.get_states()
    assert Sut.THIRD in Sut.get_states()
    assert Sut.SHORTER in Sut.get_states()

def test_invlid_transitions():
    assert (Sut.FIRST, Sut.FIRST) in Sut.get_invalid_transitions()
    assert (Sut.SECOND, Sut.SECOND) in Sut.get_invalid_transitions()
    assert (Sut.SECOND, Sut.FIRST) in Sut.get_invalid_transitions()
    assert (Sut.SHORTER, Sut.SHORTER) in Sut.get_invalid_transitions()
    assert (Sut.SHORTER, Sut.FIRST) in Sut.get_invalid_transitions()
