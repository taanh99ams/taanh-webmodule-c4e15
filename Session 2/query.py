import mlab
from models.service import Service

mlab.connect()

# all_services = Service.objects() #extract a list of documents
#
# first_service = all_services[0] #dictionary
# print(first_service['name'])
#
# last_service = all_services[-1]
# print(last_service.name)

# id_to_find = '5a955e047b816a16483072dd'
#
# loren = Service.objects.get(id=id_to_find)
# print(loren.name)
# print(loren.to_mongo())

# Delete: loren.delete()
#Create: service.save()
#Update:
# id_to_find = "5a955d437b816a19fc17b8fb"
# # service = Service.objects.get(id=id_to_find)
# service = Service.objects.with_id(id_to_find)
# print(service.to_mongo())
# # if service is not None:
#     service.update(set__status=False)
#     service.reload()
#     print(service.to_mongo())
# else:
#     print('not found')

# id_to_find = '5a9562477b816a1f406acb28'
# service = Service.objects.get(id=id_to_find)
#
# # print(service.to_mongo())
# if service is not None:
#     service.update(set__name='Ta Anh')
#     service.reload()
#     print(service.to_mongo())
# else:
#     print('not found')
index = 0
services = Service.objects()
for service in services:
    service.delete()
    index = index + 1
    print('deleted ', index)
