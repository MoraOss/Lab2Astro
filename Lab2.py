import numpy as np
import matplotlib.pyplot as plt

from scipy import stats
from astropy.io import fits
from astropy.visualization import hist
from astropy.stats import mad_std
from astropy.nddata import CCDData

file = fits.open(r'J:\UC\Segundo Semestre 2023\Laboratorio de Instrumentación Astronómica\Lab 2\Nueva carpeta\Image0002.tiff')

#Getting information from fits file
file.info()

#Read data from Primary HDU
data = file[0].data
std_dev = np.std(data)
print(std_dev)

hist_values, bin_edges = np.histogram(data.flatten(), bins='auto')

hist(data.flatten(), bins=bin_edges, color='b', alpha=0.7, rwidth=0.85)
plt.xlabel('Valor del píxel (ADU)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Valores de Píxeles')
plt.grid(axis='y', alpha=0.75)


np.shape(data) #gives shape of data (pixels)
plt.imshow(data,cmap='jet') #plot the 2D image with imshow on linear scale, CCD detectors are linear
plt.show()
