
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    lst = []
    with open (INPUT_FILENAME) as f:
        csv_f = csv.DictReader(f)
        for line in csv_f:
           lst.append(dict(line))

    with open(OUTPUT_FILENAME, 'w') as f1:
        jsn_f = (json.dumps(lst, indent=4))
        print(jsn_f)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
