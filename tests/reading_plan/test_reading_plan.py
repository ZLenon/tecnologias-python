from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch
from tests.reading_plan.data_base_mock import mock_db


# Req 6
@patch("tech_news.analyzer.reading_plan.find_news")
def test_reading_plan_group_news(db):
    db.return_value = mock_db
    x = ReadingPlanService.group_news_for_available_time(2)
    assert len(x["readable"]) == 3
    assert len(x["unreadable"]) == 1
    assert x["readable"][0]["unfilled_time"] == 0
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
