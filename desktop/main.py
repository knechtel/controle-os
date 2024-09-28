from tkinter import * 
import webbrowser 
import  tkinter    as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from model.client import Client
from model.equipment import Equipment
from service.client_service import client_find_all, client_update, client_create
from service.equipment_service import equipment_update, equipment_create

itemAutorizado = None
client_clone = Client()
aux_client = 0
list_clients=[]
editName=False
textObs = None
data_saida=''
data_entrada=''
i=0
index=0
master = Tk('')
state_garantia_entregue = tk.IntVar()
state_garantia = tk.IntVar()
state_autorizado = tk.IntVar()
devolucao_state = tk.IntVar()
pronto_state = tk.IntVar()
entregue_state = tk.IntVar()
master.title("Controle de OS")
listbox = Listbox(master)
listbox.grid(row=3,column=0,padx=10,pady=10,rowspan=26)
listbox.config(width=5,height=20)
flag_novo = False
entryName = Entry(master)
client_cpy = None



for client in client_find_all():
	index+=1
	list_clients.append(client)
	listbox.insert(index,client.id)

def is_float(value):
	try:
		float(value)
	except ValueError:
		return False
	return True

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def print_selected_item():
	selected_index = listbox.curselection()  # Get the selected item's index
	if selected_index:
		selected_item = listbox.get(selected_index[0])  # Get the selected item
		print(f"Selected Item: {selected_item}")
	else:
		print("no selected item ")


def get_state_entregue():
	global entregue_state
	if(entregue_state.get() == 1):
		return True
	else:
		return False
	

def get_state_autorizado():
	global state_autorizado
	state = state_autorizado.get()
	if(state == 1):
		return True
	else:
		return False
	

def get_state_garantia():
	global state_garantia
	if(state_garantia.get() == 1):
		return True
	else:
		return False
def get_state__entregue_garantia():
	global state_garantia_entregue
	if(state_garantia_entregue.get() == 1):
		return True
	else:
		return False
	
def get_state_devolucao():
	global devolucao_state
	if(devolucao_state.get() == 1):
		return True
	else:
		return False
	
def get_sate_pronto():
	global pronto_state
	if(pronto_state.get() == 1):
		return True
	else:
		return False

def imprimir_os():
	id = str(client_clone.id)
	address = "http://ec2-52-67-56-229.sa-east-1.compute.amazonaws.com:8080/download?id="+id
	webbrowser.open(address)

def novo_os():
	clear_fields()
	global flag_novo
	flag_novo = True
	print("prepara nova Os.")

