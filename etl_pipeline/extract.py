"""Extract earthquake data as a JSON from the USGS."""

import requests
import pandas as pd


class APIError(Exception):
    """Describes an error triggered by a failing API call."""

    def __init__(self, message: str, code: int = 500):
        """Creates a new APIError instance."""
        self.message = message
        self.code = code


def extract_earthquakes() -> list[dict]:
    """Get all earthquake data over the last hour in geojson format.
    Returns a list of dictionaries."""

    # url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        raise APIError("Unable to locate any earthquakes.",
                       response.status_code)
    if response.status_code != 200:
        raise APIError("Unable to connect to server.", response.status_code)

    earthquakes = response.json()

    earthquakes = earthquakes['features']

    if not earthquakes:
        return []
    else:
        return earthquakes


if __name__ == "__main__":
    extract_earthquakes()
