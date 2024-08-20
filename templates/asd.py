


import pandas as pd 
import requests
import json



url = "http://192.168.2.203:8123/api/states"
headers = {
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmOGYwMzQ2YjAwYTc0Yjk4OTE3Nzk3NWE0ODVlYjk3YSIsImlhdCI6MTcyMjM1MTkwNiwiZXhwIjoyMDM3NzExOTA2fQ.xk0IJe0aSD4w_ulQwJJBSxKAph8R925xyMx3-j7UZSM",
"content-type": "application/json",
}

response = requests.get(url, headers=headers)
data = response.json()

df= pd.DataFrame(data)
df = df[['entity_id','state']]
print (df)
