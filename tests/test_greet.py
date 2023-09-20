from lib.greet import greet

def test_greet():
    result = greet("Daniel")
    assert result == "Hello, Daniel!"