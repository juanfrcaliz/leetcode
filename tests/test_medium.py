import pytest
from code.medium.ship_within_days import ship_within_days


@pytest.mark.parametrize(
    'weights, days, output', [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3)
    ]
)
def test_shipWithinDays(weights, days, output):
    result = ship_within_days(weights, days)
    assert result == output
