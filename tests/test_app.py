from app import visit

# Normal
# http://127.0.0.1:8000/visit/?store_name=Lille&year=2023&month=9&day=13&sensor_id=0


def test_with_sensor():
    visit_number = visit("Lille", 2023, 9, 13, 1)
    assert 247 == visit_number.body


# without sensor_id
# http://127.0.0.1:8000/visit/?store_name=Lille&year=2023&month=9&day=13


def test_without_sensor_id():
    visit_number = visit("Lille", 2023, 9, 13)
    assert 2473 == visit_number.body


# Normal
# http://127.0.0.1:8000/visit/?store_name=Lille&year=2023&month=9&day=10&sensor_id=0


def test_closed_store():
    visit_number = visit("Lille", 2023, 9, 10, 0)
    assert "The store was closed try another date" == visit_number.body


# Store name not found
# http://127.0.0.1:8000/visit/?store_name=Arras&year=2023&month=9&day=13&sensor_id=0


def test_store_name():
    visit_number = visit("Arras", 2023, 9, 13, 0)
    assert "Store Not found" == visit_number.body


# Sensor_id not found
# http://127.0.0.1:8000/visit/?store_name=Lille&year=2023&month=9&day=13&sensor_id=-1


def test_sensor_id_negative():
    visit_number = visit("Lille", 2023, 9, 13, -1)
    assert "Sensor_id Not Found. It must be between 0 and 7" == visit_number.body

    # Sensor_id not found


# http://127.0.0.1:8000/visit/?store_name=Lille&year=2023&month=9&day=13&sensor_id=8


def test_sensor_id_not_found():
    visit_number = visit("Lille", 2023, 9, 13, 8)
    assert "Sensor_id Not Found. It must be between 0 and 7" == visit_number.body


# Year before 2020
# http://127.0.0.1:8000/visit/?store_name=Lille&year=2019&month=9&day=13&sensor_id=0


def test_year_before_2020():
    visit_number = visit("Lille", 2019, 9, 13, 0)
    assert "No data before 2020" == visit_number.body


# Choose a correct date
# http://127.0.0.1:8000/visit/?store_name=Lille&year=2023&month=2&day=31&sensor_id=0


def test_incorrect_date():
    visit_number = visit("Lille", 2023, 2, 31, 0)
    assert "Enter a valid date" == visit_number.body


# date in futur
# http://127.0.0.1:8000/visit/?store_name=Lille&year=2025&month=2&day=15&sensor_id=0


def test_date_in_futur():
    visit_number = visit("Lille", 2025, 9, 13, 0)
    assert "Choose a date in the past" == visit_number.body
