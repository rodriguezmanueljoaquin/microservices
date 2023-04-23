import pytest

def test_ping(airport_service):
    response = airport_service.ping()
    assert response == "Pong!"

def test_create_and_get_airport(airport_service):
    airport_id = airport_service.create({"airport": "Ezeiza"})
    assert airport_id is not None

    airport = airport_service.get(airport_id)
    assert airport["airport"] == "Ezeiza"