import json

with open("debug/dataset.json") as f:
    data = json.loads(f.read())

correct_data = []
incorrect_data = []
for feature in data["features"]:
    correct_data.append(
        [coordinate for coordinate in feature["geometry"]["coordinates"][0]]
    )
    incorrect_data.append(
        [[coordinate[0]] for coordinate in feature["geometry"]["coordinates"][0]]
    )

with (
    open("data/correct_data.json", "w") as correct,
    open("data/data.json", "w") as incorrect,
):
    correct.write(json.dumps(correct_data))
    incorrect.write(json.dumps(incorrect_data))
