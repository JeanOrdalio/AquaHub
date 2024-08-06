from __init__ import app
from flask import render_template,request,redirect,url_for
from models.models import User,Device,Keys,Device_log
from  __init__ import db,mqtt_client,cache
from flask_login import login_user, logout_user,login_required,current_user
from controllers.controllers import Sensor,Sensor_Get
import json




def get_user():
    user_data = current_user
    
    return user_data

@app.route('/',methods= ['GET','POST'])
def login():
    
    if request.method == 'POST':
            
        email = request.form['email']
        password = request.form['password']

        user =  User.query.filter_by(email = email).first()
        
        
        if user and user.password == password:
            name= user.name
            mqtt_client.subscribe(f'{name}/reles/rele1')
            
            login_user(user)

            mqtt_client.publish(f'{name}/controle',user.name)
           
            return redirect(url_for('dashboard')) 
        return redirect(url_for('login'))
            
    
        
           
                
    return render_template('home.html')
                    

@app.route('/registrar',methods= ['GET','POST'])
def registrar():
   
    
   
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        cep = request.form['cep']
        password = request.form['password']
        key = request.form['device']
        key_verify = Keys.query.filter_by( key = key ).first()
        acess = str(key_verify.key)
        rele1 = "1"
        temp = "0"
        if key == acess:
        
            user = User(name,email,cep,password,key)
            device = Device(name,rele1,temp)
            
            db.session.add(user)
            db.session.add(device)
            db.session.commit() 
            
            return redirect(url_for('login'))
             
             

    return render_template('registrar.html')

 
@app.route('/logout')
def logout():
    logout_user()
    print("saindo")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    try:
        data_hum = Sensor_Get.sensor_get(Sensor.sensorhum)
        sensorhum_json = data_hum.to_json(orient='records')
        sensorhum_json = json.loads(sensorhum_json)
        
        
        data_sensor1 = Sensor_Get.sensor_get(Sensor.sensor1)
        sensor1_json = data_sensor1.to_json(orient='records')
        sensor1_json = json.loads(sensor1_json)

        data_sensor2 = Sensor_Get.sensor_get(Sensor.sensor2)
        sensor2_json = data_sensor2.to_json(orient='records')
        sensor2_json = json.loads(sensor2_json)



        data_device = Device.query.filter_by(id = current_user.id).first()
        sensor1_name = data_device.name_sensor_temp01
        sensor2_name = data_device.name_sensor_temp02
        sensorhum_name = data_device.name_sensor_hum
        sensor1 = data_device.sensortemp01
        sensor2 = data_device.sensortemp02
        sensorhum = data_device.sensorhum
        

        

        return render_template('dashboard.html', sensorhum_json = sensorhum_json, sensor1_json = sensor1_json,sensor1_name = sensor1_name,sensor2_name = sensor2_name,sensorhum_name = sensorhum_name,sensor2_json =sensor2_json,data_sensor2 = data_sensor2,sensor1 = sensor1, sensor2 = sensor2, sensorhum = sensorhum)

    except:
        status ="Offline"
        return render_template('dashboard.html',status = status)

    
@app.route('/reles',methods= ['GET','POST'])
@login_required
def reles():
    
    
    try:
        device = Device.query.filter_by(user = current_user.name ).first()
        name_rele1 = device.name_rele1
        name_rele2 = device.name_rele2
        name_rele3 = device.name_rele3
        name_rele4 = device.name_rele4
        if request.method == 'POST' and request.form.rele123:
            print("kabum")
        data_rele = Device.query.filter_by(user = current_user.name ).first()
        rele1 = data_rele.rele1
        if data_rele.rele1 == "0":
            rele1 = "Desligado"
            status = "Online"
            return render_template('reles.html',rele1 = rele1,status = status,name_rele1 = name_rele1,name_rele2 = name_rele2, name_rele3 = name_rele3, name_rele4 = name_rele4,)
        if data_rele.rele1 == "1":
            rele1 = "Ligado"
            status = "Online"
            return render_template('reles.html',rele1 = rele1,status = status,name_rele1 = name_rele1,name_rele2 = name_rele2, name_rele3 = name_rele3, name_rele4 = name_rele4,)  
    except: 
        status = "Offline" 
        rele1 = "Offline"

    return render_template('reles.html',rele1 = rele1,status = status)



@app.route('/configs',methods= ['GET','POST'])
@login_required
def configs():
    user = current_user.name
    device = Device.query.filter_by(user = user ).first()
    name_rele1 = device.name_rele1
    name_rele2 = device.name_rele2
    name_rele3 = device.name_rele3
    name_rele4 = device.name_rele4
    name_sensor_temp1 = device.name_sensor_temp01
    name_sensor_temp2 = device.name_sensor_temp02
    name_sensor_hum = device.name_sensor_hum
   
 


   

    return render_template('configs.html',name_rele1 = name_rele1,name_rele2 = name_rele2, name_rele3 = name_rele3, name_rele4 = name_rele4,name_sensor_temp1 = name_sensor_temp1, name_sensor_hum = name_sensor_hum, name_sensor_temp2 = name_sensor_temp2)
        


   
   
    return render_template('configs.html',name_rele1 = name_rele1,name_rele2 = name_rele2, name_rele3 = name_rele3, name_rele4 = name_rele4,name_sensor_temp1 = name_sensor_temp1, name_sensor_hum = name_sensor_hum, name_sensor_temp2 = name_sensor_temp2)




