# CalculadoraContrato
Web services calculadora incluye el contrato en swagger
Webservices calculadora con imagen de docker Lenguaje Python Requisitos: Docker Para la ejecución se debe descargar la carpeta Calculadora, y desde una consola de PowerShell:

* Ubicarse dentro de la ruta en donde se dejo la carpeta Calculadora
* Compilar y generar la imagen con el siguiente comando: docker build -t calculadora .
* Verificar que se haya cargado la imagen con el comando docker image ls
* Correr la aplicación con el siguiente comando: docker run -p 5000:80 calculadora

Para consumir el servicio debe ingresar de la siguiente forma, con algún cliente para probar servicios rest:

* http://localhost:5000/sumar/ En el caso de la suma, se debe ingresar como parámetros en el body en formato json: 
{
"numeros":"10:2"
}
* http://localhost:5000/restar/ En el caso de la resta, solo se restan dos números, se debe ingresar como parámetros en el body en formato json:
{
"numero1":"10",
"numero2":"4"
}
* http://localhost:5000/multiplicar/ En la multiplicación, los parámetros se ingresan igual que en la suma
* http://localhost:5000/dividir/ En la división, los parámetros son igual que en la resta
