from sensor import VisitSensor
from store import StoreSensor
from datetime import date

lille_store = StoreSensor('Lille', 1200, 300)

print(lille_store.get_all_traffic(date(2023, 9, 13)))

print(lille_store.get_sensor_traffic(2, date(2023, 9, 13)))

           
