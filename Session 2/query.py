import mlab
from models.service import Service

mlab.connect()

all_services = Service.objects() #extract a list of documents

first_service = all_services[0] #dictionary
print(first_service['name'])

last_service = all_services[-1]
print(last_service.name)
