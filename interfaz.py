import tkinter as tk
from funciones import *


funcion=apiCloud()
def listar_vms():
    funcion=apiCloud()
    lista= apiCloud().list_vms(funcion.get_token())
    ventana2=tk.Toplevel(ventana)
    ventana2.geometry("2000x800")
    ventana2.title("Lista de VMs")
    texto = tk.Text(ventana2)
    texto.pack(fill="both", expand=True)
    for item in lista:
        texto.insert(tk.END, f"{item}\n")
    ventana2.mainloop()

ventana=tk.Tk() 
ventana.config(width=400, height=300)
ventana.title("vms")
#boton = tk.Button(text="Conseguir token", command=lambda: funcion.get_token())
#boton.place(x=20,y=50,width=100,height=30) ##ancho alto y localizacion dentro de la ventana



boton2 = tk.Button(text="Ver vms", command=lambda: listar_vms())
boton2.place(x=135,y=50,width=100,height=30) ##ancho alto y localizacion dentro de la ventana
caja=tk.Entry()
caja.place(x=20,y=120,width=200,height=25)
etiqueta=tk.Label(text="Ingresar Href a apagar o encender")
etiqueta.place(x=20,y=90)

def prender():
   ventana2=tk.Tk() 
   ventana2.config(width=400, height=300)
   try:
      if(caja.get() != ""):
         if(funcion.verEstado(caja.get(),funcion.get_token())!=4):
            funcion.power_on_vm(funcion.get_token(), caja.get())
            ventana2.title("Ok")
            tk.Label(ventana2, text="la vm encendiendose").place(x=100,y=100) 
         else:
            ventana2.title("error")
            tk.Label(ventana2, text="la vm ya esta encendida").place(x=100,y=100)   
      else:
         ventana2.title("error")
         tk.Label(ventana2, text="la caja no puede estar vacia").place(x=100,y=100)
   except requests.exceptions.HTTPError as err:
       ventana2.title("error")
       tk.Label(ventana2, text=err).place(x=100,y=100)
   ventana2.mainloop()
boton3 = tk.Button(text="Encender o apagar VM", command=lambda: prender())
boton3.place(x=20,y=150,width=150,height=30)

def apagar():
   ventana2=tk.Tk() 
   ventana2.config(width=400, height=300)
   try:
      if(caja.get() != ""):
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
boton4.place(x=180,y=150,width=150,height=30)
ventana.mainloop()



    
