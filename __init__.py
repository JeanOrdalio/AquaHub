from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt
from flask_caching import Cache



app = Flask(__name__, static_url_path='/static')
app.app_context().push() 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)
app.secret_key = 'webmaster'
app.config['MQTT_BROKER_URL'] = '192.168.2.156'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'home' 
app.config['MQTT_PASSWORD'] = 'webmaster'  
app.config['MQTT_KEEPALIVE'] = 10  
app.config['MQTT_TLS_ENABLED'] = False 
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 3600 
cache = Cache(app)
mqtt_client = Mqtt(app)
login_manager = LoginManager()
login_manager.init_app(app)
mqtt_client.subscribe('jean/controle')
mqtt_client.subscribe('jean/reles')
mqtt_client.subscribe('jean/sensores/aquario')
mqtt_client.subscribe('jean/sensores/terrario')
mqtt_client.subscribe('jean/sensores/humidade_terrario')





from controllers import default


