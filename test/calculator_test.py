import pytest
from calc.calculator import stringcalculator

def test_string_calculator_should_return_zero_on_empty_string():
    result=stringcalculator("")
    assert result== 0
    
def test_string_calculator_should_return_correct_number_on_one():
    result=stringcalculator("1")
    assert result== 1
    
def test_string_calculator_should_return_correct_number_on_two():
    result=stringcalculator("2")
    assert result== 2
    
def test_string_calculator_should_return_correct_number_on_two_values():
    result=stringcalculator("1,2")
    assert result== 3
    
def test_string_calculator_for_multiple_numeric_values():
    result=stringcalculator("1,2,3")
    assert result== 6
    
def test_string_calculator_new_line_as_delimiter():
    result=stringcalculator("1\n2,3")
    assert result== 6	
def test_string_calculator_negative_numbers_exception():
    	
	with pytest.raises(Exception, match = r'negatives not allowed \[-1, -2, -3\]'):
		result=stringcalculator("-1, -2, -3, 1, 2, 3")
        
def test_string_calculator_greater_than_1000():
    result=stringcalculator("//;\n1000,1;2")
    assert result== 3	

def test_string_calculator_any_length():
    result=stringcalculator("//[***]\n1***2***3")
    assert result== 6	
def test_string_calculator_multiple_delimiters():
    result=stringcalculator("//[*][%]\n1*2%3")
    assert result== 6	