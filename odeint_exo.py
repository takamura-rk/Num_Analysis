import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Exercice 2 de la fiche de TD5 en Python 
# Définir l'équation différentielle : y' = -0.1*y + cos(t)
def equation(y, t):
    return -0.1 * y + np.cos(t)


t = np.linspace(-1, 15, 300)


a = 2
sol_a2 = odeint(equation, a, t)

plt.figure(figsize=(10, 6))
plt.plot(t, sol_a2, label="a = 2", linewidth=2, color='blue')


for k in range(9):
    a_k = 0.5 * k
    sol = odeint(equation, a_k, t)
    plt.plot(t, sol, color='orange', alpha=0.7)

plt.title("Portrait de phase de y' + 0.1y = cos(t)")
plt.xlabel("temps t")
plt.ylabel("solution y(t)")
plt.grid(True)
plt.legend()
plt.show()
