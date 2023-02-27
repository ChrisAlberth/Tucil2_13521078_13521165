import point

if __name__ =="__main__":
    print("Find Closest Pair")
    n = int(input("Banyak point: "))
    p = point.initializePoint(n)
    
    print("Closest pair dengan Brute Force:")
    distBF, bf1, bf2 = point.closestPairBF(p)
    print("Jarak terdekat", distBF)
    print("Titik 1:", bf1)
    print("Titik 2:", bf2)
    
    print("Closest pair dengan Divide and Conquer:")
    distDC, dc1, dc2 = point.closestPairDNC(p)
    print("Jarak terdekat", distDC)
    print("Titik 1:", dc1)
    print("Titik 2:", dc2)