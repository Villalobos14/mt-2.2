Act. 2.2_MT
Este proyecto consiste en la implementación de una Máquina de Turing que verifica cadenas binarias y realiza una suma de los valores binarios presentes en la cinta de entrada. La interfaz gráfica del proyecto está desarrollada utilizando Tkinter, lo que permite una fácil interacción para ingresar la cadena y visualizar los resultados.

Características
Verificación de cadenas binarias (solo acepta los caracteres 0 y 1).
Implementación de una Máquina de Turing que procesa la cadena y calcula la suma de los valores binarios.
Interfaz gráfica amigable que permite ingresar la cadena y ver el resultado de la operación.
Gestión de errores mediante ventanas emergentes que informan al usuario sobre entradas inválidas o resultados incorrectos.
Estructura del proyecto
El proyecto contiene los siguientes archivos principales:

main.py: Archivo que contiene la interfaz gráfica creada con Tkinter, donde se puede ingresar la cadena a procesar.
turingMachine.py: Implementación de la Máquina de Turing que se encarga de realizar el procesamiento de la cadena.
Requisitos previos
Para ejecutar este proyecto, necesitarás tener instalado lo siguiente:

Python 3.x
Tkinter (incluido con la mayoría de las instalaciones de Python)
Instalación
Clona el repositorio en tu máquina local:

bash
Copiar código
git clone https://github.com/tuusuario/Act.2.2_MT.git
Navega al directorio del proyecto:

bash
Copiar código
cd Act.2.2_MT
Ejecuta el programa principal:

bash
Copiar código
python main.py
Uso
Ejecuta el archivo main.py para abrir la interfaz gráfica.
Ingresa una cadena binaria válida (solo 0 y 1).
Haz clic en el botón Verificar para que la Máquina de Turing procese la cadena.
Verifica los resultados en la ventana emergente: si la cadena es válida, se mostrará la suma de los valores binarios en decimal y binario.
Ejemplo de uso
Entrada: 110
Resultado: Suma: 2 - Binario: 10
Si se ingresa una cadena inválida (por ejemplo, una cadena con caracteres que no sean 0 o 1), se mostrará un mensaje de error indicando que solo se aceptan cadenas binarias.

Autor
Josh Villalobos
