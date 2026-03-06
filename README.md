# Gestor de VMs

Herramienta desarrollada en Python para consultar y encender / apagar máquinas virtuales mediante API REST en la plataforma claro cloud.

El objetivo del proyecto es proporcionar una forma alternativa de interactuar con las VMs cuando la interfaz web de la plataforma cloud no está disponible o presenta fallas.

La aplicación permite listar máquinas virtuales, consultar su estado y ejecutar acciones básicas de operación como encendido y apagado.

---

# Características

- Autenticación mediante API
- Obtención de token de sesión
- Listado de máquinas virtuales
- Consulta del estado de las VMs
- Encendido de máquinas virtuales
- Apagado de máquinas virtuales
- Interfaz gráfica simple para operación

---

# Arquitectura del proyecto

El proyecto está dividido en tres componentes principales:
interfaz.py → interfaz gráfica
funciones.py → cliente API
test.py → pruebas de funcionamiento

### test.py

Script simple utilizado para probar las funciones de la API desde consola.

---

# Flujo de funcionamiento

1. La aplicación solicita autenticación al servidor API.
2. Se obtiene un token de sesión.
3. El token se utiliza para realizar consultas a la API.
4. Se obtiene la lista de máquinas virtuales.
5. El usuario puede consultar el estado de una VM o ejecutar acciones sobre ella.

---

# Tecnologías utilizadas

- Python
- Tkinter
- Requests
- API REST

---

# Instalación

Clonar el repositorio:


git clone https://github.com/inegretti/Gestor-de-vms.git


Ingresar al directorio:


cd Gestor-de-vms


Instalar dependencias:


pip install requests


---

# Ejecución

Para ejecutar la interfaz gráfica:


python interfaz.py


Para ejecutar pruebas simples desde consola:


python test.py


---

# Configuración

Antes de ejecutar la aplicación es necesario configurar:

- URL del servidor API
- versión de API
- credenciales de acceso

Estos parámetros se encuentran en la clase `apiCloud`.

---

# Uso

1. Ejecutar la aplicación.
2. Presionar el botón **Ver VMs** para listar las máquinas disponibles.
3. Copiar el `href` de la VM que se desea operar.
4. Pegar el `href` en el campo de entrada.
5. Elegir la acción:

- Encender VM
- Apagar VM

---

# Posibles mejoras

Algunas mejoras futuras para el proyecto:

- manejo de variables de entorno para credenciales
- sistema de logging
- caché de token
- empaquetado como ejecutable
- CLI además de interfaz gráfica
- monitoreo automático del estado de VMs

---

# Autor

Ignacio Negretti Dietrich
