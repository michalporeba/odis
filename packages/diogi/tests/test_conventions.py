from diogi.conventions import *


def test_reduce_to_data():
    class A:
        def __init__(self, v: any):
            self.v = v

        def as_data(self):
            return self.v * 2

    class X:
        def __init__(self, v: any):
            self.v = v

    assert to_data(None) is None
    assert 1 == to_data(1)
    assert "a" == to_data("a")
    assert [] == to_data([])
    assert [None] == to_data([None])
    assert [1, 2, 3] == to_data([1, 2, 3])
    assert ["a", "b", "c"] == to_data(["a", "b", "c"])
    assert 2 == to_data(A(1))
    assert [4, 6] == to_data([A(2), A(3)])
    assert isinstance(to_data(X(1)), X)
