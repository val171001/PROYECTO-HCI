#__universidad del Valle de Guatemala
#__HCI
#__Marcos Gutierrez
#__David Valenzuela
#__carlos Chew
#__Mario Sarmientos
#__Fernando Hengstenberg
#__maquina de latas

#__importamos la libreria tkinter
#__interfaz Grafica
from tkinter import *



#__creamos la raiz
raiz=Tk()

#__titulo de la ventana
raiz.title("Reciclar")

#__no ose puede redimencionar la ventana
raiz.resizable(0,0)

#__figura del icono
#raiz.iconbitmap("icono.ico")

#__tamanio de la ventana
raiz.geometry("1400x500")

#__color de fondo
raiz.config(bg="white")

#__creamos el frame
frame=Frame()

#__empaquetamos el frame
frame.pack()

#__tamanio al frame
frame.config(width="1400",height="500")


#__cargamos la primer imagen
imagen_reciclar=PhotoImage(file="reciclar.png")

#__lugar de la imagen_reciclar
lblImagen=Label (raiz,image=imagen_reciclar).place(x=140,y=0)

#__imagen de latas
imagen_latas=PhotoImage(file="latas.png")

#__lugar de imagen_latas
lblImagen2=Label(raiz,image=imagen_latas).place(x=550,y=0)



#__instrucciones de la ventana.
#__titulo
informacion_titulo =Label(frame,text="Maquina de Reciclaje",fg="forestgreen", font=("Comic Sans MS",18)).place(x=100,y=170)

#__informacion_parrafo
imformacion_parrafo=Label(frame,text="Maquina de reciclaje de latas que motiva a las personas a utilizarla por medio de códigos y puntos que van acumulando los distintos usuarios, estos se pueden canjear en diferentes plataformas algunos ejemplos serian, códigos de Steam, saldo de diferentes compañías de telefonía como Tigo y Claro, Códigos para PlayStation Network. Con el fin de concientizar a las personas y motivarlas a cuidar nuestro planeta el cual ya se encuentra muy deteriorado, las latas son recicladas para cuidar el medio ambiente.",fg="black", font=("Comic Sans MS",12),wraplength=400,anchor="center").place(x=25,y=230)


#__instrucciones
informacion_instrucciones =Label(frame,text="Instrucciones",fg="forestgreen", font=("Comic Sans MS",18)).place(x=660,y=170)

#__informacion_instrucciones
imformacion_parrafo_instrucciones=Label(frame,text="Para poder hacer uso de la Maquina de reciclaje tienes que seguir las siguientes instrucciones, regístrate en nuestra pagina web para tener tu propio usuario e ir acumulando puntos con tu cuenta, ingresa una lata en la máquina y espera tu código, introduce tu código en la página web acumulando puntos, al tener una cantidad de puntos necesaria podrás cambiar estos por cupones en tiendas online, por saldo o internet en compañías telefónicas..",fg="black", font=("Comic Sans MS",12),wraplength=400,anchor="center",justify='center').place(x=540,y=230)

imagen_qr=PhotoImage(file="code.png")
lblcode=Label (raiz,image=imagen_qr)
lblcode.place(x= 1030,y=70)

#__instrucciones de la ventana.
#__titulo
informacion_titulo =Label(frame,text="Tu código es:",fg="forestgreen", font=("Comic Sans MS",18)).place(x=1030,y=30)


#__instrucciones de la ventana.
#__titulo
f = open("code.txt", "r")
ejemplo = f.read()
f.close()
codigo =Label(frame,text=ejemplo,fg="forestgreen", font=("Comic Sans MS",25)).place(x=1030,y=400)

def callback():
	global lblcode
	img = PhotoImage(file="code.png")
	lblcode.configure(image=img)
	lblcode.image = img
	print("change")
	lblcode.after(1000, callback)

raiz.after(1000, callback)
#__loop para la ventana.
raiz.mainloop()
