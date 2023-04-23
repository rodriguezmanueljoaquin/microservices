import pytest

def test_ping(trip_service):
    response = trip_service.ping()
    assert response == "Pong!"

def test_create_and_get_trip(trip_service):
    trip_id = trip_service.create("AIRPORT_1", "AIRPORT_2")
    assert trip_id is not None

    trip = trip_service.get(trip_id)
    assert trip["from"] == "AIRPORT_1"
    assert trip["to"] == "AIRPORT_2"