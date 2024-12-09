import json

def task() -> float:
    sum_res = 0
    filename = 'input.json'

    with open(filename) as file:
        data = json.load(file)

    for date in data:
        sum_res += date['score'] * date['weight']

    return round(sum_res, 3)

print(task())