from sensor import VisitSensor
from datetime import date

lille_sensor_1 = VisitSensor(1200, 300, perc_malfunction=10)

print(lille_sensor_1.get_visit(date(2023, 11, 28)))

           
