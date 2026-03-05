"""End-to-end tests for the GET /interactions endpoint."""

import httpx


def test_get_interactions_returns_200(client: httpx.Client):
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client):
    response = client.get("/interactions/")
    assert isinstance(response.json(), list)


def test_get_interactions_response_structure(client: httpx.Client):
    response = client.get("/interactions/")
    data = response.json()
    if data:  # если есть данные
        item = data[0]
        assert "id" in item
        assert "learner_id" in item
        assert "item_id" in item
        assert "kind" in item
        assert "created_at" in item