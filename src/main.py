import point

if __name__ =="__main__":
    print("Selamat datang di program Find Closest Point!!!")

    nPoint = int(input("Banyak point: "))
    nDim = int(input("Dimensi: "))
    p = point.initializePoint(nPoint, nDim)
    
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
    