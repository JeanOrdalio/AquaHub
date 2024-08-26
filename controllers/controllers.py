from requests import get,post
from flask import request,redirect,url_for
from flask_login import current_user,login_required
from models.models import Device
from __init__ import db,app
import pandas as pd 



class Sensor_state():

    def __init__(self,sensor):
        self.sensor = sensor
    
    def state(sensor):
        url = "http://192.168.2.239:8123/api/states"
        headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxYjVhNTQ5NmEzNmM0MWYyOWRmY2I1NDg1MGEwYTBlOCIsImlhdCI6MTcyMzkwODI5OSwiZXhwIjoyMDM5MjY4Mjk5fQ.J0C6-KurkkgVUxT_61_3cX4qIgKWMH1MJm5sS9GnlVI",
        "content-type": "application/json",
        }

        response = get(url, headers=headers)
        data = response.json()
        df= pd.DataFrame(data)[['entity_id','state']]
        df = df = df[df['entity_id'] == (f'{sensor}')] 
        for c in df['state']:
            valor = c 
        return valor



class Reles ():
    rele1 = "switch.sensor_temperatura_e_umidade"


    def __init__(self,rele1):
        self.rele1 = rele1


class Sensor():
    sensorhum = "sensor.sensor_dht11_humidity"
    sensor2 =  "sensor.sensor_dht11_temperature"
    sensor1 = "sensor.sensor_ds18b20_temperature"


    def __init__(self,sensorhum, sensor1,sensor2):
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensorhum = sensorhum

class Auto_rele():

    def __init__(self,hora, rele, name,status):
        self.hora = hora
        self.rele = rele
        self.name = name
        self.status = status


        

    def automacao_hora(hora,name,status,autor):

        url = (f"http://192.168.2.239:8123/api/config/automation/config/{name}")
        headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxYjVhNTQ5NmEzNmM0MWYyOWRmY2I1NDg1MGEwYTBlOCIsImlhdCI6MTcyMzkwODI5OSwiZXhwIjoyMDM5MjY4Mjk5fQ.J0C6-KurkkgVUxT_61_3cX4qIgKWMH1MJm5sS9GnlVI",
        "content-type": "application/json",
        }

        automation_data = {
        "alias": (f"{autor}_{name}"),
        "trigger": [
            {
                "platform": "time",
                "at": (f"{hora}")
            }
        ],
        "action": [
            {
                "service": (f"switch.turn_{status}"),
                "target": {
                    "entity_id":"switch.sensor_temperatura_e_umidade"
                }
            }
        ]
        }

        response = post(url, json=automation_data, headers=headers)

        
      

class Sensor_log():
     

    def __init__(self,sensor):
        self.sensor = sensor

    def sensor_get(sensor):
        url = (f"http://192.168.2.239:8123/api/history/period?filter_entity_id={sensor}")
        headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxYjVhNTQ5NmEzNmM0MWYyOWRmY2I1NDg1MGEwYTBlOCIsImlhdCI6MTcyMzkwODI5OSwiZXhwIjoyMDM5MjY4Mjk5fQ.J0C6-KurkkgVUxT_61_3cX4qIgKWMH1MJm5sS9GnlVI",
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


def buscar_auto():
    try:
        url = "http://192.168.2.239:8123/api/states"
        headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxYjVhNTQ5NmEzNmM0MWYyOWRmY2I1NDg1MGEwYTBlOCIsImlhdCI6MTcyMzkwODI5OSwiZXhwIjoyMDM5MjY4Mjk5fQ.J0C6-KurkkgVUxT_61_3cX4qIgKWMH1MJm5sS9GnlVI",
        "content-type": "application/json",
        }

        response = get(url, headers=headers)
        data = response.json()
        df= pd.DataFrame(data)

        df = df[['entity_id','state','context']]
        df['id'] = df['context'].apply(lambda x: x['id'])
        df = df[['entity_id','state','id']]
        automaçoes = pd.DataFrame()
        for c in df['entity_id']:
            if "automation" in c:
                automaçoes = automaçoes._append(df[df['entity_id'] == (f'{c}')])
        automaçoes['disp'] = automaçoes['entity_id'].map(lambda x: x.lstrip('automation.'))
        automaçoes['disp'] = automaçoes['disp'].str.split('_').str[0]
        automaçoes['disp'] = automaçoes['disp'].str.replace('qw',"")
        automaçoes['entity_id'] = automaçoes['entity_id'].str.split('qw').str[1]
        automaçoes['entity_id'] = automaçoes['entity_id'].str.replace("_"," ")
    
    
        return(automaçoes)
    except:
        pass



        
