# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt
from matplotlib import style 

def loadData():
    #input_dir='C:/Users/PATH/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
    filename='energydata_complete.csv'

    # Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
    #datos=np.genfromtxt(filename,delimiter=';',skip_header=1)

    #alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
    datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = (0, 12), dtype=None, encoding=None)

    return datos


#Calculates the average of the data along an specific axis
#using numpy.average with just sums the values and divides them
#by the amount of values
#Parameters:
# - dataArray: raw data from csv
#Return: Average of data
def calculateAverage(dataArray):

    return np.average(dataArray)

#Calculates the median of the data using numpy.median
#which computes the median finding the X((n-1)/2), if
#n happened to be odd, it uses the average of the 2 middle
#values
#Parameters:
# - dataArray: sorted data from csv in ascending order
#Return: Median of data
def calculateMedian(dataArray):

    return np.median(dataArray)

#Auxiliare function for calling functions that calculate quantiles
#Parameters:
# - dataArray: sorted values from csv in ascending order
# - method: which of the methods know to use
#Return: list of quantiles
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

#Calculates quantiles using numpy.quantile whcih uses a linear method
#meaning it calculates the quantile using the following equation
# i + g = q*(n - alpha - beta + 1) + alpha
#where i is the floor and g the fractional part of the index q
#the default is the linear method which uses alpha = beta = 1
#Parameters:
# - dataArray: Sorted data array
#Return: Q1 and Q3
def calculateQuartilesNumpy(dataArray):

    Q1 = np.quantile(dataArray, q = 0.25)
    Q3 = np.quantile(dataArray, q = 0.75)

    return (Q1, Q3)

#Calculates quantiles using the ceiling of the 0.25*n th index and
#0.75*n th
#Parameters:
# - dataArray: Sorted data array
#Return: Q1 and Q3
def calculateQuartilesManually(dataArray):

    n = len(dataArray)

    Q1 = dataArray[mt.ceil(0.25*n)]
    Q3 = dataArray[mt.ceil(0.75*n)]

    return (Q1, Q3)

#Calculates the variance of the data using numpy.var
#using x's mean and 
def calculateVariance(dataArray):

    return np.var(dataArray)

#Calculates the standard deviation using the square root
#of the variance
#Parameters:
# - variance: N/A
#Return: square root of variance
def calculateStandardDeviation(variance):
    return np.sqrt(variance)

#Calculates the variance coefficient using
#standard deviation and average by dividing them in said respective order
#and multiplying it by 100
#Parameters:
# - standard deviation: N/A
# - average: N/A
#Return: result of substraction
def calculateVarianceCoeficient(standardDeviation, average):
    return (standardDeviation/average)*100

#Calculates the sample range substracting the max value in the data
#from the min value
#Parameters:
# - dataArraySorted: Sorted values in ascending order
#Return: result of substraction
def calculateSampleRange(dataArraySorted):
    return np.max(dataArraySorted) - np.min(dataArraySorted)

#Calculates the quantile range by substracting Q1 from Q3
#Parameters:
# - Q1: quantile 1
# - Q3: quantile 3
#Return: result of substraction
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
    
def histogram(dataArray, sampleRange):

    numOfClases = (mt.ceil(np.sqrt(len(dataArray))))

    interval = (sampleRange*(1+0.05))/numOfClases

    initialValue = dataArray.min()*0.99

    counts, bins, patches = plt.hist(dataArray,bins=numOfClases, edgecolor="black", rwidth=0.9)

    style.use('bmh')
    plt.xlabel("Porcentaje de Humedad")
    plt.ylabel("Frecuencia de mediciones")
    plt.title("Humedad presente en el baño")
    plt.xticks(ticks=bins)
    plt.show()

#This function generates the statistics for a sample of data
#Parameters:
# - printResults: bool indicating whether to print results to terminal
#Return: Returns a dictionary of the statistics for the sample data
#possible values for the dictionary are:
# average, median, quantiles (list of 2 values), variance, standardDeviation,
# varianceCoefficient, sampleRange, quantileRange 
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

    #Realizar histograma
    histogram(dataArraySorted, valuesObtained['sampleRange'])

    return valuesObtained


    

calculateStatistics(True)