import pandas as pd
import json

with open('Filtering Data/json_customers.json', 'r') as customers_json:
    data = json.load(customers_json)
    df = pd.DataFrame(data)
    
    print(df.loc[(df['Country'] == 'Philippines'), ['First Name', 'Last Name', 'Country']])