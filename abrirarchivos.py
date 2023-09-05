import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def dict_promedio(ruta_archivo, desde, hasta):
    # Lista de nombres de archivos TIFF de flats
    archivos_flats = [f"{ruta_archivo}{i:03d}.tiff" for i in range(desde, hasta)]

    # Lista para almacenar los datos de los flats (promedio de valores de píxeles)
    datos_flats = []

    # Recorremos la lista de archivos TIFF de flats
    for archivo_nombre in archivos_flats:
        try:
            # Cargamos cada archivo TIFF de flat
            imagen_flat = Image.open(archivo_nombre)
            
            # Convierte la imagen a un arreglo numpy para trabajar con los datos de píxeles
            datos_imagen = np.array(imagen_flat)
            
            # Agrega los datos de la imagen (matriz de píxeles) a la lista
            datos_flats.append(datos_imagen)
        except FileNotFoundError:
            print(f"El archivo {archivo_nombre} no se encontró.")

    # Calcula el promedio de los valores de píxeles entre todas las imágenes
    promedio_flats = np.mean(datos_flats, axis=0)
    
    return promedio_flats

ruta_flats = r"J:\UC\Segundo Semestre 2023\Laboratorio de Instrumentación Astronómica\Lab 2\Nueva carpeta\Flats 182 sec\Image0"
promedio_flats = dict_promedio(ruta_flats, 1, 101)
print("FLATS:", promedio_flats)
ruta_bias = r"J:\UC\Segundo Semestre 2023\Laboratorio de Instrumentación Astronómica\Lab 2\Nueva carpeta\Bias\Image0"
promedio_bias = dict_promedio(ruta_bias, 10, 110)
print("BIAS:", promedio_bias)
ruta_dark = r"J:\UC\Segundo Semestre 2023\Laboratorio de Instrumentación Astronómica\Lab 2\Nueva carpeta\Darks de 23 seg\Image0"
promedio_dark = dict_promedio(ruta_dark, 1, 10)
print("DARK:", promedio_dark)

print("PIXEL",promedio_dark[4][100])


std_dev = np.std(promedio_dark)
print("Desviación Estándar:", std_dev)


# Genera un histograma de los valores de píxeles
hist_values, bin_edges = np.histogram(promedio_dark.flatten(), bins='auto')

# Histograma
plt.hist(promedio_dark.flatten(), bins=bin_edges, color='b', alpha=0.7, rwidth=0.85)
plt.xlabel('Valor del píxel')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valores de Píxeles')
plt.grid(axis='y', alpha=0.75)
plt.show()  # Muestra el histograma

# Muestra la imagen
plt.figure()
plt.imshow(promedio_dark, cmap='jet')
plt.title('Imagen TIFF')
plt.colorbar()
plt.show()  # Muestra la imagen

# Información sobre la forma de los datos (píxeles)
print("Forma de los datos:", promedio_dark.shape)

