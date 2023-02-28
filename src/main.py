import point
import time
import plot
import platform

if __name__ =="__main__":
    print("Selamat datang di program Find Closest Point!!!")
    
    while (True):
        print("\nMenu")
        print("1. 3 Dimensional Space")
        print("2. Euclidean Space (Vector Rn)")
        print("3. Keluar Program")
        
        menuInp = int(input("Masukan pilihan menu: "))
        
        if (menuInp not in [1,2,3]):
            print("Pilihan menu tidak ada. Pilih kembali menu!")
        else:
            if (menuInp == 3):
                print("Terima kasih sudah menggunakan program kami. Sampai jumpa")
                exit()
            else:
                if (menuInp == 1):
                    nDim = 3
                else:
                    nDim = int(input("Dimensi: "))
                    
                nPoint = int(input("Banyak point: "))
                p = point.initializePoint(nPoint, nDim)

                print("Closest pair dengan Brute Force:")
                t1 = time.time()
                distBF, bf1, bf2, c1 = point.closestPairBF(p)
                t2 = time.time()
                print("Jarak terdekat", distBF)
                print("Titik 1:", bf1)
                print("Titik 2:", bf2)
                print("Waktu eksekusi (s):", t2-t1)
                print("Banyak operasi Euclidean Distance:", c1)
                print("Running on", platform.platform(), platform.processor())

                print("\nClosest pair dengan Divide and Conquer:")
                t1 = time.time()
                distDC, dc1, dc2, c2 = point.closestPairDNC(p)
                t2 = time.time()
                print("Jarak terdekat", distDC)
                print("Titik 1:", dc1)
                print("Titik 2:", dc2)
                print("Waktu eksekusi (s):", t2-t1)
                print("Banyak operasi Euclidean Distance:", c2)
                print("Running on", platform.platform(), platform.processor())

                if nDim==3:
                    plot.plot_3d(p, bf1, bf2)