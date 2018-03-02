#fapp
from flask import Flask, render_template
# from mongoengine import Document, StringField, IntField, BooleanField
import mlab
from models.service import Service

mlab.connect()

app = Flask(__name__)

#Create collection (collection is bunch of documents)
#It is recommended to create collection in other files (models) and import collection into app.py


#Fill in the form
# service = Service(name='Loren',
#                     yob="1998",
#                     gender=0,
#                     height=170,
#                     phone="0981641654",
#                     address="Hanoi",
#                     status=True)
#
# # #Put the form into collection
# service.save()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/search/<gender>')
# def search(gender):
#     services = Service.objects(gender=gender, yob__lte=1998, address__exact="Hanoi") #Trong dau ngoac la dieu kien loc
#     return render_template('search.html', all_services=services)

if __name__ == '__main__':
  app.run(debug=True)
