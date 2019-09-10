# Taller Final Entrega Smart Data Construcción

El objetivo de este taller es transferir las capacidades básicas para la operación de la plataforma SmartData Construcción (desde ahora **'la plataforma'**). Se espera que al final de esta jornada las(os) asistentes tengan instalados todos los software y herramientas necesarias, se hayan hecho tests del trabajo con datos y su posterior deploy a la nube, para que sean leídos dichos datos a través de la plataforma y se construyan las visualizaciones.

## Instalación de Software
### Anaconda
El procesamiento de datos en SmartData se realiza en dos pasos:

1. Trabajo en Excel para la agregación de datos (respetando el formato de dichas tablas),
2. Trabajo en Python3/Jupyter Notebook para el procesamiento de los datos desde excel, y convertirlos a JSON, con el fin de servir dichos outputs en la nube y ser visualizados.

Si no se tiene instalado Python3/Jupyter Notebook se debe instalar aquí:

#### a) Windows:
Para instalar Anaconda seguiremos estas instrucciones: 
- https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/ 

#### b) MacOS:
Para instalar Anaconda seguiremos estas instrucciones: 
- https://docs.python-guide.org/starting/install3/osx/ 


### Cyberduck
El programa para la transferencia sencilla de datos utilizado en SmartData Construcción, es Cyberduck. Para su descarga (Windows, MacOS) se debe visitar el siguiente link:
- https://cyberduck.io/download/ 

## Datos 
Los datos y los notebooks con los que se construye la plataforma los encontramos aquí: 
- https://drive.google.com/drive/folders/1d_lLRqCewmuDsuIeIKu1vEv2mo0FJJ_K?usp=sharing 

## Procesamiento de Datos
Los datos corresponden a 93 datasets divididos en 8 tablas generales:
- Macroindicadores
- Sustentabilidad
- Inmobiliarios y Habitacionales 
- Casen
- Innovacion
- BIM
- Materiales
- Leed_CES

Cada una de estas tablas han sido separadas en hojas para la construcción de los datasets finales. Estas tablas de entrada son del tipo ‘Excel’. Para cada una de las tablas antes mencionadas se ha creado una sección dentro de la plataforma una serie de scripts en el lenguaje de programación Python, utilizando la herramienta Jupyter Notebook, que facilita una interfaz gráfica amigable de la terminal del computador.

- S1_Destacados.ipynb
- S2_Macroindicadores.ipynb
- S3_Sustentabilidad.ipynb
- S4_Inmobiliario_habitacional.ipynb 
- S5_BIM_Innovacion.ipynb
- S6_Seguridad.ipynb
- S7_CChC.ipynb

Lo que realiza cada uno de estos notebooks es tomar la data de ingreso (archivos excel), procesarlos mediante una serie de funciones y generar el formato final con toda la información relacionada para indicador. El formato de salida de los datos, siempre es del tipo Json.

### Jupyter Notebooks
Los datos de entrada están ya configurados para cada notebook de cada sección. Por ende, si existe algún nuevo datos que se quiera agregar, basta con respetar el formato de las tablas excel, subirlas a la carpeta antes mencionada ($ src > frontend > public) y ejecutar los notebooks. Para hacer correr la totalidad de funciones para los indicadores de cada sección, de debe presionar en cada notebook la opción ‘Cell > Run All’.

#### Geocoding
Pasos:
- Crear una Key de Bing: https://www.bingmapsportal.com/ 
- Editar el Notebook de Geocodificación 'LEED_CES_GeoCoding.ipynb' y ejecutarlo
- Convertir CSV a GeoJson: http://www.convertcsv.com/csv-to-geojson.htm 
- Transformar GeoJson resultantes al formato indicado utilizando el *script* funcion_geojson.py

### Deployment
Los datos en la aplicación deben tener presencia en dos espacios para poder hacer un render de la visualización. Los datos deben estar presentes tanto en la carpeta ‘Data’ en la ruta $ src > frontend > public > data; tanto como en la carpeta ‘SmartData-Files/data’ en Digital Ocean. El que deban tener presencia en ambos espacios radica en que las visualizaciones, al mismo tiempo, trabajan en local y en la nube. El proceso de subida de datos a digital ocean es tan sencillo como arrastrar un archivo y configurar los permisos del mismo para que sea visible por el modulo de visualización.

Para configurar permisos a cada dataset (o conjunto de datos o carpeta), se debe solamente hacer click derecho en el archivo que ha sido subido a Digital Ocean mediante CyberDuck, luego click en ‘info’. Estos nos lleva a la pestaña de permisos en donde presionamos en la rueda (o gear) para añadir un permiso a ‘Everyone’, el cual configuramos a READ. Estos permite que las visualizaciones tengan todos los permisos necesarios para leer los datos y construir las gráficas.