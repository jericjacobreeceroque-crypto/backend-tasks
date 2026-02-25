import json, csv

with open('employees.json', 'r') as employees_json:
    data = json.load(employees_json)
    fieldNames = ['first_name', 'last_name', 'city']

    print(data)

with open('csv_employees.csv', 'w', newline='') as employees_csv:
    csv_writer = csv.DictWriter(employees_csv, fieldnames=fieldNames)

    csv_writer.writeheader()
    csv_writer.writerows(data)