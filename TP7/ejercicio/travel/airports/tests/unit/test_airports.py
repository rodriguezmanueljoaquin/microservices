from nameko.testing.services import worker_factory
from ...airports import AirportsService
import pytest

def test_ping():
    service = worker_factory(AirportsService)
    response = service.ping()
    assert response == "Pong!"

def test_create():
    service = worker_factory(AirportsService)
    # mock redis
    service.redis.set = lambda airport_id, airport: airport_id
    airport_id = service.create({"airport": "Ezeiza"})
    assert airport_id is not None

def test_get():
    service = worker_factory(AirportsService)
    # mock redis
    service.redis.get = lambda airport_id: "123"
    response = service.get("airport_id")
    assert response == "123"