def do_save():
	global i
	global editName
	global client_clone
	global flag_novo
	if( flag_novo == True):
		if(listbox.size() >= 1):
		
			print("Novo registro"+ entryName.get())
			
			client = Client()
			client.name = entryName.get()
			client.cpf = eCPF.get()
			client.telefone = eTelefone.get()
			client.endereco = endereco.get()
			client.email = eEmail.get()
			
			
			equipment = Equipment()
			equipment.serial = eAparelhoSerial.get()
			equipment.model = eAparelhoModelo.get()
			equipment.brand = eAparelhoMarca.get()
			equipment.defectForRepair = eAparelhoDefeito.get()
			equipment.obs = textObs.get("1.0",END)
			equipment.description = descricaoAparelho.get()
			if(entryName.get()==''):
				entryName.config(bg='yellow')
				messagebox.showwarning ('Aviso!', 'É necessário ao menos o cadastro do nome do cliente!') 
			else:	
				if(is_float(eAparelhoPreco.get())):
					id_client = client_create(client)
					equipment.id_client = id_client
					list_clients.insert(0,client)
					equipment.price = float(eAparelhoPreco.get())
					client.id = id_client
					client_clone = 	client
					listbox.insert(0,id_client)
					
					eAparelhoPreco.config(bg='white')
					entryName.config(bg='white')
					data = equipment_create(equipment)
					equipment.id =data.get("id")
					equipment.entryDate = data.get("entryDate")
					
					timestamp_millis = equipment.entryDate
					timestamp_seconds = timestamp_millis / 1000
					date = datetime.fromtimestamp(timestamp_seconds)
					formatted_date = date.strftime("%d/%m/%Y")
					data_entrada = str(formatted_date+"  -                          ")
					dataEntrada.config(text = data_entrada)
				
					client_clone.list_equipments.append(equipment)
					flag_novo = False
					listbox.select_set(0)
				else:
					eAparelhoPreco.config(bg='yellow')
					if(entryName.get()!=''):
						entryName.config(bg="white")
					messagebox.showwarning ('Aviso!', 'Campo preço com valor inválido!') 
		else:
			client = Client()
			client.name = entryName.get()
			client.cpf = eCPF.get()
			client.telefone = eTelefone.get()
			client.endereco = endereco.get()
			client.email = eEmail.get()
			
			
			equipment = Equipment()
			equipment.serial = eAparelhoSerial.get()
			equipment.model = eAparelhoModelo.get()
			equipment.brand = eAparelhoMarca.get()
			equipment.defectForRepair = eAparelhoDefeito.get()
			equipment.obs = textObs.get("1.0",END)
			equipment.description = eAparelho.get()
			if(entryName.get()==''):
				entryName.config(bg='yellow')
				messagebox.showwarning ('Aviso!', 'É necessário ao menos o cadastro do nome do cliente!') 
			id_client = client_create(client)
			equipment.id_client = id_client
			list_clients.insert(0,client)
			equipment.price = float(eAparelhoPreco.get())
			client.id = id_client
			client_clone = 	client
			listbox.insert(0,id_client)
					
			eAparelhoPreco.config(bg='white')
			entryName.config(bg='white')
			data = equipment_create(equipment)
			equipment.id =data.get("id")
			equipment.entryDate = data.get("entryDate")
					
			timestamp_millis = equipment.entryDate
			timestamp_seconds = timestamp_millis / 1000
			date = datetime.fromtimestamp(timestamp_seconds)
			formatted_date = date.strftime("%d/%m/%Y")
			data_entrada = str(formatted_date+"  -                          ")
			dataEntrada.config(text = data_entrada)
				
			client_clone.list_equipments.append(equipment)
			flag_novo = False
			listbox.select_set(0)
	else:
		global aux_client
		indices_selecionados = listbox.curselection()
		print(indices_selecionados)
		try:
			if(indices_selecionados):
				client_clone.id = listbox.get(indices_selecionados[0])
		except ValueError:
			print("erro")
		print("client_clone id = ",client_clone.id)
		client_clone.name = entryName.get()
		client_clone.cpf = eCPF.get()
		client_clone.telefone = eTelefone.get()
		client_clone.endereco = endereco.get()
		client_clone.email = eEmail.get()
		

		messagebox.showwarning ('Aviso!', 'Cliente editado com sucesso!') 
		client_update(client_clone)

	
		if(len(client_clone.list_equipments) > 0):
			client_clone.list_equipments[0].description = eAparelho.get()
			client_clone.list_equipments[0].brand = eAparelhoMarca.get()
			client_clone.list_equipments[0].defectForRepair = eAparelhoDefeito.get()
			client_clone.list_equipments[0].price = eAparelhoPreco.get()
			client_clone.list_equipments[0].model =eAparelhoModelo.get()
			client_clone.list_equipments[0].obs = textObs.get("1.0",END)
			client_clone.list_equipments[0].serial = eAparelhoSerial.get()
			client_clone.list_equipments[0].autorizado =  get_state_autorizado()
			client_clone.list_equipments[0].devolucao =  get_state_devolucao()
			client_clone.list_equipments[0].pronto =  get_sate_pronto()
			client_clone.list_equipments[0].entregue =  get_state_entregue()
			#client_clone.list_equipments[0].entryDate
			client_clone.list_equipments[0].garantia =  get_state_garantia()
			client_clone.list_equipments[0].departuretWarranty = False
			if(get_state_garantia()==True and get_state__entregue_garantia()==True):
				client_clone.list_equipments[0].departuretWarranty = get_state__entregue_garantia()
			else:
				client_clone.list_equipments[0].departuretWarranty = False
			#aqui trabalhando nesta feature
			
			data = equipment_update(client_clone.list_equipments[0])
			if(data.get("departureDate")!=None):
				
				client_clone.list_equipments[0].departureDate = data.get("departureDate")
				timestamp_millis = client_clone.list_equipments[0].departureDate

				timestamp_seconds = timestamp_millis / 1000
				date = datetime.fromtimestamp(timestamp_seconds)
				formatted_date = date.strftime("%d/%m/%Y")
				data_saidaAux = str(formatted_date+"  -                            ")
				dataSaida.config(text= data_saidaAux)
				item_entregue.config(state='disable')
				disabled()
			else:
				dataSaida.config(text= '')
					
		if( 0 < len(client_clone.list_equipments)):
			if(data.get("entryData")!=None):
				client_clone.list_equipments[0].entryDate = data.get("entryData")
				timestamp_millis = client_clone.list_equipments[0].entryDate
				timestamp_seconds = timestamp_millis / 1000
				date = datetime.fromtimestamp(timestamp_seconds)
				formatted_date = date.strftime("%d/%m/%Y")
				data_entrada = str(formatted_date+"  -                          ")
				dataEntrada.config(text = data_entrada)
			else:
				print("ERRO ---  ")
		if( 0 < len(client_clone.list_equipments)):
			if(data.get("entryEquipmentWarranty")!=None):
				client_clone.list_equipments[0].entryEquipmentWarranty = data.get("entryEquipmentWarranty")
				timestamp_millis = client_clone.list_equipments[0].entryEquipmentWarranty
				timestamp_seconds = timestamp_millis / 1000
				date = datetime.fromtimestamp(timestamp_seconds)
				formatted_date = date.strftime("%d/%m/%Y")
				data_entrada = str(formatted_date+"  -                          ")
				dataEntradaGarantia.config(state= "normal")
				dataEntradaGarantia.delete(0, 'end')
				dataEntradaGarantia.insert(0, data_entrada)
				dataEntradaGarantia.config(state= "readonly")
				itemGarantia1.config(state="disabled")
				#itemEntregue.select()
				#itemEntregue.config(state="disabled")
		
		if( 0 < len(client_clone.list_equipments)):
			if(data.get("departureEquipmentWarranty")!=None):
				if(get_state_garantia()==True):
					print("é garantia")
					client_clone.list_equipments[0].departureEquipmentWarranty = data.get("departureEquipmentWarranty")
					timestamp_millis = client_clone.list_equipments[0].departureEquipmentWarranty
					timestamp_seconds = timestamp_millis / 1000
					date = datetime.fromtimestamp(timestamp_seconds)
					formatted_date = date.strftime("%d/%m/%Y")
					data_saida_garantia = str(formatted_date+"  -                          ")
					dataSaidaGarantia.config(state= "normal")
					dataSaidaGarantia.insert(0, data_saida_garantia)
					dataSaidaGarantia.config(state= "readonly")
					itemEntregueGarantia.select()
					itemEntregueGarantia.config(state="disabled")
				
		if(0<len(client_clone.list_equipments)):
			if(data.get("description")!=None):
				descricaoAparelho.delete(0,'end')
				descricaoAparelho.insert(0,client_clone.list_equipments[0].description)
				#set garantia pronta e entregue
		
			
