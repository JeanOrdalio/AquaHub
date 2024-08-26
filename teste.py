from requests import get

import pandas as pd 








url = "http://192.168.2.239:8123/api/states"
headers = {
"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxYjVhNTQ5NmEzNmM0MWYyOWRmY2I1NDg1MGEwYTBlOCIsImlhdCI6MTcyMzkwODI5OSwiZXhwIjoyMDM5MjY4Mjk5fQ.J0C6-KurkkgVUxT_61_3cX4qIgKWMH1MJm5sS9GnlVI",
"content-type": "application/json",
}
# Enviar a solicitação GET
response = get(url, headers=headers)

# Verifica o status da resposta
if response.status_code == 200:
    data = response.json()
    # Filtrar para obter apenas as automações
    automations = [entity for entity in data if entity['entity_id'].startswith('automation.')]
    print('Automatizações:', automations)
else:
    print(f'Falha ao listar automações: {response.status_code} - {response.text}')