# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np

#input_dir='C:/Users/PATH/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename='energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
#datos=np.genfromtxt(filename,delimiter=';',skip_header=1)

#alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = (0, 12))

print("Done")

# Su código va aquí...
