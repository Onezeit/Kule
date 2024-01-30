# punkty.py
from vpython import vector, pi, cos, sin


def punkty_na_kuli(liczba_punktow, promien):
    punkty = []
    phi = pi * (3. - 5**0.5)  # Złoty kąt w radianach
    for i in range(liczba_punktow):
        y = 1 - (i / float(liczba_punktow - 1)) * 2  # y w zakresie od -1 do 1
        radius = (1 - y * y)**0.5  # promień okręgu odcinka sferycznego
        theta = phi * i  # kąt azymutalny

        x = cos(theta) * radius
        z = sin(theta) * radius
        punkty.append(vector(x, y, z) * promien)
    return punkty


# Lista wektorów pozycji punktów
punkty_pos = punkty_na_kuli(liczba_punktow=100, promien=1)
