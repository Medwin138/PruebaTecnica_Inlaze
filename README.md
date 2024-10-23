# Proyecto de Automatización de Pruebas con Selenium

Este proyecto está diseñado para automatizar pruebas de inicio de sesión, cierre de sesión y registro de usuarios en una aplicación web utilizando Selenium y Pytest. El objetivo es garantizar que las funcionalidades críticas de la aplicación funcionen como se espera.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecutar Pruebas](#ejecutar-pruebas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Funciones](#funciones)
- [Contribución](#contribución)

## Requisitos

- Python 3.x
- Selenium
- Pytest
- Google Chrome (o cualquier otro navegador compatible con el driver correspondiente)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   cd nombre_del_repositorio](https://github.com/Medwin138/PruebaTecnica_Inlaze.git

## Ejecutar Pruebas
Asegúrate de tener el ChromeDriver instalado y que sea compatible con la versión de Google Chrome que tienes en tu máquina. Descarga ChromeDriver.

ejecuta el siguiente comando en la terminal 
pip install -r requirements.txt

-Esto ejecutará todos los casos de prueba definidos en el proyecto y generará un informe en formato HTML, así como capturas de pantalla en caso de fallos.

## Estructura del Proyecto
esta es laestructura basica del proyecto 

/proyecto
│
├── pages
│   ├── login_page.py         # Clase para manejar la lógica de la página de inicio de sesión y registro.
│
├── tests
│   ├── test_login.py         # Conjunto de pruebas para las funcionalidades de inicio de sesión y registro.
│
├── requirements.txt          # Dependencias del proyecto.
├── screenshots                # Carpeta para almacenar las capturas de pantalla.
└── README.md                  # Este archivo.

## Funciones

La clase LoginPage maneja las interacciones con la página de inicio de sesión y registro. A continuación se detallan los métodos disponibles:

open(url): Abre la URL especificada en el navegador.
login(email, password): Realiza un intento de inicio de sesión con las credenciales proporcionadas.
logout(): Cierra la sesión del usuario actual.
registro_usuario(full_name, email, password, repeat_password): Registra un nuevo usuario en la aplicación con la información proporcionada.
is_login_successful(): Verifica si el inicio de sesión fue exitoso.
is_logout_successful(): Verifica si el cierre de sesión fue exitoso.
is_registration_successful(): Verifica si el registro del usuario fue exitoso.
get_error_message(): Obtiene el mensaje de error en caso de fallo en el registro o inicio de sesión.
Clase TestLogin

La clase TestLogin contiene pruebas automatizadas para verificar las funcionalidades de inicio de sesión y registro de usuarios. Se utilizan assertions para comprobar que los resultados de las acciones sean los esperados.

Métodos de la Clase TestLogin

test_login_successful(setup, request):
Descripción: Verifica que el inicio de sesión sea exitoso con credenciales válidas.
Acciones:
Abre la página de inicio de sesión.
Intenta iniciar sesión con un usuario y contraseña válidos.
Asegura que el inicio de sesión fue exitoso.
Captura una pantalla si la prueba tiene éxito.

test_logout_successful(setup, request):
Descripción: Verifica que el cierre de sesión sea exitoso.
Acciones:
Inicia sesión primero.
Ejecuta la acción de cerrar sesión.
Asegura que el cierre de sesión fue exitoso.
Captura una pantalla si la prueba tiene éxito.

test_register_successful(setup, request):
Descripción: Verifica que el registro de un nuevo usuario sea exitoso.
Acciones:
Abre la página de registro.
Intenta registrar un nuevo usuario con información válida.
Asegura que el registro fue exitoso.
Captura una pantalla si la prueba tiene éxito.

test_register_name_validation(setup, request):
Descripción: Verifica la validación del nombre durante el registro.
Acciones:
Intenta registrar un usuario con un solo nombre.
Asegura que el botón de registro no esté habilitado.

test_register_password_validation(setup):
Descripción: Verifica la validación de la contraseña durante el registro.
Acciones:
Intenta registrar un usuario con una contraseña débil.
Asegura que el botón de registro esté deshabilitado.

test_register_required_fields(setup, request):
Descripción: Verifica que los campos obligatorios sean validados correctamente.
Acciones:
Intenta registrar un usuario dejando el campo de nombre vacío.
Asegura que el botón de registro esté deshabilitado.

test_register_password_mismatch(setup, request):
Descripción: Verifica que las contraseñas coincidan durante el registro.
Acciones:
Intenta registrar un usuario con contraseñas que no coinciden.
Asegura que el botón de registro esté deshabilitado y se muestre el mensaje de error adecuado.

Comentarios sobre el Código
Manejo de Errores: Cada test incluye afirmaciones para verificar el estado después de realizar acciones (como inicio de sesión o registro), lo que permite detectar errores en la aplicación.
Capturas de Pantalla: Las capturas de pantalla se toman para ayudar en la depuración cuando una prueba falla, lo cual es especialmente útil en pruebas de interfaz de usuario.
Estructura Modular: La utilización de una clase de página LoginPage sugiere una buena práctica de separación de responsabilidades, facilitando el mantenimiento y la legibilidad del código.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, sigue estos pasos:

Contactame
milleredwin85@gmail.com

   @@@@@@
  @      @
 @        @
 @        @
  @@@@@@@@


Haz un fork del proyecto.
Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz un commit (git commit -m 'Añadir nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.

