import requests
from model.client import Client
from model.equipment import Equipment
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def client_find_all():
    list_client = []
    x = requests.get('http://ec2-52-67-56-229.sa-east-1.compute.amazonaws.com:8080/client-findAll')
    data = x.json()
    
    for index in  data:
        client = Client()
        client.id = index["id"]
        client.name = index["name"]
        client.cpf = index["cpf"]
        client.email = index["email"]
        client.endereco = index["address"]
        client.telefone = index["phone"]
        if(is_iterable(index["equipments"])):
            for e1 in  index["equipments"]:
                equipment = Equipment()
                equipment.id = e1["id"]
                equipment.model = e1["model"]
                equipment.serial = e1["serial"]
                equipment.brand =  e1["brand"]
                equipment.price =  e1["price"]
                equipment.pronto = e1["pronto"]
                equipment.autorizado = e1["autorizado"]
                equipment.entryDate =e1["entryDate"]
                equipment.defectForRepair = e1["defectForRepair"]
                equipment.departureDate = e1["departureDate"]
                equipment.obs = e1["obs"]
                equipment.devolucao = e1["devolucao"]
                equipment.entregue = e1["entregue"]
                equipment.garantia = e1["garantia"]
                equipment.departureEquipmentWarranty = e1["departureEquipmentWarranty"]
                equipment.entryEquipmentWarranty = e1["entryEquipmentWarranty"]
                equipment.description = e1["description"]
                client.list_equipments.append(equipment)
        list_client.append(client)
        #print(client.list_equipments)
    
    return list_client

def client_find_by_id(id):
    url = 'http://ec2-52-67-56-229.sa-east-1.compute.amazonaws.com:8080/client-findById'
    myobj = {'id': id}
    x = requests.post(url, json = myobj)
    data = x.json()
    print(data)
    return data
#client_find_by_id(2)

def client_update(client):
    url = 'http://ec2-52-67-56-229.sa-east-1.compute.amazonaws.com:8080/client-update'
    myobj = {'id': client.id, 'name':client.name,
             'email':client.email,
             'cpf':client.cpf,
             'phone':client.telefone,
             'address':client.endereco
         }
    x = requests.post(url, json = myobj)
  
    print('teste = ',x)
    return x

def client_create(client):
    url = 'http://ec2-52-67-56-229.sa-east-1.compute.amazonaws.com:8080/client-create'
    myobj = { 'name':client.name,
             'email':client.email,
             'cpf':client.cpf,
             'phone':client.telefone,
             'address': client.endereco
    }
    x = requests.post(url, json = myobj)
  
    print('teste = ',x)
    return x.json().get('id')

client_find_all()