Label(master, text='').grid(row=0)
Label(master, text='').grid(row=1)
Label(master, bg="white", fg='#f00',text='OS').grid(row=2,column=0)
Label(master, text='Nome').grid(row=0,column=1)
Label(master, text='CPF').grid(row=1,column=1)
Label(master, text='Telefone').grid(row=2,column=1)
Label(master, text='Endereço').grid(row=1,column=2)
Label(master, text='Email').grid(row=0,column=3)

idCad=Label(master, text='')
idCad.grid(row=3,column=1)
Label(master, text='Aparelho').grid(row=4,column=1)
Label(master, text='Modelo').grid(row=5,column=1)
Label(master, text='Serial').grid(row=6,column=1)
Label(master, text='Marca').grid(row=7,column=1)
Label(master, text='Defeito').grid(row=4,column=3)
Label(master, text='Preco').grid(row=5,column=3)
Label(master, text='Endereço').grid(row=1,column=3)
Label(master, text='Entrada').grid(row=8,column=1)
Label(master, text='Saida').grid(row=9,column=1)
Label(master, text='Garantia').grid(row=10,column=1,rowspan=2)
itemEntregueGarantia = Checkbutton(master, text="Entregue Garantia",variable=state_garantia_entregue)
itemEntregueGarantia.grid(row=10,column=2)

