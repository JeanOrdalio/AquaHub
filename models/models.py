
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

        

class Device_log(db.Model):
    __tablename__= 'device_log'
    id = db.Column(db.Integer,autoincrement = True, primary_key = True,unique = True)
    temp_aqua_max = db.Column(db.Integer,unique = True)
    temp_aqua_min = db.Column(db.Integer)
    temp_ter_max= db.Column(db.Integer)
    temp_ter_min = db.Column(db.Integer)
    hum_max = db.Column(db.Integer)
    hum_min = db.Column(db.Integer)

    def __init__(self,temp_aqua_max, temp_aqua_min,temp_ter_max,temp_ter_min,hum_max, hum_min ):
        self.temp_aqua_max = temp_aqua_max
        self.temp_aqua_min = temp_aqua_min
        self.temp_ter_max = temp_ter_max
        self.temp_ter_min = temp_ter_min
        self.hum_max = hum_max
        self.hum_min = hum_min

       
