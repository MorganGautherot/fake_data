from fake_data_app.store import StoreSensor
from datetime import date


def create_app() -> dict:
    """Create the store of the API"""

    # Name of the store
    store_name = ["Lille", "Paris", "Lyon", "Toulouse", "Marseille"]
    # Average of visit per store
    store_avg_visit = [3000, 8000, 6000, 2000, 1700]
    # Standard deviation per store
    store_std_visit = [500, 800, 500, 400, 100]
    # Percentage of sensor malfunction per store
    perc_malfunction = [5, 10, 8, 5, 5]
    # Percentage of sensor default per store
    perc_break = [5, 8, 5, 2, 0]
    # Dictionnary where the store are saved
    store_dict = dict()

    for i in range(len(store_name)):
        store_dict[store_name[i]] = StoreSensor(
            store_name[i],
            store_avg_visit[i],
            store_std_visit[i],
            perc_malfunction[i],
            perc_break[i],
        )
    return store_dict
