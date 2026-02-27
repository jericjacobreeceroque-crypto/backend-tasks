import csv, json

with open('CSV to JSON/customers-10000.csv', 'r') as customers_csv:
    csv_reader = csv.DictReader(customers_csv)

    lines = list(csv_reader)
    
    # for line in csv_reader:
    #     print(line)

with open('CSV to JSON/json_customers.json', 'w') as customers_json:
    json.dump(lines, customers_json, indent=4)

