import numpy as np
from datetime import date


class VisitSensor:
    def __init__(
        self,
        avg_visit: int,
        std_visit: int,
        perc_malfunction: float = 0,
        perc_break: float = 0,
    ) -> None:
        """Intialize sensor"""
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_malfunction = perc_malfunction
        self.perc_break = perc_break

    def get_visit(self, date: date) -> int:
        """return the number of person detected by the sensor
        during the day"""

        np.random.seed(seed=date.toordinal())
        proba_malfunction = np.random.randint(1, 100)

        # The sensor can break time to time
        if proba_malfunction < self.perc_break:
            visit = 0
        else:
            visit = self.simulate_visit(date)

        # The sensor can have malfunction time to time
        if proba_malfunction < self.perc_malfunction:
            print('malfunction')
            visit = np.floor(visit * 0.7)

        return visit

    def simulate_visit(self, date: date) -> int:
        """Simulate the number of person detected by the sensor
        during the day"""

        # Ensure reproducibility of measurements
        np.random.seed(seed=date.toordinal())

        # Find out which day the date corresponds to: Monday = 0, Sunday = 6
        week_day = date.weekday()

        # If the date is a sunday the store is closed
        if week_day == 6:
            visit = -1
        # If the date is a Wednesday there are more traffic
        elif week_day == 2:
            visit = np.random.normal(self.avg_visit, self.std_visit) * 1.15
        # If the date is a Friday there are more traffic
        elif week_day == 4:
            visit = np.random.normal(self.avg_visit, self.std_visit) * 1.20
        # If the date is a Saturday there are more traffic
        elif week_day == 5:
            visit = np.random.normal(self.avg_visit, self.std_visit) * 1.35
        # It is a normal day
        else:
            visit = np.random.normal(self.avg_visit, self.std_visit)

        # Return an integer
        return np.floor(visit)
