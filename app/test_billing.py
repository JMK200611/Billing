import pytest
from billing import calculate_bill, calculate_discounted_bill

def test_calculate_bill():
    assert calculate_bill(10.0, 5) == 50.0
    assert calculate_bill(0, 5) == 0.0
    with pytest.raises(ValueError):
        calculate_bill(-10, 5)

def test_calculate_discounted_bill():
    assert calculate_discounted_bill(100.0, 1, 10) == 90.0
    assert calculate_discounted_bill(50.0, 2, 0) == 100.0
    with pytest.raises(ValueError):
        calculate_discounted_bill(10, 2, -5)
