from funciones import *

funcion=apiCloud()
token=funcion.get_token()
#print(token)
funcion.list_vms(token)
#print(funcion.list_vms(token))

#funcion.shutdown_vm(token, "https://vcd.clarocloud.com/api/vApp/vm-0b4cbf5e-d282-445b-807c-0c63896c7fc6")
#funcion.power_on_vm(token, "https://vcd.clarocloud.com/api/vApp/vm-0b4cbf5e-d282-445b-807c-0c63896c7fc6")         
