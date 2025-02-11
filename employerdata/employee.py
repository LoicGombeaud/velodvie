import googlemaps

from employerdata import config
from employerdata.geo_point import GeoPoint
from employerdata.overview_polyline import OverviewPolyline

gmaps = googlemaps.Client(config.google_maps_api_key())

class Employee:
    def __init__(self, employer, street_address):
        self.employer, self.street_address = employer, street_address

    def get_geo_point(self):
        try:
            return self.geo_point
        except AttributeError:
            self.populate()
            return self.geo_point

    def get_direct_distance(self):
        try:
            return self.direct_distance
        except AttributeError:
            self.populate()
            return self.direct_distance

    def get_cycling_distance(self):
        try:
            return self.cycling_distance
        except AttributeError:
            self.populate()
            return self.cycling_distance

    def get_overview_polyline(self):
        try:
            return self.overview_polyline
        except AttributeError:
            self.populate()
            return self.overview_polyline

    def populate(self):
        gmaps_result = gmaps.directions(self.street_address,
                                        self.employer.street_address,
                                        mode='bicycling',
                                        units='metric')

        start_location = gmaps_result[0]['legs'][0]['start_location']
        self.geo_point = GeoPoint(start_location['lat'],
                                  start_location['lng'])

        self.direct_distance = self.geo_point.direct_distance_from(self.employer.get_geo_point())

        self.cycling_distance = gmaps_result[0]['legs'][0]['distance']['value']

        self.overview_polyline = OverviewPolyline(gmaps_result[0]['overview_polyline']['points'])
