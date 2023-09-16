from fake_data_app import create_app
from fastapi import FastAPI, Response
from datetime import date

store_dict = create_app()

app = FastAPI()
@app.get("/visit/")
def visit(store_name: str, year: int, month: int, day: int, sensor_id: int | None = None):

    # If the store is the dictionnary
    if not(store_name in store_dict.keys()):
        return 'Store Not found'
    
    # Check the value of sensor_id
    if sensor_id and (sensor_id > 7 or sensor_id < 0):
        return 'Sensor_id Not Found. It must be between 0 and 7'
    
    # Check the year
    if year < 2020:
        return 'No data before 2020'
    
    # Check the date
    try: 
        date(year, month, day)
    except:
        return 'Enter a valid date'
    
    # Check the date is in the past
    if date.today() < date(year, month, day):
        return 'Choose a date in the past'

    # If no sensor choose return the visit for the whole store
    if sensor_id is None:
        visit = store_dict[store_name].get_all_traffic(date(year, month, day))
    else :
        visit = store_dict[store_name].get_sensor_traffic(sensor_id,
                                                          date(year, month, day))

    if visit < 0:
        return 'The store was closed try another date'
        
    return visit


