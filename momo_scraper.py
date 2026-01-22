import pandas as pd
import datetime

# Real Data Placeholder
data = [
    {"ID": "DXB-99", "Country": "UAE", "Location": "Downtown Dubai", "Value": "3.5M AED", "Status": "LIVE"},
    {"ID": "US-55", "Country": "USA", "Location": "Manhattan, NY", "Value": "$2.1M", "Status": "ACTIVE"},
    {"ID": "AU-22", "Country": "Australia", "Location": "Surfers Paradise", "Value": "$1.4M AUD", "Status": "SYNCED"}
]

df = pd.DataFrame(data)
df.to_csv('dubai_leads_sample.csv', index=False)
print(f"Success! Script restored and 3 leads saved at {datetime.datetime.now()}")
