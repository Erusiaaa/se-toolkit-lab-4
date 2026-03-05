"""AI-generated unit tests for interactions."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def test_filter_returns_empty_for_non_existent_item_id():
    interactions = [
        InteractionLog(item_id=1, learner_id=1),
        InteractionLog(item_id=2, learner_id=2)
    ]
    result = _filter_by_item_id(interactions, 999)
    assert result == []


def test_filter_returns_multiple_matching_items():
    interactions = [
        InteractionLog(item_id=1, learner_id=1),
        InteractionLog(item_id=1, learner_id=2),
        InteractionLog(item_id=2, learner_id=3)
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 2