Label(master, text='Entrada').grid(row=11,column=1)
dataEntradaGarantia = Entry(master)
dataEntradaGarantia.grid(row=11,column=2)
#dataEntradaGarantia.insert(0,"25/08/2024")
dataEntradaGarantia.config(state= "readonly")
Label(master, text='Saida').grid(row=12,column=1)
dataSaidaGarantia = Entry(master)
dataSaidaGarantia.config(state= "disabled")

dataSaidaGarantia.grid(row=12,column=2)


dataEntrada = Label(master,text='')
dataEntrada.grid(row=8,column=2)



dataSaida = Label(master,text=str(data_saida))

dataSaida.grid(row=9,column=2)
descricaoAparelho = Entry(master)
descricaoAparelho.grid(row=4,column=2)
#eAparelho.insert(0,"E6")


entryName.grid(row=0, column=2)


eCPF = Entry(master)
eCPF.grid(row=1, column=2)

eTelefone = Entry(master)
eTelefone.grid(row=2, column=2)

eEmail = Entry(master)
eEmail.grid(row=0, column=4)

eAparelhoModelo = Entry(master)
eAparelhoModelo.grid(row=5,column=2)

eAparelhoSerial = Entry(master)
eAparelhoSerial.grid(row=6,column=2)


eAparelhoMarca = Entry(master)
eAparelhoMarca.grid(row=7,column=2)

eAparelhoDefeito = Entry(master)
eAparelhoDefeito.grid(row=4,column=4)

eAparelhoPreco = Entry(master)
eAparelhoPreco.grid(row=5,column=4)

endereco = Entry(master)
endereco.grid(row=1,column=4)

# button6=Button(master,command=myfunction, text="Enviar")
# button6.grid(row=2,column=5)
itemPronto = Checkbutton(master, text="Pronto  ",variable=pronto_state)
itemPronto.grid(row=6,column=3)
item_entregue = Checkbutton(master, text="Entregue",variable=entregue_state)
item_entregue.grid(row=7,column=3)

itemDevolucao = Checkbutton(master, text="Devolução",variable=devolucao_state)
itemDevolucao.grid(row=7,column=4)

itemAutorizado = Checkbutton(master, text="Autorizado",variable=state_autorizado)
itemAutorizado.grid(row=8,column=4)
itemGarantia1 = Checkbutton(master, text="Garantia   ",variable=state_garantia)
itemGarantia1.grid(row=9,column=4)
 
textObs = Text(master, height = 5, width = 25)
textObs.grid(row=10,column=4)
Label(master, text='Obs').grid(row=10,column=3)
buttonAparelhoSave=Button(master,command=do_save, text="Salvar")
buttonAparelhoSave.grid(row=11,column=4)
buttonAparelhoNovo=Button(master,command=novo_os, text="Novo")
buttonAparelhoNovo.grid(row=11,column=5)
buttonAparelhoOs=Button(master,command=imprimir_os, text="Imprimir")
buttonAparelhoOs.grid(row=11,column=6)

def set_client():
	global client_clone 
	entryName.delete(0, 'end')
	entryName.insert(0,client_clone.name)
	
	endereco.delete(0, 'end')
	if(client_clone.endereco!=None):
		endereco.insert(0,client_clone.endereco)

	
	eEmail.delete(0, 'end')
	eEmail.insert(0,client_clone.email)


	eCPF.delete(0,'end')
	eCPF.insert(0,client_clone.cpf)

	
	eTelefone.delete(0,'end')
	eTelefone.insert(0,client_clone.telefone)

