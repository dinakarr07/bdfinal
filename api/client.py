from polygon import RESTClient
import config
import json
from typing import cast
from urllib3 import HTTPResponse
import pandas as pd

client = RESTClient(config.polygon_api)

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        'AAPL',
        1,
        'day',
        '2023-01-01',  # Start date in correct string format
        '2024-11-30',  # End date in correct string format
        raw=True
    ),
)

data = json.loads(aggs.data)
#print(data)

# Assuming 'data' contains a 'results' key with the data you're interested in
results = data.get('results', [])

# Convert the data to a pandas DataFrame
df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
df.to_csv('aapl_stock_data.csv', index=False)

# Print confirmation message
print("Data saved to 'aapl_stock_data.csv'")