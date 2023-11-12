import json


def task() -> float:
    with open("input.json", "r") as f:
        json_data = json.load(f)
        return round(sum(item["score"] * item["weight"] for item in json_data), 3)


print(task())
