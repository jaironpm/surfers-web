from enum import Enum, unique
from flask import current_app as app

@unique
class API_URL(Enum):
    ALERTS = f"http://{app.config['API_HOST']}:{app.config['API_PORT']}/api/v1/weather/alert"
    SWELL = f"http://{app.config['API_HOST']}:{app.config['API_PORT']}/api/v1/surf/swell/"
    WATER = f"http://{app.config['API_HOST']}:{app.config['API_PORT']}/api/v1/surf/water/"
    LOCATION = f"http://{app.config['API_HOST']}:{app.config['API_PORT']}/api/v1/weather/locations/"
    WEATHER_CURRENT = f"http://{app.config['API_HOST']}:{app.config['API_PORT']}/api/v1/weather/observation/"
    HEALTHZ = f"http://{app.config['API_HOST']}:{app.config['API_PORT']}/api/v1/healthz"

    def set_location(self, locationid):
        _url = f"{self.value}{locationid}"
        return _url
