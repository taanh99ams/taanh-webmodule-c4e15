from flask import Flask, render_template
import mlab
from models.customer import Customer

mlab.connect()
app = Flask(__name__)

@app.route('/')
def index_customer():
    return render_template('index_customer.html')

@app.route('/search')
def search_customer():
    customers = Customer.objects(gender__exact=0, contacted__exact='not yet contacted')
    return render_template('search_customer.html', customers=customers)

if __name__ == '__main__':
  app.run(debug=True)
