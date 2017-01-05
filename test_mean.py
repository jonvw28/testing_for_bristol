from mean import *

def test_ints():
    input = [1,2,3,4,5]
    calculated_value = mean(input)
    expected_value = 3
    assert calculated_value == expected_value

def test_zero():
    """Testing that mean correctly handles input values of zero"""
    input = [0,1,2,3,4]
    calculated_value = mean(input)
    expected_value = 2
    assert calculated_value == expected_value	
	
def test_float():
    """Testing that mean works for floats"""
    input = [1.0,2.0,3.0,4.0]
    calculated_value = mean(input)
    expected_value = 2.5
    assert calculated_value == expected_value
	
def test_int2float():
    """Testing that mean works for integers that give float values"""
    input = [1,2,3,4]
    calculated_value = mean(input)
    expected_value = 2.5
    assert calculated_value == expected_value