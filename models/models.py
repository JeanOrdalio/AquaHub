
from flask_login import UserMixin
from __init__ import db,login_manager




@login_manager.user_loader
def get_user(user_id):
    
    usuario=User.query.filter_by(id =user_id).first()
   
   
    return  usuario



class User(db.Model,UserMixin):
    __tablename__= 'users'

    id = db.Column(db.Integer,autoincrement = True,primary_key = True, unique = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)
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
    temp_aquario = db.Column(db.Integer)
    temp_terrario = db.Column(db.Integer)
    humidade_terrario = db.Column(db.Integer)


    def __init__(self,user,rele1,temp):
        self.user = user
        self.rele1 = rele1
        self.temp = temp

        

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

       

