import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        csv_data = csv.DictReader(f)
        json_data = [row for row in csv_data]
        with open(OUTPUT_FILENAME, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

if __name__ == '__main__':
    # Вызов функции конвертации
    task()

    # Чтение и вывод содержимого JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
