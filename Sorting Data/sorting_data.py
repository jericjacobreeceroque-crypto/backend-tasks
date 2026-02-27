import pandas as pd
import json

with open ('Sorting Data/json_customers.json', 'r') as customers_json:
    data = json.load(customers_json)
    df = pd.DataFrame(data)
    
    result = df.sort_values(
        by=['Last Name', 'First Name'], 
        ascending = [False, True]
        )[['First Name', 'Last Name']]
        
    print(result.head(10))