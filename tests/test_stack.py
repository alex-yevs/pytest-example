def test_stack():
    stack = []

    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two' 
    assert stack.pop() == 'one'
