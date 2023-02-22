import pytest
from code.easy.count_odds import count_odds


@pytest.mark.parametrize(
    'low, high, output', [
        (3, 7, 3),
        (8, 10, 1)
    ]
)
def test_count_odds(low, high, output):
    assert count_odds(low, high) == output
