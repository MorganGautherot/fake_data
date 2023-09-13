from sensor import *
from datetime import date

lille_sensor_1 = VisitSensor(1200, 300)

print(lille_sensor_1.get_visit(date(2023, 9, 17)))