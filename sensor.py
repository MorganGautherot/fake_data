import numpy as np
from datetime import date


class VisitSensor:
    def __init__(self, avg_visit: int, std_visit: int) -> None:
        """Intialize sensor"""
        self.avg_visit = avg_visit
        self.std_visit = std_visit

    def get_visit(self, date: date) -> int:
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
