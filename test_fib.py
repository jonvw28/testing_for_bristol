from fib import *

def test_zero():
    """Testing behaviour of n = 0"""
    calculated_value = fib(0)
    expected_value = 1
    assert calculated_value == expected_value
	
def test_one():
    """Testing behaviour of n = 1"""
    calculated_value = fib(1)
    expected_value = 1
    assert calculated_value == expected_value
	
def test_ten():
    """Testing behaviour of n = 10"""
    calculated_value = fib(10)
    expected_value = 89
    assert calculated_value == expected_value