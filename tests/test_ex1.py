import pytest

@pytest.mark.slow 
def test_example():
    assert 1 == 1
    print("First test")

def test_example1():
    assert 1 == 1