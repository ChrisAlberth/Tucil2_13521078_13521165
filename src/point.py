import math
import matplotlib.pyplot as plt
import random
import numpy as np      

#hitung jarak 2 point
def eucDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

#inisialisasi point secara random
def initializePoint(nPoint):
    listOfPoints = []
    i = 0
    for i in range (nPoint):
        x = random.uniform(-1000,1000)
        y = random.uniform(-1000,1000)
        z = random.uniform(-1000,1000)
        
        listOfPoints.append([x,y,z])
        
    return listOfPoints

#menentukan pasangan terdekat dengan Divide and Conquer
def closestPairDNC(listOfPoints):
    nPoint = len(listOfPoints)

    # d jarak, pair1 = point pertama, pair2 = point kedua
    d1, p11, p12 = closestPairInArea(listOfPoints, nPoint)
    d2, p21, p22 = compareStrip(listOfPoints)
    
    if (d1 < d2):
        return d1, p11, p12
    else:
        return d2, p21, p22
    

#menentukan pasangan point terdekat dari 2 area
#masih error    
def closestPairInArea(listOfPoints, n):
    listOfPoints = np.sort(listOfPoints, axis=0)
    
    if n == 2:
        d = eucDistance(listOfPoints[0], listOfPoints[1])
        pair1 = listOfPoints[0]
        pair2 = listOfPoints[1]
    else:
        S1 = []
        S2 = []
        i = 0
        for i in range(n):
            if i < n/2:
                S1.append(listOfPoints[i])
            else:
                S2.append(listOfPoints[i])
                
        # d jarak, pair1 = point pertama, pair2 = point kedua
        d1, leftPair1, leftPair2 = closestPairInArea(S1, len(S1)) 
        d2, rightPair1, rightPair2 = closestPairInArea(S2, len(S2))

        if d1 <= d2:
            d = d1
            pair1 = leftPair1
            pair2 = leftPair2
        else:
            d = d2
            pair1 = rightPair1
            pair2 = rightPair2
    
    return d, pair1, pair2

#mencari pasangan terdekat di strip area
#masih error
def compareStrip(listOfPoints):
    nPoints = len(listOfPoints)
    mid = nPoints/2
    if nPoints % 2 == 0:
        l = (listOfPoints[mid-1][0] + listOfPoints[mid][0])/2.0
    else:
        l = listOfPoints[mid][0]
        
    pointInStrip = []
    for point in listOfPoints:
        if point[0] > l - d and point[0] < l + d:
            pointInStrip.append(point)
            
    nStrip = len(pointInStrip)
    d = 1000000
    pair1 = []
    pair2 = []
    i = 0
    for i in range(nStrip):
        j = i + 1
        for j in range(nStrip):
            distResult = eucDistance(pointInStrip[i], pointInStrip[j])
            if d > distResult:
                d = distResult
                pair1 = pointInStrip[i]
                pair2 = pointInStrip[j]
                
    return d, pair1, pair2

#menentukan pasangan terdekat dengan Brute Force
def closestPairBF(listOfPoints):
    nPoints = len(listOfPoints)
    
    d = 100000
    pair1 = []
    pair2 = []
    i = 0
    for i in range(nPoints):
        for j in range(i+1,nPoints):
            distResult = eucDistance(listOfPoints[i], listOfPoints[j])
            if d > distResult:
                d = distResult
                pair1 = listOfPoints[i]
                pair2 = listOfPoints[j]
    
    return d, pair1, pair2
                
