# hotel_reservations_system

# Sistema de Reservas de Hotel
Este es un sistema de reservas de hotel desarrollado como
proyecto académico. La aplicación permite a los clientes
registrarse, iniciar sesión y realizar reservas de habitaciones.
Los administradores pueden gestionar habitaciones y visualizar
reservas.
## Arquitectura del Proyecto
La aplicación está dividida en tres capas, cada una desplegada
en una máquina virtual (VM) separada:
1. **Capa de Presentación** (VM1)
- **Tecnologías**: HTML, CSS, Bootstrap, jQuery, jQuery
DataTables
- **Servidor Web**: NGINX
- **Descripción**: Interfaz de usuario accesible desde el
exterior a través de SERVEO.
2. **Capa de Lógica de Negocio** (VM2)
- **Tecnologías**: Python Flask
- **Descripción**: API RESTful que maneja la lógica de la
aplicación y se comunica con la base de datos.
3. **Capa de Datos** (VM3)
- **Tecnologías**: MariaDB
- **Descripción**: Base de datos que almacena la información
de clientes, habitaciones y reservas.
