from sinc2d import *
import numpy as np

def test_sinc2d_x0_y0():
	"""Testing case x and y are zero in sinc2d()"""
	expected_value = 1.0
	calculated_value = sinc2d(0.0,0.0)
	assert expected_value == calculated_value
	
def test_sinc2d_x0():
	"""Testing case x is zero, y is non-zero in sinc2d()"""
	expected_value = 0.5*np.sin(2.0)
	calculated_value = sinc2d(0.0,2.0)
	assert expected_value == calculated_value
	
def test_sinc2d_y0():
	"""Testing case y is zero, x is non-zero in sinc2d()"""
	expected_value = 0.5*np.sin(2.0)
	calculated_value = sinc2d(2.0,0.0)
	assert expected_value == calculated_value
	
def test_sinc2d_normal():
	"""Testing case x, y non-zero in sinc2d()"""
	expected_value = 0.25*np.sin(2.0)*np.sin(2.0)
	calculated_value = sinc2d(2.0,2.0)
	assert expected_value == calculated_value