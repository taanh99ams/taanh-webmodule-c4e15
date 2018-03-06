from flask import *
import mlab
from models.dating import Dating
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    datings = Dating.objects()
    return render_template('dating_index.html', datings=datings)

@app.route('/detail/<id_to_find>')
def detail(id_to_find):
    girl = Dating.objects().with_id(id_to_find)
    return render_template('dating_detail.html', girl=girl)

@app.route('/admin')
def admin():
    datings = Dating.objects()
    return render_template('dating_admin.html',datings=datings)

@app.route('/form', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('dating_newservice.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_dating = Dating(name=name,
                            yob=yob,
                            phone=phone,
                            address='Hanoi'
                            )
        new_dating.save()
        return 'Saved'

if __name__ == '__main__':
  app.run(debug=True)

    # name = StringField()
    # yob = IntField()
    # phone = StringField()
    # address = StringField()
    # description = StringField()
    # measurement = ListField()
    # image = StringField()
