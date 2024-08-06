from requests import get
from flask import request,redirect,url_for
from flask_login import current_user,login_required
from models.models import Device
from __init__ import db,app
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
        url = (f"http://192.168.2.203:8123/api/history/period?filter_entity_id={sensor}")
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
        df['Hora'] = df['last_updated'].dt.strftime(('%H:%M'))
        df['Estado'] = df['state']
        df = df = df[df['state'] != 'unavailable'] 
        df = df = df[df['state'] != 'unknown']
        df = df = df[df['state'] != '']

        df = df[['Data','Hora','Estado']]

       

        return df
    

@app.route('/executor_rele_name', methods=['POST'])
@login_required
def executor_rele_name():

    salvar =  salvar_name_rele()
    print('456')
    return salvar


def salvar_name_rele():

    user = current_user.name
    device = Device.query.filter_by(user = user ).first()
    
    name_rele01 = request.form['rele1']
    name_rele02 = request.form['rele2']
    
    name_rele03 = request.form['rele3']
    name_rele04 = request.form['rele4']
    if name_rele01 == "":
        pass
    else:
        device.name_rele1 = name_rele01
        db.session.commit()
    if name_rele02 == "":
        pass
    else:
        device.name_rele2 = name_rele02
        db.session.commit()
    if name_rele03 == "":
        pass
    else:   
        device.name_rele3 = name_rele03
        db.session.commit()
    if name_rele04 == "":
        pass
    else:
        device.name_rele4 = name_rele04
        db.session.commit()
    
    db.session.commit()
    print('123')
    return redirect(url_for('configs'))



@app.route('/executor_rele1', methods=['POST'])
@login_required
def executor():
    resultado = alternar_reles()

    return resultado

def alternar_reles():
    
    user = current_user.name
    data_rele = Device.query.filter_by(user = user ).first()
    
    if data_rele.rele1 == "1":
        data_rele.rele1 = "0"
        db.session.commit()
        return redirect(url_for('reles'))
    if data_rele.rele1 == "0":
        data_rele.rele1 = "1"
        db.session.commit()
        return redirect(url_for('reles'))




@app.route('/executor_sensor_name', methods=['POST'])
@login_required
def executor_sensor_name():

    salvar =  salvar_name_sensor()
    print('456')
    return salvar

def salvar_name_sensor():
  


    user = current_user.name
    device = Device.query.filter_by(user = user ).first()
    
    name_sensor01 = request.form['sensor1']
    name_sensor02 = request.form['sensor2']
    name_sensor_hum = request.form['sensorhum']
    if name_sensor01 == "":
        pass
    else:
        device.name_sensor_temp01 = name_sensor01
        db.session.commit()
    if name_sensor02 =="":
        pass
    else:
        device.name_sensor_temp02 = name_sensor02
        db.session.commit()
    if name_sensor_hum == "":
        pass
    else:
        device.name_sensor_hum = name_sensor_hum
        db.session.commit()
  
    return redirect(url_for('configs'))

