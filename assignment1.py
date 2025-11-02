import numpy as np

def find_period(L0,L1):
    g= 9.81 #in m/s^2
    
    if not (isinstance(L0, int) and isinstance(L1, int)):
        print("Error : L0 and L1 must be integers!")
    elif not (L1 > L0 > 0):
        print("Eror : L1 must be greater than L0 and both > 0!")
    else: 
        for L in range(L0, L1 + 1):
            T= 2 * np.pi * np.sqrt(L/g)
            print("When L= %4.1f m, T= %4.1f s"% (float(L), T))
            
        T0= 2 * np.pi * np.sqrt(L0 / g)
        T1= 2 * np.pi * np.sqrt(L1 / g)
        return T0, T1