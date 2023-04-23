import pytest
from nameko.testing.services import worker_factory
from ..trips import TripsService

@pytest.fixture
def trip_service():
    service = worker_factory(TripsService)
    return service