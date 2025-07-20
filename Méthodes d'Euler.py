import numpy as np 
import matplotlib.pyplot as plt 

def f_1(t,y):
    return -np.exp(t*y)

def euler_exp(f,y0,t_i,t_f,n):
    t_n=[t_i]
    y_n=[y0]
    while t_n[-1]<t_f:
        pas=(t_f-t_i)/n
        t=t_n[-1]+pas
        y=y_n[-1]+pas*f(t_n[-1],y_n[-1])
        t_n.append(t)
        y_n.append(y)
    return t_n, y_n

T_1,Y_1=euler_exp(f_1,1,-5,5,5000)


plt.plot(T_1, Y_1, label="f_1")
plt.legend()
plt.title("Méthode d'Euler explicite")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
