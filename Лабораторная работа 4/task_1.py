import json

input_file = "input.json"

def task() -> float:
    with open(input_file) as f:
        data = json.load(f)

    d = 0
    for i in data:
        d += i["score"]*i["weight"]
    return round(d, 3)

print(task())
