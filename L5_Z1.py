import numpy as np
import matplotlib.pyplot as plt


def generate_poisson_process(T, lambd):
    """
    Generuje próbę trajektorii procesu Poissona na odcinku [0, T].
        T: Czas trwania procesu.
        lambd: Intensywność procesu Poissona.

    Zwraca:
        t: Tablica punktów czasowych.
        Nt: Tablica wartości procesu Poissona.
    """
    t = np.arange(0, T, 0.01)  # Punkty czasowe
    Nt = np.cumsum(np.random.poisson(lambd * 0.01, len(t)))
    return t, Nt


T = 5  # Czas trwania procesu
lambd = 2  # Intensywność procesu Poissona

# Generowanie trajektorii procesu Poissona
t, Nt = generate_poisson_process(T, lambd)

# Narysuj trajektorię procesu Poissona jako funkcję skokową
plt.figure(figsize=(10, 5))
plt.step(t, Nt, where="post", color="blue")
plt.title("Trajektoria procesu Poissona")
plt.xlabel("Czas")
plt.ylabel("Wartość funkcji skokowej")
plt.grid(True)
plt.show()