@login_required
@app.route('/sensores',methods= ['GET','POST'])
def sensores():
    

    sensor1_inf = Sensor_Get.sensor_get(Sensor.sensor1)
    sensor2_inf = Sensor_Get.sensor_get(Sensor.sensor2)
    sensorhum_inf = Sensor_Get.sensor_get(Sensor.sensorhum)

  
  
    sensor1_max = sensor1_inf['Estado'].max()
    sensor1_min = sensor1_inf['Estado'].min()
    
    
    sensor2_max = sensor2_inf['Estado'].max()
    sensor2_min = sensor2_inf['Estado'].min()
    
    
    hum_max = sensorhum_inf['Estado'].max()
    hum_min = sensorhum_inf['Estado'].min()
    

    

    data = Device.query.filter_by(id = current_user.id).first()
    sensor1 = data.sensortemp01
    sensor2 = data.sensortemp02
    sensorhum = data.sensorhum
    name_sensor_temp1 = data.name_sensor_temp01
    name_sensor_temp2 = data.name_sensor_temp02
    name_sensor_hum = data.name_sensor_hum
    
    return render_template('sensores.html',sensor1 = sensor1,sensor2 = sensor2, sensorhum = sensorhum,sensor1_max = sensor1_max,sensor1_min = sensor1_min, sensor2_max = sensor2_max, sensor2_min = sensor2_min, hum_min = hum_min ,hum_max = hum_max,name_sensor_temp1 = name_sensor_temp1, name_sensor_hum = name_sensor_hum, name_sensor_temp2 = name_sensor_temp2)

    

@mqtt_client.on_message()
def receber_mqtt_menssager(client, userdata, message):

 
    payload=message.payload.decode()
    topic=message.topic
    if topic ==(f'{payload}/controle'):
        user = payload
        cache.add("username",user)
        
    
    with app.app_context():

        user = cache.get("username")
        print(user)
        if topic == (f'{payload}/controle'):
            
            data_rele = Device.query.filter_by(user = user ).first()
            print(data_rele.rele1)

            
        topic2 = (f'{user}/reles')
        topic_sensor01 = (f'{user}/sensores/aquario')
        topic_sensor02 =(f'{user}/sensores/terrario')
        topic_sensorhum =(f'{user}/sensores/humidade_terrario')

        if topic == topic2:
            if payload == "off":

                data_rele = Device.query.filter_by(user = user ).first()
                data_rele.rele1 = "0"
                print("off")
                db.session.commit()   

            if payload == "on":
                data_rele = Device.query.filter_by(user = user).first()
                data_rele.rele1 = "1"
                print("on")
                db.session.commit()  

        if topic == topic_sensor01:
            payload = float(payload)
            
            data_sensor = Device.query.filter_by(user= user ).first()
            data_log = Device_log.query.filter_by(id = data_sensor.id).first() 
            data_sensor.sensortemp01 = payload
            db.session.commit()
            if payload >= data_log.temp_aqua_max:
                data_log.temp_aqua_max = payload
                data_sensor.temp_sensor01 = payload
               
                db.session.commit()
            if payload <= data_log.temp_aqua_min:
                data_log.temp_aqua_min = payload
                data_sensor.temp_sensor01 = payload
                db.session.commit()


        if topic ==  topic_sensor02 :
            payload = float(payload)
            data_sensor = Device.query.filter_by(user= user ).first() 
            data_log = Device_log.query.filter_by(id = data_sensor.id).first() 
            data_sensor.sensortemp02 = payload
            db.session.commit()
            
            if payload >= data_log.temp_ter_max:
                data_log.temp_ter_max = payload
                data_sensor.temp_terrario = payload
                db.session.commit()
            if payload <= data_log.temp_ter_min:
                data_log.temp_ter_min = payload
                data_sensor.temp_terrario = payload
                db.session.commit()
        
        if topic ==  topic_sensorhum:
            payload = float(payload)
            data_sensor = Device.query.filter_by(user= user ).first()
            data_log = Device_log.query.filter_by(id = data_sensor.id).first()
            data_sensor.sensorhum = payload
            db.session.commit()
            if payload >= data_log.hum_max:
                data_log.hum_max = payload
                data_sensor.sensorhum= payload
                db.session.commit()
            if payload <= data_log.hum_min:
                data_log.hum_min = payload
                data_sensor.sensorhum = payload
                db.session.commit()



    