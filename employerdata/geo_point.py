from geopy import distance, Point

class GeoPoint(Point):
    def __add__(self, other):
        return GeoPoint(self.latitude + other.latitude,
                        self.longitude + other.longitude)

    def __sub__(self, other):
        return GeoPoint(self.latitude - other.latitude,
                        self.longitude - other.longitude)

    def __mul__(self, scalar):
        return GeoPoint(scalar * self.latitude,
                        scalar * self.longitude)

    __rmul__ = __mul__

    def direct_distance_from(self, other):
        return round(distance.distance(self, other).meters)
