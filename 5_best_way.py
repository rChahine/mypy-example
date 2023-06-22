import json
from pathlib import Path
from typing import List, Literal, Tuple, Any, Mapping

import pydantic


def load_data() -> Any:
    data = Path("./data.json")
    return json.loads(data.read_text())


class Geometry(pydantic.BaseModel):
    type: Literal["Polygon"]
    coordinates: List[Tuple[float, float]]


class Feature(pydantic.BaseModel):
    type: Literal["Feature"]
    geometry: Geometry
    properties: Mapping[str, Any]


class GeoJson:
    def __init__(self, features: List[Feature]) -> None:
        self.features = features

    def extract(self) -> None:
        geojson = {"type": "FeatureCollection", "features": self.features}

        output_path = Path("./output.json")
        output_path.write_text(json.dumps(geojson))


data = load_data()

features = [  # type the incoming variable
    Feature(type="Feature", geometry=Geometry(type="Polygon", coordinates=[d]), properties={})
    for d in data
]

GeoJson(features).extract()
