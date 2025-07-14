import numpy as np 
import matplotlib.pyplot as plt

def dicho(f,a,b,epsilon):
    fa,fb=f(a),f(b)
    if np.sign(fa)==np.sign(fb):
        print('les images des bords de l_intérvalle ne sont pas de signes opposés')
        return None, 0
    
    nb_iter=0
    while b-a>epsilon :
            c=(a+b)/2
            fc=f(c)
            if fc==0:
               return c, nb_iter
            
            if np.sign(fc)==np.sign(fa):
                a=c
                fa=fc
            else:
                b=c
            nb_iter+=1
    return (a+b)/2, nb_iter    

def f_1(x):
    return np.exp(x)+3*np.sqrt(x)-2

racine, iterations = dicho(f_1,0,1,1e-7)
print(racine, iterations)