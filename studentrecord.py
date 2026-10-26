import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read CSV file
print("CSV Records:")
with open(os.path.join(BASE_DIR, "students.csv"), "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(",".join(row))

# Read JSON file
print("\nJSON Records:")
with open(os.path.join(BASE_DIR, "students.json"), "r") as file:
    data = json.load(file)
    for student in data:
        print(student)