import pytest
from app import calculate_bill

def test_calculate_bill_valid():
    assert calculate_bill(10.0, 5) == 50.0
    assert calculate_bill(0.0, 10) == 0.0

def test_calculate_bill_negative():
    with pytest.raises(ValueError):
        calculate_bill(-5.0, 2)
