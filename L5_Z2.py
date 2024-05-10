import numpy as np
import matplotlib.pyplot as plt


def generate_compound_poisson_process_step_function(T, lambd_max, alpha):
    """
    Generuje próbę trajektorii złożonego procesu Poissona jako funkcję schodkową na odcinku [0, T].
        T: Czas trwania procesu.
        lambd_max: Maksymalna intensywność procesu Poissona.
        alpha: Parametr kontrolujący zmienność intensywności.

    Zwraca:
        t: Tablica punktów czasowych.
        Nt_step_function: Tablica wartości funkcji schodkowej złożonego procesu Poissona.
    """
    t = np.arange(0, T, 0.01)  # Punkty czasowe
    intensity = lambd_max * np.exp(-alpha * t)  # Zmienna intensywność procesu Poissona
    Nt = np.cumsum(np.random.poisson(intensity * 0.01, len(t)))
    Nt_step_function = np.zeros_like(t)
    for i, time in enumerate(t):
        Nt_step_function[i] = np.sum(Nt <= i)
    return t, Nt_step_function


T = 10
lambd_max = 1000
alpha = 0.1


t, Nt_step_function = generate_compound_poisson_process_step_function(
    T, lambd_max, alpha
)


plt.figure(figsize=(10, 5))
plt.step(t, Nt_step_function, where="post", color="blue")
plt.title("Trajektoria złożonego procesu Poissona")
plt.xlabel("Czas")
plt.ylabel("Wartość funkcji schodkowej")
plt.grid(True)
plt.show()
