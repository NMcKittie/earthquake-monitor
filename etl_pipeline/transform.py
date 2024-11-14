"""Normalise and standardise the data being retrieved from the database."""


from geopy.geocoders import Nominatim
import pandas as pd

from extract import extract_earthquakes


def flatten_data(earthquakes: list[dict]) -> list[dict]:
    """Flatten each earthquake json data so all columns are the keys."""

    earthquake_properties = []

    for earthquake in earthquakes:

        earthquake_property = earthquake.get('properties')
        geometry = earthquake.get('geometry')
        latitude = geometry.get('coordinates')[1]
        longitude = geometry.get('coordinates')[0]
        depth = geometry.get('coordinates')[2]
        earthquake_id = earthquake.get('id')

        extras = {'lat': latitude, 'lon': longitude,
                  'depth': depth, 'quake_id': earthquake_id}

        earthquake_property.update(extras)

        earthquake_properties.append(earthquake_property)

    return earthquake_properties


def pandas_clean_data(earthquakes: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardise the data using pandas."""

    earthquakes = earthquakes.drop(columns=['tz', 'url', 'detail', 'mmi',
                                            'sig', 'code', 'ids', 'sources',
                                            'types', 'rms', 'dmin', 'title',
                                            'updated', 'cdi'])
    earthquakes['time'] = earthquakes.time.apply(lambda x: str(x)[:-3])
    earthquakes['time'] = pd.to_datetime(earthquakes['time'], unit='s')
    earthquakes['felt'] = earthquakes['felt'].fillna(0)
    earthquakes['alert'] = earthquakes['alert'].fillna('No alert')
    return earthquakes


def transform(earthquakes: list[dict]) -> pd.DataFrame:

    earthquakes = flatten_data(earthquakes)
    earthquakes = pd.DataFrame(earthquakes)
    earthquakes = pandas_clean_data(earthquakes)

    return earthquakes


if __name__ == "__main__":

    earthquakes = extract_earthquakes()
    earthquakes = flatten_data(earthquakes)
    earthquakes = pd.DataFrame(earthquakes)
    earthquakes.to_csv("all_e.csv", encoding='utf-8', index=False)

    """
    geolocator = Nominatim(user_agent="nathan_earthquake_monitor")
    location = geolocator.geocode("Constitución, Chile")
    json = location.raw
    lat = json['lat']
    lon = json['lon']
    print(lat)
    print(lon)
    location = geolocator.reverse(f"{lat}, {lon}")
    print(location.raw)
    """
