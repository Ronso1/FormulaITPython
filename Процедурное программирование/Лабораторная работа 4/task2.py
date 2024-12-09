import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME) as file:
        reader = csv.DictReader(file)
        new_dictionary = list(reader)

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(new_dictionary, file, indent=4)

if __name__ == '__main__':

    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
