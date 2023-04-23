import pytest
from nameko.testing.services import worker_factory
from ..airports import AirportsService

@pytest.fixture(scope="module")
def airport_service():
    service = worker_factory(AirportsService)
    yield service