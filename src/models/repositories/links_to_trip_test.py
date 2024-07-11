import uuid
import pytest
from src.models.settings.db_connection_handler import db_connetction_handler
from .links_to_trip import LinksToTrip

db_connetction_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='interação com banco')
def test_registry_link():
    conn = db_connetction_handler.get_connection()
    links_to_trip = LinksToTrip(conn)

    registry_link_info = {
        "id": link_id,
        "trip_id": trip_id,
        "email": "test@example.com",
        "link": "https://filme.com.br",
        "title": "O trem bala ta na pista"
    }

    links_to_trip.registry_link(registry_link_info)


@pytest.mark.skip(reason='interação com banco')
def test_find_link_info():
    conn = db_connetction_handler.get_connection()
    links_to_trip = LinksToTrip(conn)

    links = links_to_trip.find_link_info(trip_id)
    
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)