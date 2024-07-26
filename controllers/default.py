from __init__ import app
from flask import render_template,request,redirect,url_for
from models.models import User,Device,Keys
from  __init__ import db,mqtt_client,cache
from flask_login import login_user, logout_user,login_required,current_user



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
        password = request.form['password']
        key = request.form['device']
        key_verify = Keys.query.filter_by( key = key ).first()
        acess = str(key_verify.key)
        rele1 = "1"
        temp = "0"
        if key == acess:
        
            user = User(name,email,password,key)
            device = Device(name,rele1,temp)
            
            db.session.add(user)
            db.session.add(device)
            db.session.commit() 
            
            return redirect(url_for('login'))
             
             

    return render_template('registrar.html')

 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    try:
        user = current_user.name
        device = Device.query.filter_by(user = user ).first()
        rele1 = device.rele1
        if  rele1 == "0":
            rele1 = "Desligado"
            status = "Online"
        if rele1 =="1":
            rele1 = "Ligado"
            status = "Online"
        return render_template('dashboard.html',rele1 = rele1,status = status)

    except:
        status ="Offline"
        return render_template('dashboard.html',rele1 = rele1,status = status)

    

@app.route('/reles',methods= ['GET','POST'])
@login_required
def reles():
    
    
    try:
        if request.method == 'POST' and request.form.rele123:
            print("kabum")
        data_rele = Device.query.filter_by(user = current_user.name ).first()
        rele1 = data_rele.rele1
        if data_rele.rele1 == "0":
            rele1 = "Desligado"
            status = "Online"
            return render_template('reles.html',rele1 = rele1,status = status)
        if data_rele.rele1 == "1":
            rele1 = "Ligado"
            status = "Online"
            return render_template('reles.html',rele1 = rele1,status = status)  
    except: 
        status = "Offline" 
        rele1 = "Offline"

    return render_template('reles.html',rele1 = rele1,status = status)

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

    

@login_required
@app.route('/sensores',methods= ['GET','POST'])
def sensores():
    
    

    
    user = current_user.name
    try:

        data_sensores = Device.query.filter_by(user = user).first()
        aquario = data_sensores.temp_aquario
        terrario = data_sensores.temp_terrario
        humidade = data_sensores.humidade_terrario
        status = "Online"
        



    except:
        status ="Offline"


    return render_template('sensores.html',aquario = aquario, terrario = terrario , humidade = humidade,status = status)

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
        topic_aquario = (f'{user}/sensores/aquario')
        topic_terrario =(f'{user}/sensores/terrario')
        topic_humidade_terrario =(f'{user}/sensores/humidade_terrario')

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

        if topic == topic_aquario:

            data_sensor = Device.query.filter_by(user= user ).first()
            data_sensor.temp = payload
            db.session.commit()      

        if topic ==  topic_terrario :
            data_sensor = Device.query.filter_by(user= user ).first() 
            data_sensor.temp_terrario = payload
            db.session.commit()
        
        if topic ==  topic_humidade_terrario :
            data_sensor = Device.query.filter_by(user= user ).first() 
            data_sensor.humidade_terrario = payload
            db.session.commit()

                
        
   
   
    