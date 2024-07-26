
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
    id = db.Column(db.Integer,autoincrement = True, primary_key = True,unique = True)
    user = db.Column(db.String,unique = True)
    rele1 = db.Column(db.String)
    temp_aquario = db.Column(db.String)
    temp_terrario = db.Column(db.String)
    humidade_terrario = db.Column(db.String)


    def __init__(self,user,rele1,temp):
        self.user = user
        self.rele1 = rele1
        self.temp = temp

        




        
       

