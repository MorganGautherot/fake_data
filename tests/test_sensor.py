from fake_data_app.sensor import VisitSensor
from datetime import date


def test_monday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit(date(2023, 9, 11))


def test_tuesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit(date(2023, 9, 12))


def test_wednesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit(date(2023, 9, 13))


def test_thursday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit(date(2023, 9, 14))


def test_friday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit(date(2023, 9, 15))


def test_saturday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit(date(2023, 9, 16))


def test_sunday_closed():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 == visit_sensor.simulate_visit(date(2023, 9, 17))


def test_with_break():
    visit_sensor = VisitSensor(1200, 300, perc_break=10)
    print(visit_sensor.get_visit(date(2023, 10, 22)))
    assert 0 == visit_sensor.get_visit(date(2023, 11, 28))


def test_without_break():
    visit_sensor = VisitSensor(1200, 300, perc_break=0)
    assert 0 != visit_sensor.get_visit(date(2023, 11, 28))

def test_with_malfunction():
    visit_sensor = VisitSensor(1200, 300, perc_malfunction=10)
    assert 834 == visit_sensor.get_visit(date(2023, 11, 28))


def test_without_malfunction():
    visit_sensor = VisitSensor(1200, 300, perc_malfunction=0)
    assert 1192 == visit_sensor.get_visit(date(2023, 11, 28))
