import point
import time
import plot

if __name__ =="__main__":
    print("Selamat datang di program Find Closest Point!!!")

    nPoint = int(input("Banyak point: "))
    nDim = int(input("Dimensi: "))
    p = point.initializePoint(nPoint, nDim)
    
    print("Closest pair dengan Brute Force:")
    t1 = time.time()
    distBF, bf1, bf2 = point.closestPairBF(p)
    t2 = time.time()
    print("Jarak terdekat", distBF)
    print("Titik 1:", bf1)
    print("Titik 2:", bf2)
    print("Waktu eksekusi (s):", t2-t1)
    
    print("Closest pair dengan Divide and Conquer:")
    t1 = time.time()
    distDC, dc1, dc2 = point.closestPairDNC(p)
    t2 = time.time()
    print("Jarak terdekat", distDC)
    print("Titik 1:", dc1)
    print("Titik 2:", dc2)
    print("Waktu eksekusi (s):", t2-t1)
    
    if nDim==3:
        plot.plot_3d(p, bf1, bf2)