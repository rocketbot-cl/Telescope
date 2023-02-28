



# Rocketbot Telescope
  
Modulo para Rocketbot Telescope  
  
![banner](/imgs/Banner_Telescope.png)

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  

## Como usar este modulo

Para usar este modulo usted debe:

1. Crear proyecto
2. Generar la plantilla
   1. Toma un punto de referencia.
   2. Seleccione los datos que desea extraer.
   3. Guarde la Plantilla.
   4. Cargue y procese un archivo.
   5. Verifique los datos extraídos.
3. Guarde el token generado para la plantilla
4. Crear un archivo denominado telescope.ini que contenga:
   1. [USER]
   2. user = aaaa@rocketbot.cl
   3. password = robot1111
   4. server = http://11.11.1.111/api


## Descripción de los comandos

### Login Telescope
  
Comando para conectarse a Telescope
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta Archivo .ini|Selecciona el archivo .ini para conectarse|C:/Users/User/Desktop/archivo.ini|

### Subir documento
  
Subir documento para obtener texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccionar archivo|Selecciona el documento a subir para obtener el texto|C:/Users/User/Desktop/documento.jpg|
|Template token|Token de Template en Telescope|RCKU2GKCUP4XB5VW|
|Asignar a variable|Variable donde se guardará el texto obtenido|var|

### Subir documentos
  
Subir multiples documentos para obtener texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccionar carpeta|Selecciona la carpeta donde se encuentran los documentos a subir|C:/Users/User/Desktop/carpeta|
|Template ID|ID de Template en Telescope|RCKU2GKCUP4XB5VW|
|Asignar a variable|Variable donde se guardará el contenido de los documentos|var|

### Consultar estado de resultado
  
Devuelve el estado de un resultado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token de resultado|Token de resultado de un proceso de extracción de texto|4YLXHLLD4IXM621P|
|Asignar a variable|Variable donde se guardará el resultado de la consulta|var|

### Obtener resultado
  
Obtener información de un resultado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token de resultado|Token de resultado de un proceso de extracción de texto|RCKU2GKCUP4XB5VW|
|Guardar resultado en variable|Variable donde se guardará el resultado||
