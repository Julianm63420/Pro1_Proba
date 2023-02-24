# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np
import math as mt

def loadData():
    #input_dir='C:/Users/PATH/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
    filename='energydata_complete.csv'

    # Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
    #datos=np.genfromtxt(filename,delimiter=';',skip_header=1)

    #alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
    datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = (0, 12), dtype=None, encoding=None)

    return datos


def calculateAverage(dataArray):

    return np.average(dataArray)

def calculateMedian(dataArray):

    return np.median(dataArray)

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

    return (Q1, Q3)

def calculateQuartilesManually(dataArray):

    n = len(dataArray)

    Q1 = dataArray[mt.ceil(0.25*n)]
    Q3 = dataArray[mt.ceil(0.75*n)]

    return (Q1, Q3)

def calculateVariance(dataArray):

    return np.var(dataArray)

def calculateStandardDeviation(variance):
    return np.sqrt(variance)

def calculateVarianceCoeficient(standardDeviation, average):
    return (standardDeviation/average)*100

def calculateSampleRange(dataArraySorted):
    return np.max(dataArraySorted) - np.min(dataArraySorted)

def calculateQuantileRange(Q1, Q3):
    return Q3 - Q1

def printValues(valuesObtained):
    print("Datos has the following values\n"
          + "Average: " + str(valuesObtained['average']) + "\n"
          + "Median: " + str(valuesObtained['median']) + "\n"
          + "Q1: " + str(valuesObtained['quantiles'][0]) + "\n"
          + "Q3: " + str(valuesObtained['quantiles'][1]) + "\n"
          + "Variance: " + str(valuesObtained['variance']) + "\n"
          + "Standard Deviation: " + str(valuesObtained['standardDeviation']) + "\n"
          + "Variance Coeficient: " + str(valuesObtained['varianceCoeficient']) + "\n"
          + "Sample Range: " + str(valuesObtained['sampleRange']) + "\n"
          + "Quantile Range: " + str(valuesObtained['quantileRange']) + "\n")

    

def calculateStatistics(printResults):

    datos = loadData()
    
    dateArray = []
    dataArray = []

    valuesObtained = dict()

    for line in datos:
        dateArray.insert(0, line[0])
        dataArray.insert(0, line[1])

    dataArraySorted = np.sort(dataArray)
    
    #Calcular promedio
    valuesObtained['average'] = calculateAverage(dataArray)

    #Calcular mediana
    valuesObtained['median'] = calculateMedian(dataArraySorted)

    #Calcular Quartiles
    valuesObtained['quantiles'] = calculateQuartiles(dataArraySorted, "manual")

    #Calcular varianza muestral
    valuesObtained['variance'] = calculateVariance(dataArraySorted)

    #Calcular desviación estándar
    valuesObtained['standardDeviation'] = calculateStandardDeviation(valuesObtained['variance'])

    #Calcular coeficiente de variación
    valuesObtained['varianceCoeficient'] = calculateVarianceCoeficient(valuesObtained['standardDeviation'],
                                                                        valuesObtained['average'])

    #Calcular rango muestral
    valuesObtained['sampleRange'] = calculateSampleRange(dataArraySorted)

    #Calcular rango interquartil
    valuesObtained['quantileRange'] = calculateQuantileRange(valuesObtained['quantiles'][0],
                                                              valuesObtained['quantiles'][1])

    if printResults:
        printValues(valuesObtained)

    return valuesObtained


    

calculateStatistics(True)