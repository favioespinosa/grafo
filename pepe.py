from array import *
class Grafo:
	def __init__(self,numero):
		self.next=[None for i in range(numero)]
		self.numero=None
def Lector(linea):
	lagar=0#Inicio
	lagar2=0#entre
	lagar3=1#entre
	lagar4=1#fin
	trozo=""
	arr=array('i',[])
	lagarnum=0
	num1=0
	num2=0
	for i in range(len(linea)):
		if linea[i]=='[':
			if lagar==0 and lagar3==1:#Si es al principio
				lagar=1
			elif lagar2==0 and lagar==1:#Si es entre
				lagar2=1
				lagar3=1
			else:
				print("Ingreso mal los datos: "+linea[i])
		elif linea[i]==']':
			if lagar3==1 and lagar2==1:#Si es que es entre
				arr.append(int(trozo))
				trozo=""
				lagar3=0
				lagar2=0
			elif lagar4==1 and lagar3==0:#Si es que es al final
				break
			else:
				print("Ingreso mal los datos1: "+linea[i])
				break
		elif linea[i]==',' and lagar==1 and lagar2==1 and lagar3==1 and lagar4==1 and lagarnum==1:
			arr.append(int(trozo))
			trozo=""
		elif ord(linea[i])>=ord('0') and ord(linea[i])<=ord('9'):
			lagarnum=1
			trozo=trozo+linea[i]
		else:
			print("",end='')
			#print(i)
	return arr
def maximo(arr):
	may=0
	for i in range(len(arr)):
		if arr[i]>may:
			may=arr[i]
	return may
def Perito(arr):
	largo=maximo(arr)
	flag=0
	for i in range(largo):
		flag=0
		for j in range(len(arr)):
			if i==arr[j]:
				flag=1
		if flag==0:
			print("Esta mal construido el Grafo")
			return False
	return True

def Construccion(base,arr):
	for i in range(len(arr)):
		if i%2==0:
			base[arr[i]].next[arr[i+1]]=base[arr[i+1]]
			#print(base[i].numero)
			base[arr[i+1]].next[arr[i]]=base[arr[i]]
def todo_lleno(grafico):
	for i in range(len(grafico.next)):
		if grafico.next[i]!=None:
			return True
	return False
def base_de_datos(arr):
	base=[Grafo(maximo(arr)+1) for i in range(maximo(arr)+1)]
	for i in range(maximo(arr)+1):
		base[i]=Grafo(maximo(arr)+1)
		base[i].numero=i
	return base,base
def todo_visitado(visitado,vertices):
	for i in range(vertices):
		if visitado[i]==False:
			return True
	return False
def fin_de_cola(base,vertices,visitado):
	for i in range(vertices):
		if base.next[i]!=None and visitado[i]==False:
			return True
	return False

def movimiento_por_profundidad(base,vertices):#Glubino
	visitado=[False for i in range(vertices)]
	head=[Grafo(vertices) for i in range(vertices)]
	j=0
	head[0]=base
	while todo_visitado(visitado,vertices):
		#print(base.numero)
		if j==0:
			base=head[0]
		else:
			base=head[j-1]
		#print("Legga")
		while fin_de_cola(base,vertices,visitado):
			#print(base.numero)
			for i in range(vertices):
				if base.next[i]!=None and visitado[i]==False:
					head[j]=base
					j+=1
					print(base.numero,end='->')
					base=base.next[i]
					print(base.numero,end='->')
					visitado[i]=True
					break
def movimiento_por_ancho(base,vertices):#Shirinu
	visitado=[False for i in range(vertices)]
	head=[Grafo(vertices) for i in range(vertices)]
	puntos=array('i',[0])
	head[0]=base[0]
	visitado[0]=True
	while todo_visitado(visitado,vertices):
		print("(0->)",end='')
		for j in range(vertices):
			print("(",end='')
			for i in range(vertices):
				if base[puntos[j]].next[i]!=None and visitado[i]==False:
					tmp=base[puntos[j]].next[i]
					visitado[i]=True
					puntos.append(tmp.numero)
					i=0
					print(tmp.numero,end='->')
			print(")",end='')
		break
linea=input()
arr=Lector(linea)
#print(arr)
if (Perito(arr)):
	casa,base=base_de_datos(arr)
	print(base[3].numero)
	Construccion(base,arr)
	base=base[0]
	#print(base.numero)
	movimiento_por_profundidad(base,maximo(arr)+1)
	print("")
	movimiento_por_ancho(casa,maximo(arr)+1)

