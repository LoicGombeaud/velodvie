import polyline
from employerdata.geo_point import GeoPoint

class OverviewPolyline:
    ENRICHMENT_DISTANCE = 1

    def __init__(self, base64):
        self.geo_points = []
        for geo_point in polyline.decode(base64):
            self.geo_points.append(GeoPoint(*geo_point))

    def get_enriched_geo_points(self, enrichment_distance=ENRICHMENT_DISTANCE):
        try:
            return self.enriched_geo_points
        except AttributeError:
            pass

        self.enriched_geo_points = []

        for i in range(len(self.geo_points) - 1):
            current_point = self.geo_points[i]
            self.enriched_geo_points.append(current_point)

            next_point = self.geo_points[i+1]
            distance_to_next_point = current_point.direct_distance_from(next_point)
            if distance_to_next_point > self.ENRICHMENT_DISTANCE:
                num_points_to_add = round(distance_to_next_point / self.ENRICHMENT_DISTANCE)
                for j in range(1, num_points_to_add):
                    vector = next_point - current_point
                    step = vector * (j / (num_points_to_add + 1))
                    extra_point = current_point + step
                    self.enriched_geo_points.append(extra_point)

        return self.enriched_geo_points