def set_equipment():
	global client_clone 
	if( 0 < len(client_clone.list_equipments)):
		eAparelhoModelo.delete(0,'end')
		eAparelhoModelo.insert(0,client_clone.list_equipments[0].model)

	if( 0 < len(client_clone.list_equipments)):
		eAparelhoSerial.delete(0,'end')
		eAparelhoSerial.insert(0,client_clone.list_equipments[0].serial)
	if( 0 < len(client_clone.list_equipments)):
		eAparelhoMarca.delete(0,'end')
		eAparelhoMarca.insert(0,client_clone.list_equipments[0].brand)
	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].defectForRepair != None):
			eAparelhoDefeito.delete(0,'end')
			eAparelhoDefeito.insert(0,client_clone.list_equipments[0].defectForRepair)

	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].description==None):
			descricaoAparelho.delete(0,'end')
			print(client_clone.list_equipments[0].description)
		else:
			descricaoAparelho.delete(0,'end')
			descricaoAparelho.insert(0,client_clone.list_equipments[0].description)

	if( 0 < len(client_clone.list_equipments)):
		eAparelhoPreco.delete(0,'end')
		eAparelhoPreco.insert(0,client_clone.list_equipments[0].price)

	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].entryDate!=None):
			timestamp_millis = client_clone.list_equipments[0].entryDate
			timestamp_seconds = timestamp_millis / 1000
			date = datetime.fromtimestamp(timestamp_seconds)
			formatted_date = date.strftime("%d/%m/%Y")
			data_entrada = str(formatted_date+"  -                          ")
			dataEntrada.config(text = data_entrada)

	dataSaida.config(text = '')	
	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].departureDate!=None):

			timestamp_millis = client_clone.list_equipments[0].departureDate
			timestamp_seconds = timestamp_millis / 1000
			date = datetime.fromtimestamp(timestamp_seconds)
			formatted_date = date.strftime("%d/%m/%Y")
			data_saida_cast = str(formatted_date+"  -                             ")
			
			dataSaida.config(text= data_saida_cast)
			disabled()
		else:
			itemAutorizado.config(state=NORMAL)
			item_entregue.config(state=NORMAL)
			itemDevolucao.config(state=NORMAL)
			itemEntregueGarantia.config(state=NORMAL)
			itemPronto.config(state=NORMAL)
			itemGarantia1.config(state=NORMAL)
			itemEntregueGarantia.config(state=NORMAL)
	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].devolucao == True):
			itemDevolucao.select()
		else:
			itemDevolucao.deselect()

	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].pronto == True):
			itemPronto.select()
		else:
			itemPronto.deselect()

	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].autorizado==True):
			itemAutorizado.select()
		else:
			itemAutorizado.deselect()

	#entrou para garantia
	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].garantia==True):
			itemGarantia1.select()
			itemGarantia1.config(state="disabled")

		else:
			itemGarantia1.deselect()
			itemGarantia1.config(state="normal")

	if(0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].entryEquipmentWarranty!=None):
			timestamp_millis = client_clone.list_equipments[0].entryEquipmentWarranty
			timestamp_seconds = timestamp_millis / 1000
			date = datetime.fromtimestamp(timestamp_seconds)
			formatted_date = date.strftime("%d/%m/%Y")
			data_entrada = str(formatted_date+"  -                          ")
			dataEntradaGarantia.config(state= "normal")
			dataEntradaGarantia.insert(0, data_entrada)
			dataEntradaGarantia.config(state= "readonly")
			#itemEntregue.select()Garantia
			
		else:
			dataEntradaGarantia.config(state= "normal")
			dataEntradaGarantia.delete(0,'end')
			dataEntradaGarantia.insert(0, '')
			dataEntradaGarantia.config(state= "readonly")
			itemEntregueGarantia.config(state='normal')

	#parte final da garantia 
	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].departureEquipmentWarranty!=None):
			
			timestamp_millis = client_clone.list_equipments[0].departureEquipmentWarranty
			timestamp_seconds = timestamp_millis / 1000
			date = datetime.fromtimestamp(timestamp_seconds)
			formatted_date = date.strftime("%d/%m/%Y")
			data_saida = str(formatted_date+"  -                          ")
			dataSaidaGarantia.config(state= "normal")
			dataSaidaGarantia.delete(0,'end')
			dataSaidaGarantia.insert(0, data_saida)
			dataSaidaGarantia.config(state= "readonly")
			itemEntregueGarantia.select()
			itemEntregueGarantia.config(state= "disabled")
		else:
			itemEntregueGarantia.deselect()
			itemEntregueGarantia.config(state= "normal")
			dataSaidaGarantia.config(state= "normal")
			dataSaidaGarantia.delete(0,'end')
			dataSaidaGarantia.insert(0, '')
			dataSaidaGarantia.config(state= "readonly")

	textObs.delete("1.0", "end")
	if( 0 < len(client_clone.list_equipments)):
		textObs.insert(INSERT,str(client_clone.list_equipments[0].obs))
	
	if( 0 < len(client_clone.list_equipments)):
		if(client_clone.list_equipments[0].entregue==True):
			item_entregue.select()
			item_entregue.config(state="disabled")
			# entryName.config(state='readonly')
			# eTelefone.config(state='readonly')
			# eEmail.config(state='readonly')
			# endereco.config(state='readonly')
			# eCPF.config(state='readonly')
			# eAparelhoModelo.config(state='readonly')
			# eAparelhoSerial.config(state='readonly')
			# eAparelhoMarca.config(state='readonly')
			# eAparelhoDefeito.config(state='readonly')
			# eAparelhoPreco.config(state='readonly')
			# textObs.config(state='disabled')
		else:
			item_entregue.deselect()
			item_entregue.config(state="normal")
			entryName.config(state='normal')
			eTelefone.config(state='normal')
			eEmail.config(state='normal')
			endereco.config(state='normal')
			eCPF.config(state='normal')
			descricaoAparelho.config(state='normal')
			eAparelhoModelo.config(state='normal')
			eAparelhoSerial.config(state='normal')
			eAparelhoMarca.config(state='normal')
			eAparelhoDefeito.config(state='normal')
			eAparelhoPreco.config(state='normal')
			textObs.config(state='normal')
