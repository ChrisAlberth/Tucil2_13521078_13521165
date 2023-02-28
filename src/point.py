import math
import matplotlib.pyplot as plt
import random

#hitung jarak 2 point
def eucDistance(point1, point2, dimension):
    sum = 0
    i = 0
    for i in range(dimension):
        sum += (point1[i] - point2[i])**2
        
    return math.sqrt(sum)

#inisialisasi point secara random
def initializePoint(nPoint, nDimension):
    listOfPoints = []
    i = 0
    for i in range(nPoint):
        temp = []
        j = 0
        for j in range(nDimension):
            value = random.uniform(-100, 100)
            temp.append(value)
        
        listOfPoints.append(temp)
        
    return listOfPoints

#untuk menggabungkan 2 list secara terurut
def merge(list1, list2, axis): #axis = pengurutan point berdasarkan sumbu
    result = []
    n1 = len(list1)
    n2 = len(list2)
    
    i = 0
    j = 0
    while ((i < n1) and (j < n2)):
        if list1[i][axis] <= list2[j][axis]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
            
    while (i < n1):
        result.append(list1[i])
        i += 1
        
    while (j < n2):
        result.append(list2[j])
        j += 1
        
    return result
    
#sort dengan Divide and Conquer
def mergeSort(listOfPoints, axis):
    n = len(listOfPoints)
    mid = n//2
    
    if (n > 1):
        list1 = listOfPoints[0:mid]
        list2 = listOfPoints[mid:]
        
        sorted1 = mergeSort(list1, axis)
        sorted2 = mergeSort(list2, axis)
        
        result = merge(sorted1, sorted2, axis)
    else:
        result = listOfPoints
        
    return result
        
#mendapat point-point yang berada di strip area
def stripList(listOfPoints, middle, d):
    result = []
    for point in listOfPoints:
        if abs(point[0] - middle) < d:
            result.append(point)
            
    return result

#menentukan pasangan terdekat dengan Divide and Conquer
def closestPairDNC(listOfPoints):
    n = len(listOfPoints)
    sortedPoints = mergeSort(listOfPoints, 0)
    
    if n <= 3:
        d, point1, point2 = closestPairBF(sortedPoints)
    else:
        halfn = n//2
        
        if (n%2 == 0):
            space1 = sortedPoints[0:halfn]
            space2 = sortedPoints[halfn:n]
            middleLine = (sortedPoints[halfn-1][0] + sortedPoints[halfn][0]) / 2
        else:
            space1 = sortedPoints[0:halfn]
            space2 = sortedPoints[halfn+1:n]
            middleLine = sortedPoints[halfn][0]
            
        leftDist, leftPoint1, leftPoint2 = closestPairDNC(space1)
        rightdist, rightPoint1, rightPoint2 =  closestPairDNC(space2)
            
        if (leftDist < rightdist):
            d = leftDist
            point1 = leftPoint1
            point2 = leftPoint2
        else:
            d = rightdist
            point1 = rightPoint1
            point2 = rightPoint2
            
        stripPoint = stripList(sortedPoints, middleLine, d)
        sortedStrip = mergeSort(stripPoint, 1)
        
        stripDist, stripPoint1, stripPoint2 = closestPairBF(sortedStrip)
        
        if (stripDist < d):
            d = stripDist
            point1 = stripPoint1
            point2 = stripPoint2

    
    return d, point1, point2

#menentukan pasangan terdekat dengan Brute Force
def closestPairBF(listOfPoints):
    nPoints = len(listOfPoints)
    
    d = 100000
    pair1 = []
    pair2 = []
    i = 0
    for i in range(nPoints):
        for j in range(i+1,nPoints):
            distResult = eucDistance(listOfPoints[i], listOfPoints[j], len(listOfPoints[0]))
            if d > distResult:
                d = distResult
                pair1 = listOfPoints[i]
                pair2 = listOfPoints[j]
    
    return d, pair1, pair2
                
