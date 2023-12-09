import requests
import json
import os

# Cargar el archivo JSON con los nombres de los archivos y las URL de las imágenes
with open('bbdd.json', 'r') as file:
    data = json.load(file)

# Directorio donde se guardarán las imágenes descargadas
directorio_destino = 'imagenes_peliculas'

# Crear el directorio si no existe
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Descargar las imágenes
for pelicula in data['movies']:
    nombre_archivo = pelicula['poster_path']  # Ajusta esto al nombre del campo del JSON que contiene el nombre del archivo JPEG
    url_imagen = pelicula['poster_path']  # Ajusta esto al nombre del campo del JSON que contiene la URL de la imagen

    # Descargar la imagen
    response = requests.get(url_imagen)

    # Guardar la imagen descargada en el directorio destino
    with open(os.path.join(directorio_destino, nombre_archivo), 'wb') as img_file:
        img_file.write(response.content)

    print(f"Imagen '{nombre_archivo}' descargada con éxito.")

print("Proceso de descarga completado.")