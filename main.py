import json
import pandas as pd
from datetime import datetime

with open("input.json","r", encoding="utf-8") as file:
    payload = json.load(file)

 
df = pd.DataFrame(pd.read_csv("Table.csv",sep=";"))
print(df.head())


