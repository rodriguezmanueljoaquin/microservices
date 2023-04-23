from nameko.testing.services import worker_factory
from ...trips import TripsService
import pytest

def test_ping():
    service = worker_factory(TripsService)
    response = service.ping()
    assert response == "Pong!"

def test_create():
    service = worker_factory(TripsService)
    service.redis.hmset = lambda trip_id, trip: ""
    airport_id = service.create("AIRPORT_1", "AIRPORT_2")
    assert airport_id is not None

def test_get():
    service = worker_factory(TripsService)
    service.redis.hgetall = lambda trip_id: {"from": "AIRPORT_1", "to": "AIRPORT_2"}
    response = service.get("trip_id")
    assert response == {"from": "AIRPORT_1", "to": "AIRPORT_2"}