def select_from_list_box(event):
	global flag_novo 
	flag_novo = False
	clear_fields()
	
	obj_client = listbox.curselection()
	global aux_client

	try:
		aux_client = str(obj_client).replace(")","",2).replace("(","",2).replace(",","",2)
	
		global client_clone 
		client_clone = list_clients[int(aux_client)]

	
		texto = "ID "+str(client_clone.id)
		idCad.config(text=texto)
	except ValueError:
		print("")


	set_client()
	set_equipment()

	

listbox.bind('<<ListboxSelect>>', select_from_list_box)
eAparelhoPreco.insert(0,"0.00")
def clear_fields():
	entryName.config(state='normal')
	eTelefone.config(state='normal')
	eEmail.config(state='normal')
	endereco.config(state='normal')
	eCPF.config(state='normal')
	eAparelhoModelo.config(state='normal')
	eAparelhoSerial.config(state='normal')
	eAparelhoMarca.config(state='normal')
	eAparelhoDefeito.config(state='normal')
	eAparelhoPreco.config(state='normal')
	textObs.config(state='normal')
	entryName.delete(0, END)
	eTelefone.delete(0, END)
	eEmail.delete(0, END)
	endereco.delete(0, END)
	eCPF.delete(0, END)
	eAparelhoModelo.delete(0, END)
	eAparelhoSerial.delete(0, END)
	eAparelhoMarca.delete(0, END)
	eAparelhoDefeito.delete(0, END)
	eAparelhoPreco.delete(0, END)
	descricaoAparelho.delete(0,END)
	#textObs.delete(0, END)
	itemPronto.deselect()
	itemDevolucao.deselect()	
	itemAutorizado.deselect()
	item_entregue.deselect()
	itemGarantia1.deselect()
	dataEntrada.config(text='')
	dataSaida.config(text='')
	dataEntradaGarantia.config(state= "normal")
	dataEntradaGarantia.delete(0,END)
	dataEntradaGarantia.config(state= "disabled")
	dataSaidaGarantia.config(state= "normal")
	dataSaidaGarantia.delete(0,END)
	dataSaidaGarantia.config(state= "disabled")
	itemAutorizado.config(state=NORMAL)
	item_entregue.config(state=NORMAL)
	itemDevolucao.config(state=NORMAL)
	itemEntregueGarantia.config(state=NORMAL)
	itemPronto.config(state=NORMAL)
	itemGarantia1.config(state=NORMAL)
	itemEntregueGarantia.config(state=NORMAL)
	itemEntregueGarantia.deselect()
	descricaoAparelho.config(state=NORMAL)
	descricaoAparelho.delete(0,END)
def disabled():
	itemAutorizado.config(state='disabled')
	
	item_entregue.config(state='disabled')
	itemDevolucao.config(state='disabled')
	itemPronto.config(state='disabled')
	entryName.config(state='readonly')
	eTelefone.config(state='readonly')
	eEmail.config(state='readonly')
	endereco.config(state='readonly')
	eCPF.config(state='readonly')
	descricaoAparelho.config(state='readonly')
	eAparelhoModelo.config(state='readonly')
	eAparelhoSerial.config(state='readonly')
	eAparelhoMarca.config(state='readonly')
	eAparelhoDefeito.config(state='readonly')
	eAparelhoPreco.config(state='readonly')
	textObs.config(state='disabled')

mainloop()
