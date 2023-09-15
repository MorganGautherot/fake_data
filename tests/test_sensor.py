import os, sys

# Get the parent directory
parent_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from sensor import VisitSensor
from datetime import date


def test_monday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.get_visit(date(2023, 9, 11))


def test_tuesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.get_visit(date(2023, 9, 12))


def test_wednesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.get_visit(date(2023, 9, 13))


def test_thursday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.get_visit(date(2023, 9, 14))


def test_friday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.get_visit(date(2023, 9, 15))


def test_saturday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.get_visit(date(2023, 9, 16))


def test_sunday_closed():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 == visit_sensor.get_visit(date(2023, 9, 17))
