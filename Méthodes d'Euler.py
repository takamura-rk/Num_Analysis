import numpy as np 
from scipy.optimize import fsolve
import matplotlib.pyplot as plt 


def f_1(t,y):
    return -np.exp(t*y)

def f_2(t,y):
    return 1/(1+t*y)    

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


def euler_imp(f,y0,t_i,t_f,h):
    t_n=[t_i]
    y_n=[y0]
    while t_n[-1] < t_f:
        t_1 = t_n[-1] + h
        y = y_n[-1]
        #On défini la fonction implicite : y_1 - y - h*f(t_1, y_1) = 0
        def fct_aux(y_1):
            return y_1 - y - h * f(t_1, y_1)

        y_1 = fsolve(fct_aux, y)[0] 
        t_n.append(t_1)
        y_n.append(y_1)

    return t_n, y_n
    
y0 = 1
t_i = -5
t_f = 5

T_1, Y_1 = euler_exp(f_2, y0, t_i, t_f, 5000)
t_1, y_1 = euler_imp(f_2, y0, t_i, t_f, 0.002)

plt.plot(T_1, Y_1, 'r-', label="Euler explicite")
plt.plot(t_1, y_1, 'b--', label="Euler implicite")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Comparaison Euler Explicite vs Implicite\npour $y' = \\frac{1}{1 + ty}$ avec $y(0) = 0$")
plt.grid(True)
plt.legend()
plt.show()

# Remarque :
# On observe une différence significative entre Euler explicite et Euler implicite :
# - La méthode explicite peut devenir instable ou diverger dans certaines zones de l’intervalle, 
#   notamment si t*y devient proche de -1 (ce qui rend f mal défini ou très grand).
# - La méthode implicite reste beaucoup plus stable et contrôle mieux les zones "dangereuses"
#   où la fonction f(t, y) varie fortement.
# Cela illustre un comportement classique dans les EDO non linéaires : 
# les méthodes implicites offrent une meilleure robustesse au détriment du coût de calcul.

