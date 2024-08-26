
from flask_login import UserMixin
from __init__ import db,login_manager
from requests import get
import pandas as pd




@login_manager.user_loader
def get_user(user_id):
    
    usuario=User.query.filter_by(id =user_id).first()
   
   
    return  usuario



class User(db.Model,UserMixin):
    __tablename__= 'users'

    id = db.Column(db.Integer,autoincrement = True,primary_key = True, unique = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    cep = db.Column(db.Integer)
    password = db.Column(db.String)
    dispositivo = db.Column(db.String,unique = True)
 
    def __init__(self,name,email,password,dispositivo):
        self.name = name
        self.email = email
        self.password = password
        self.dispositivo = dispositivo

class Keys(db.Model):

    __tablename__= 'keys'

    key = db.Column(db.String,primary_key = True,unique = True)
   
    def __init__(self,key):
 
        self.key = key
     
class Device(db.Model):

    __tablename__= 'device'
    id = db.Column(db.Integer,autoincrement = True, primary_key = True,unique = True,)
    user = db.Column(db.String,unique = True)
    rele1 = db.Column(db.String)
    rele2 = db.Column(db.String)
    rele3 = db.Column(db.String)
    rele4 = db.Column(db.String)
    name_sensor_temp01 = db.Column(db.String)
    name_sensor_temp02 =db.Column(db.String)
    name_sensor_hum = db.Column(db.String)
    name_rele1 = db.Column(db.String)
    name_rele2 = db.Column(db.String)
    name_rele3 = db.Column(db.String)
    name_rele4 = db.Column(db.String)



    def __init__(self,user,rele1,temp,name_sensor_temp01, name_sensor_temp02,name_sensor_hum,name_rele1,name_rele2,name_rele3,name_rele4):
        self.user = user
        self.rele1 = rele1
        self.temp = temp
        self.name_sensor_hum = name_sensor_hum
        self.name_sensor_temp01 = name_sensor_temp01
        self.name_sensor_temp02 = name_sensor_temp02
        self.name_rele1 = name_rele1
        self.name_rele2 = name_rele2
        self.name_rele3 = name_rele3
        self.name_rele4 = name_rele4

        
class Automation_hora(db.Model):
    __tablename__= 'automation_hora'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    hora = db.Column(db.String)
    on_off = db.Column(db.String)
    
    def __init__(self,id,name,hora, on_off):
        self.id = id 
        self.name = name
        self.hora = hora
        self.on_off = on_off

class Automation_sensor(db.Model):
    __tablename__= 'automation_sensor'
    id = db.Column(db.Integer,primary_key = True)
    sensor = db.Column(db.String)
    sensor_ligar = db.Column(db.String)
    sensor_desligar = db.Column(db.String)
    
    def __init__(self,id ,sensor, sensor_ligar,sensor_desligar):
        self.id = id 
        self.sensor = sensor
        self.sensor_ligar = sensor_ligar
        self.senssensor_desligar = sensor_desligar
       
