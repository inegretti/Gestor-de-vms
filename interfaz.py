import tkinter as tk
from funciones import *


funcion=apiCloud()

ventana=tk.Tk() 
ventana.config(width=400, height=300)
ventana.title("vms")

caja2=tk.Entry()
caja2.place(x=20,y=30,width=200,height=25)
etiqueta2=tk.Label(text="Ingresar usuario local")
etiqueta2.place(x=20,y=5)

caja3=tk.Entry()
caja3.place(x=20,y=90,width=200,height=25)
etiqueta3=tk.Label(text="Ingresar el password local")
etiqueta3.place(x=20,y=60)

def listar_vms():
   if(caja2.get() != "" and caja3.get() != ""):
    funcion=apiCloud()
    funcion.USERNAME=caja2.get()
    funcion.PASSWORD=caja3.get()
    lista= apiCloud().list_vms(funcion.get_token())
    ventana2=tk.Toplevel(ventana)
    ventana2.geometry("2000x800")
    ventana2.title("Lista de VMs")
    texto = tk.Text(ventana2)
    texto.pack(fill="both", expand=True)
    for item in lista:
        texto.insert(tk.END, f"{item}\n")
   else:
       ventana2=tk.Toplevel(ventana)
       ventana2.config(width=600, height=200)
       ventana2.title("error")
       tk.Label(ventana2, text="los campos usuario y contraseña no pueden estar vacios").place(x=100,y=100)
   ventana2.mainloop()


#boton = tk.Button(text="Conseguir token", command=lambda: funcion.get_token())
#boton.place(x=20,y=50,width=100,height=30) ##ancho alto y localizacion dentro de la ventana



boton2 = tk.Button(text="Ver vms", command=lambda: listar_vms())
boton2.place(x=135,y=130,width=100,height=30) ##ancho alto y localizacion dentro de la ventana

caja=tk.Entry()
caja.place(x=20,y=210,width=200,height=25)
etiqueta=tk.Label(text="Ingresar Href a apagar o encender")
etiqueta.place(x=20,y=180)



def prender():
   ventana2=tk.Tk() 
   ventana2.config(width=400, height=300)
   try:
      if(caja.get() != "" and caja2.get() != "" and caja3.get() != ""):
         funcion.USERNAME=caja2.get()
         funcion.PASSWORD=caja3.get()
         if(funcion.verEstado(caja.get(),funcion.get_token())!=4):
            funcion.power_on_vm(funcion.get_token(), caja.get())
            ventana2.title("Ok")
            tk.Label(ventana2, text="la vm encendiendose").place(x=100,y=100) 
         else:
            ventana2.title("error")
            tk.Label(ventana2, text="la vm ya esta encendida").place(x=100,y=100)   
      else:
         ventana2.title("error")
         tk.Label(ventana2, text="complete todos los campos").place(x=100,y=100)
   except requests.exceptions.HTTPError as err:
       ventana2.title("error")
       tk.Label(ventana2, text=err).place(x=100,y=100)
   ventana2.mainloop()
boton3 = tk.Button(text="Encender VM", command=lambda: prender())
boton3.place(x=20,y=250,width=150,height=30)

def apagar():
   ventana2=tk.Tk() 
   ventana2.config(width=400, height=300)
   try:
      if(caja.get() != "" and caja2.get() != "" and caja3.get() != ""):
         funcion.USERNAME=caja2.get()
         funcion.PASSWORD=caja3.get()
         if((funcion.verEstado(caja.get(),funcion.get_token()))!=8):
            funcion.shutdown_vm(funcion.get_token(), caja.get())
            ventana2.title("Ok")
            tk.Label(ventana2, text="vm apagandose").place(x=100,y=100)
         else:
            ventana2.title("error")
            tk.Label(ventana2, text="la vm ya esta apagada").place(x=100,y=100) 
      else:
         ventana2.title("error")
         tk.Label(ventana2, text="la caja no puede estar vacia").place(x=100,y=100)
   except requests.exceptions.HTTPError as err:
       ventana2.title("error")
       tk.Label(ventana2, text=err).place(x=100,y=100)
   ventana2.mainloop()
boton4 = tk.Button(text="Apagar VM", command=lambda: apagar())
boton4.place(x=180,y=250,width=150,height=30)
ventana.mainloop()



    
