from pathlib import Path
import json


def load_data():
    data = Path("data/data.json")
    return json.loads(data.read_text())


class GeoJson:
    def __init__(self, features) -> None:
        self.features = features

    def extract(self):
        geojson = {"type": "FeatureCollection", "features": self.features}

        output_path = Path("./output.json")
        output_path.write_text(json.dumps(geojson))


data = load_data()

features = [
    {
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": [d]},
        "properties": {},
    }
    for d in data
]
GeoJson(features).extract()
