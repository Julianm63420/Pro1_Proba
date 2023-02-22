# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np
import math as mt

#input_dir='C:/Users/PATH/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename='energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
#datos=np.genfromtxt(filename,delimiter=';',skip_header=1)

#alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = (0, 12), dtype=None)

def calculateAverage(dataArray):

    result = np.average(dataArray)

    print("Datos has an average of " + str(result))

    return result

def calculateMedian(dataArray):

    result = np.median(dataArray)

    print("Datos has a median of " + str(result))

    return result

def calculateQuartiles(dataArray, method):

    method = method.lower()

    result = None
    
    match method:

        case "numpy":
            return calculateQuartilesNumpy(dataArray)
        case "manual":
            return calculateQuartilesManually(dataArray)
        case _:
            return (None, None)

def calculateQuartilesNumpy(dataArray):

    Q1 = np.quantile(dataArray, q = 0.25)
    Q3 = np.quantile(dataArray, q = 0.75)

    print("Datos has a Q1 of " + str(Q1))
    print("Datos has a Q3 of " + str(Q1))

    return (Q1, Q3)

def calculateQuartilesManually(dataArray):

    n = len(dataArray)

    Q1 = dataArray[mt.ceil(0.25*n)]
    Q3 = dataArray[mt.ceil(0.75*n)]

    print("Datos has a Q1 of " + str(Q1))
    print("Datos has a Q3 of " + str(Q1))

    return (Q1, Q3)

def calculateVariance(dataArray):

    variance = np.var(dataArray)
    print("Datos has a variance of " + str(variance))

    return variance
    

def calculateStatistics(datos):

    dateArray = []
    dataArray = []

    for line in datos:
        dateArray.insert(0, line[0])
        dataArray.insert(0, line[1])

    dataArraySorted = np.sort(dataArray)
    
    #Calcular promedio
    average = calculateAverage(dataArray)

    #Calcular mediana
    median = calculateMedian(dataArraySorted)

    #Calcular Quartiles
    quartiles = calculateQuartiles(dataArraySorted, "manual")

    #Calcular varianza muestral
    variance = calculateVariance(dataArraySorted)

    #Calcular desviación estándar
    standardDeviation = np.sqrt(variance)

    #Calcular coeficiente de variación
    coeficient = (standardDeviation/average)*100
    print("Datos has a coeficient of variance of " + str(coeficient))

    #Calcular rango muestral
    sampleRange = np.max(dataArraySorted) - np.min(dataArraySorted)
    print("Datos has a sample range of " + str(sampleRange))

    #Calcular rango interquartil
    quantileRange = quartiles[1] - quartiles[0]
    print("Datos has a quantile range of " + str(quantileRange))


    

calculateStatistics(datos)