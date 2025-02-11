import googlemaps
import json
from jinja2 import Environment, PackageLoader

from employerdata import config
from employerdata.employee import Employee
from employerdata.geo_point import GeoPoint

gmaps = googlemaps.Client(config.google_maps_api_key())

class Employer:
    def __init__(self, name, street_address):
        self.name, self.street_address = name, street_address
        self.geo_point = self.get_geo_point()
        self.employees = []

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        employee_addresses = list(map(lambda e: e.street_address, self.employees))
        return self.name + ": " + "; ".join(map(str, employee_addresses))

    def get_geo_point(self):
        try:
            return self.geo_point
        except AttributeError:
            gmaps_result = gmaps.geocode(self.street_address)
            self.geo_point = GeoPoint(gmaps_result[0]['geometry']['location']['lat'],
                                      gmaps_result[0]['geometry']['location']['lng'])
            return self.geo_point

    def add_employee(self, employee_street_address):
        self.employees.append(Employee(self, employee_street_address))

    def get_direct_distances(self):
        direct_distances = []
        for employee in self.employees:
            direct_distances.append(employee.get_direct_distance())
        return direct_distances

    def get_cycling_distances(self):
        cycling_distances = []
        for employee in self.employees:
            cycling_distances.append(employee.get_cycling_distance())
        return cycling_distances

    def get_heatmap_geo_points(self):
        heatmap_geo_points = []
        for employee in self.employees:
            heatmap_geo_points.extend(employee.get_overview_polyline().get_enriched_geo_points())
        return heatmap_geo_points

    def get_heatmap_points_json(self):
        heatmap_points_json_list = list(map(lambda geo_point: [geo_point.latitude,
                                                               geo_point.longitude],
                                                self.get_heatmap_geo_points()))
        return json.dumps(heatmap_points_json_list)

    def generate_html(self):
        env = Environment(loader=PackageLoader('employerdata', 'templates'))
        template = env.get_template('index.html.j2')
        return template.render(employer_name=self.name,
                               employer_latitude=self.geo_point.latitude,
                               employer_longitude=self.geo_point.longitude,
                               heatmap_points=self.get_heatmap_points_json())
