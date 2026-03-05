import requests
import base64


class apiCloud:
    
    VCD_URL = "https://vcd.clarocloud.com"
    API_VERSION = "36.3"
    USERNAME =   # usuariolocaldecloud@nro de cuenta
    PASSWORD =  #contraseña del usuario
    VM_ID = "urn:vcloud:vm:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx"
    
    def __init__(self):
       pass
    

    
    #conseguir el token
    def get_token(self):
        auth = base64.b64encode(
            f"{self.USERNAME}:{self.PASSWORD}".encode()
        ).decode()

        headers = {
            "Accept": f"application/*+json;version={self.API_VERSION}",
            "Authorization": f"Basic {auth}"
        }

        response = requests.post(
            f"{self.VCD_URL}/api/sessions",
            headers=headers
        )

        response.raise_for_status()

        token = response.headers.get("X-VMWARE-VCLOUD-ACCESS-TOKEN")
        return token
    
    
    #Listar las vms
    """
    #version 1
    def list_vms(self,token):
        headers = {
            "Accept": f"application/*+json;version={self.API_VERSION}",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(
            f"{self.VCD_URL}/api/query?type=vm",
            headers=headers
        )

        response.raise_for_status()
        data = response.json()
        listado = list()
        for vm in data["record"]:
            name = vm.get("name")
            href = vm.get("href")
            status = vm.get("status")

            # Extraer ID desde la URL
            vm_id = href.split("/")[-1] if href else None

            #mostrar datos por consola(Si lo necesitan lo pueden descomentar)
            #print(f"Nombre: {name} | ID: {vm_id} | Href: {href} | Status: {status}")
            #crear el listado
            listado.append({"Nombre": name,  "ID": vm_id,  "Href": href,  "Status": status})
        return listado
   
    
    def configGeneral(self,token):
        headers = {
            "Accept": f"application/*+json;version={self.API_VERSION}",
            "Authorization": f"Bearer {token}"
        }

        url = f"{self.VCD_URL}/api/query?type=vm&filter=isVAppTemplate==false"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        
        return data
    """ 
    def list_vms(self, token):
        headers = {
            "Accept": f"application/*+json;version={self.API_VERSION}",
            "Authorization": f"Bearer {token}"
        }

        url = f"{self.VCD_URL}/api/query?type=vm&filter=isVAppTemplate==false"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        listado = []

        for vm in data["record"]:
            name = vm.get("name")
            href = vm.get("href")
            status = vm.get("status")

            vm_id = href.split("/")[-1] if href else None

            listado.append({"Nombre": name,  "ID": vm_id,  "Href": href,  "Status": status})

        return listado
    
    def verEstado(self,href,token):
        headers = {
            "Accept": f"application/*+json;version={self.API_VERSION}",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(href, headers=headers)
        response.raise_for_status()
        data = response.json()
        status = data.get("status")
        
        return status
        
        
    
    #encendido de vms        
    def power_on_vm(self,token, href):
        headers = {
            "Accept": f"application/*+json;version={self.API_VERSION}",
            "Authorization": f"Bearer {token}"
        }
        
        try:
        
            response = requests.get(href, headers=headers)
            response.raise_for_status()

            data = response.json()
            status = data.get("status")
            
            if(status == 4):
                print("La VM ya está encendida.")
                
                
            else:
                url = f"{href}/power/action/powerOn"
                response = requests.post(url, headers=headers)
                response.raise_for_status()
                print("VM encendiéndose (powerOn)")
                
        except requests.exceptions.HTTPError as err:
            raise
            

        
        
    #apagar de vms    
    def shutdown_vm(self, token, href):
        headers = {
            "Accept": f"application/*+json;version={self.API_VERSION}",
            "Authorization": f"Bearer {token}"
        }
        try:
            response = requests.get(href, headers=headers)
            response.raise_for_status()

            data = response.json()
            status = data.get("status")
            
            if(status == 8):
                print("La VM ya está apagada.")
            else:
                url = f"{href}/power/action/shutdown"

                response = requests.post(url, headers=headers)
                response.raise_for_status()

                print("VM apagándose (shutdown)") 
        except requests.exceptions.HTTPError as err:
            raise
