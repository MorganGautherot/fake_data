import numpy as np
from datetime import date
from fake_data_app.sensor import VisitSensor


class StoreSensor:
    def __init__(
        self,
        name: str,
        avg_visit: int,
        std_visit: int,
        perc_malfunction: float = 0,
        perc_break: float = 0,
    ) -> None:
        """Initialize a store"""
        self.name = name
        self.sensors = list()

        # traffic distribution
        seed = np.sum(list(self.name.encode("ascii")))
        np.random.seed(seed=seed)
        traffic_percentage = [48, 30, 5, 3, 1, 2, 10, 1]
        np.random.shuffle(traffic_percentage)

        # Intialization of the store sensors
        for i in range(8):
            sensor = VisitSensor(
                traffic_percentage[i] * avg_visit,
                traffic_percentage[i] * std_visit,
                perc_malfunction,
                perc_break,
            )

            self.sensors.append(sensor)

    def get_all_traffic(self, date: date) -> int:
        """Return the traffic for all sensors of the store at a date"""
        visit = 0
        for i in range(8):
            visit += self.sensors[i].get_visit(date)
        return visit

    def get_sensor_traffic(self, id: int, date: date) -> int:
        """Return the traffic for one sensor at a date"""
        return self.sensors[id].get_visit(date)
