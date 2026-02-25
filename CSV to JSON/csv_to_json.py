import csv, json

with open('employees.csv', 'r') as employees_csv:
    csv_reader = csv.DictReader(employees_csv)

    lines = list(csv_reader)
    
    # for line in csv_reader:
    #     print(line)

with open('converted_employees.json', 'w') as employees_json:
    json.dump(lines, employees_json, indent=4)

