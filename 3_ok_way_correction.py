import json
from pathlib import Path
from typing import List, Literal, Tuple, TypedDict


def load_data():
    data = Path("data/data.json")
    return json.loads(data.read_text())


class Geometry(TypedDict):
    type: Literal["Polygon"]
    coordinates: List[Tuple[float, float]]


class Feature(TypedDict):
    type: Literal["Feature"]
    geometry: Geometry
    properties: dict


class GeoJson:
    def __init__(self, features: List[Feature]) -> None:
        self.features = features

    def extract(self) -> None:
        geojson = {"type": "FeatureCollection", "features": self.features}

        output_path = Path("./output.json")
        output_path.write_text(json.dumps(geojson))


data = load_data()

features: List[Feature] = [  # type the incoming variable
    {
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": [d]},
        "properties": {},
    }
    for d in data
]

GeoJson(features).extract()
