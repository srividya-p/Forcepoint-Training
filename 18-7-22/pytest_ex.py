import pytest

def func(x):
    return x + 5

@pytest.mark.one
def test_func1():
    assert func(3) == 8

@pytest.mark.two
def test_func2():
    assert func(3) == 5

@pytest.fixture
def numbers():
    a, b, c, = 1, 2, 3
    return [a, b, c]

def test1(numbers):
    assert numbers[0] == 11

def test2(numbers):
    assert numbers[1] == 2

def test3(numbers):
    assert numbers[2] == 3