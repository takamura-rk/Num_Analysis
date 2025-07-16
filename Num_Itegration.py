import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import quad 
import time  


def f(x):
    return np.exp(-x**2)*np.sin(x)**2

x=np.linspace(-3,3,100)
y=f(x)

plt.figure(figsize=(4,3))
plt.plot(x,y)
plt.show()
#quad renvoie 2 valeurs la première est la valeur aprochée de l'intégral et la deuxième est l'erreur numérique 
result=quad(f,-2,2)
print(result)

#options utile de quad
#Intégration sur des intervalles infinis :
result=quad(f,-np.inf,np.inf)

def integrand(x, a, b):
    return a * x**2 + b

# fonction avec paramétre. a=2, b=3 passés via args
quad(integrand, 0, 1, args=(2, 3))

#gestion des discontinuités
quad(lambda x: 1/(x-1), 0, 2, points=[1])

