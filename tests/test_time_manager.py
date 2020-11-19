from datetime import datetime

from freezegun import freeze_time
import pytest

from src import time_manager

@pytest.mark.parametrize("test_input, expected_result", [(2,datetime(2020,9,6)),(4, datetime(2020,9,8))])
@freeze_time("2020-09-4")
def test_get_future_date(test_input, expected_result):
    actual_result = time_manager.get_future_date(test_input)

    assert actual_result == expected_result
