from fake_data_app.sensor import VisitSensor
from fake_data_app.store import StoreSensor
from datetime import date

def test_get_all_traffic():
    lille_store = StoreSensor('Lille', 1200, 300)
    visit = lille_store.get_all_traffic(date(2023, 9, 13))
    assert 79705 == visit

def test_get_sensor_traffic():
    lille_store = StoreSensor('Lille', 1200, 300)
    visit = lille_store.get_sensor_traffic(2, date(2023, 9, 13))
    assert 1594 == visit

def test_sunday_closed():
    lille_store = StoreSensor('Lille', 1200, 300)
    visit = lille_store.get_sensor_traffic(2, date(2023, 9, 17))
    assert -1 == visit

