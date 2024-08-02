from requests import get
import pandas as pd





class Sensor():
    sensorhum = "sensor.sensor_dht11_humidity"
    sensor2 =  "sensor.sensor_dht11_temperature"
    sensor1 = "sensor.sensor_ds18b20_temperature"


    def __init__(self,sensorhum, sensor1,sensor2):
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensorhum = sensorhum



class Sensor_Get():
     

    def __init__(self,sensor):
        self.sensor = sensor

    def sensor_get(sensor):
        url = (f"http://192.168.2.156:8123/api/history/period?filter_entity_id={sensor}")
        headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmOGYwMzQ2YjAwYTc0Yjk4OTE3Nzk3NWE0ODVlYjk3YSIsImlhdCI6MTcyMjM1MTkwNiwiZXhwIjoyMDM3NzExOTA2fQ.xk0IJe0aSD4w_ulQwJJBSxKAph8R925xyMx3-j7UZSM",
    "content-type": "application/json",
    }

        
        response = get(url, headers=headers)
        data = response.json()
        if data:
            sensor_data = data[0]
        
        df= pd.DataFrame(sensor_data)[['last_updated','state']]

        df['last_updated']= pd.to_datetime(df['last_updated'],format='mixed')
        df.set_index('last_updated', inplace=True)
        df = df.resample('2min').first().dropna().reset_index()

        df['last_updated'] = df['last_updated'].dt.tz_convert('America/Sao_Paulo')
        df['Data'] = df['last_updated'].dt.strftime(('%Y-%m-%d'))
        df['Hora'] = df['last_updated'].dt.strftime(('%H:%M:%S'))
        df['Estado'] = df['state']
        df = df = df[df['state'] != 'unavailable'] 
        df = df = df[df['state'] != 'unknown']

        df = df[['Data','Hora','Estado']]

       

        return df
    



