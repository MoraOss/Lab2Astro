import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Ruta de tu archivo TIFF
ruta_archivo_tiff = r'J:\UC\Segundo Semestre 2023\Laboratorio de Instrumentación Astronómica\Lab 2\Nueva carpeta\Darks de 23 seg\Image0002.tiff'

# Abre el archivo TIFF con Pillow
imagen = Image.open(ruta_archivo_tiff)

# Convierte la imagen a un arreglo NumPy
data = np.array(imagen)

# Calcula la desviación estándar de los valores de píxeles
std_dev = np.std(data)
print("Desviación Estándar:", std_dev)

# Genera un histograma de los valores de píxeles
hist_values, bin_edges = np.histogram(data.flatten(), bins='auto')

plt.hist(data.flatten(), bins=bin_edges, color='b', alpha=0.7, rwidth=0.85)
plt.xlabel('Valor del píxel')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valores de Píxeles')
plt.grid(axis='y', alpha=0.75)

# Muestra la imagen
plt.figure()
plt.imshow(data, cmap='jet')
plt.title('Imagen TIFF')
plt.colorbar()
plt.show()

# Información sobre la forma de los datos (píxeles)
print("Forma de los datos:", data.shape)
