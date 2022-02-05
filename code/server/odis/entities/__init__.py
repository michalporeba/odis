import uuid
from django.db import models


MAX_URL_LENGTH = 256
class OdisModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cts = models.DateTimeField(auto_now_add=True)
    uts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StateTransitionError(RuntimeError):
    pass


class UndefinedActionError(RuntimeError):
    pass


def guard_state_transition(transitions: dict, action: str, state: any, *args, **kwargs) -> None:
    def noop(*args, **kwargs):
        pass 

    implementation = None
    action_transitions = transitions.get(action.lower(), None)
    if action_transitions is None:
        raise UndefinedActionError

    if callable(action_transitions):
        implementation = action_transitions
    elif isinstance(action_transitions, list) : 
        for initial_states in action_transitions:
            if state in initial_states:
                implementation = initial_states[-1]
                if implementation is None:
                    implementation = noop 

    if implementation is None: 
        raise StateTransitionError

    implementation(*args, **kwargs)
    