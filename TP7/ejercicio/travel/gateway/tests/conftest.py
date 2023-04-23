import pytest
from nameko.testing.services import worker_factory
from ..trips import TripsService

@pytest.fixture(scope="module")
def trip_service():
    service = worker_factory(TripsService)
    yield service