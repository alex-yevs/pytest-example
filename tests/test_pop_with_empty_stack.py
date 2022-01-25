import pytest

def test_pop_with_empty_stack():
    stack = []

    with pytest.raises(IndexError):
        stack.pop()

