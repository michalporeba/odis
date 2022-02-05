import pytest 
from odis.entities import *
from django.db import models
import enum 


class Sut():
    class States(models.TextChoices):
        FIRST = ('one', 'the first state')
        SECOND = ('two', 'the second state')
        THIRD = ('three', 'the third state')
        SHORTER = ('s', 'two part tuple')

    state = None

    def to_second(self, *args, **kwargs):
        self.state = Sut.States.SECOND
    def to_third(self, *args, **kwargs):
        self.state = Sut.States.THIRD

    def do(self, action: str, *args, **kwargs):
        transitions = {
            'progress': [
                [Sut.States.FIRST, self.to_second],
                [Sut.States.SECOND, self.to_third]
            ],
            'third': [[
                Sut.States.FIRST,
                Sut.States.SECOND,
                self.to_third
            ], [
                Sut.States.THIRD,
                None #NoOp
            ]]
        }

        guard_state_transition(transitions, action, self.state)

def test_progress_action():
    sut = Sut()
    sut.state = Sut.States.FIRST 
    sut.do('progress')
    assert sut.state == Sut.States.SECOND
    sut.do('progress')
    assert sut.state == Sut.States.THIRD
    with pytest.raises(StateTransitionError):
        sut.do('progress')
   
def test_third_action():
    sut = Sut()
    sut.state = Sut.States.FIRST 
    sut.do('third')
    assert sut.state == Sut.States.THIRD
    sut.do('third')
    assert sut.state == Sut.States.THIRD
    

def test_invalid_operation():
    sut = Sut()
    sut.state = Sut.States.FIRST 
    with pytest.raises(UndefinedActionError):
        sut.do('undefined')

