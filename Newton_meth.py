import matplotlib.pyplot as plt
import numpy as np 

def f(x):
    return x**2-2

def f_prime(x):
    return 2*x

def phi1(x):
    return x-f(x)/f_prime(x)

def phi2(x):
    return x-1/2*(x**2-2)

def Itern(phi,x_0,N):
    x=[x_0]
    for i in range (N):
        x_next=phi(x[-1])
        x.append(x_next)
    return x
   
X_1=Itern(phi1,1,20)
print(X_1)
X_2=Itern(phi2,1,20)
print(X_2)

x = list(range(len(X_1)))

# Axe y = valeurs de la suite
y_1 = X_1
y_2 = X_2
# Tracé
fig, ax = plt.subplots()
ax.plot(x, y_1, marker='o', label='Méthode de Newton')
ax.plot(x, y_2, marker='s', label='Méthode alternative')
ax.set_ylim(0, 3)
ax.set_xlabel("n (indice)")
ax.set_ylabel("xₙ (valeur de la suite)")
ax.set_title("Convergence de la méthode de Newton")
plt.grid(True)
plt.show()