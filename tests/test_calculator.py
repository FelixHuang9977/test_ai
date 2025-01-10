import pytest
from src.calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()
    
    def test_add(self, calculator):
        assert calculator.add(1, 2) == 3
        assert calculator.add(-1, 1) == 0
        assert calculator.add(-1, -1) == -2
    
    def test_subtract(self, calculator):
        assert calculator.subtract(3, 2) == 1
        assert calculator.subtract(1, 1) == 0
        assert calculator.subtract(-1, -1) == 0
    
    def test_multiply(self, calculator):
        assert calculator.multiply(2, 3) == 6
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(-2, -3) == 6
    
    def test_divide(self, calculator):
        assert calculator.divide(6, 2) == 3
        assert calculator.divide(-6, 2) == -3
        assert calculator.divide(0, 5) == 0
        
    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.divide(1, 0)