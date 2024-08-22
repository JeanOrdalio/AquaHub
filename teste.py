from requests import get

import pandas as pd 



url = "http://192.168.2.239:8123/api/states"
headers = {
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxYjVhNTQ5NmEzNmM0MWYyOWRmY2I1NDg1MGEwYTBlOCIsImlhdCI6MTcyMzkwODI5OSwiZXhwIjoyMDM5MjY4Mjk5fQ.J0C6-KurkkgVUxT_61_3cX4qIgKWMH1MJm5sS9GnlVI",
"content-type": "application/json",
}

response = get(url, headers=headers)
data = response.json()
df= pd.DataFrame(data)

df = df[['entity_id','state']]
automaçoes = pd.DataFrame()
for c in df['entity_id']:
    if "automation" in c:
        automaçoes = automaçoes._append(df[df['entity_id'] == (f'{c}')])
print(automaçoes)




       


