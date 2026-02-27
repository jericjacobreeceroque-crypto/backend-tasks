import json, csv

with open('JSON to CSV/titanic_passengers.json', 'r') as passengers_json:
    data = json.load(passengers_json)
    fieldNames = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

    # print(data)

with open('JSON to CSV/csv_titanic_passengers.csv', 'w', newline='') as passenger_csv:
    csv_writer = csv.DictWriter(passenger_csv, fieldnames=fieldNames)

    csv_writer.writeheader()
    csv_writer.writerows(data)