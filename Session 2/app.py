#fapp
from flask import *
import mlab
from models.service import Service

mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    services = Service.objects(gender=gender, yob__lte=1998, address__exact="Hanoi") #Trong dau ngoac la dieu kien loc
    return render_template('search.html', all_services=services)

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services=services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects().with_id(service_id)

    if service_to_delete is None:
        return 'not found'
    service_to_delete.delete()
    return redirect(url_for('admin'))


@app.route('/new-service', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        #request: lay cai form ma user vua submit
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service = Service(name=name,
                            yob=yob,
                            phone=phone,
                            gender=gender,
                            height=178,
                            address='Hanoi',
                            status=True
                            )
        new_service.save()
        return 'Saved'

@app.route('/update-service/<service_id>', methods=['GET','POST'])
def update(service_id):
    service_to_update = Service.objects().with_id(service_id)
    if request.method == 'GET':
        return render_template('new_service.html', service_to_update=service_to_update)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        # new_service = Service(name=name,
        #                         yob=yob,
        #                         phone=phone,
        #                         gender=gender)
        # new_service.save()
        service_to_update.update(
                                set__name=name,
                                set__yob=yob,
                                set__gender=gender,
                                set__phone=phone
        )
        return redirect(url_for('admin'))


if __name__ == '__main__':
  app.run(debug=True)
