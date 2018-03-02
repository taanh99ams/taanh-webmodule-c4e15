from flask import Flask, render_template
from mlab import connect
from models.service import Service

# app = Flask(__name__)

connect()

#Ex2:
id_to_find = '5a955a427b816a202cc2cf43'
document = Service.objects.get(id = id_to_find)

#Ex3:
document.delete()
