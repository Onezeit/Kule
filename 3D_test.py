from vpython import sphere, color, canvas, rate, vector, mag
from punkty import punkty_pos

# Ustawienie sceny
scene = canvas()

# Tworzenie dużej kuli
promien_duzej_kuli = 1
duza_kula = sphere(pos=vector(0, 0, 0), radius=promien_duzej_kuli, color=color.blue, opacity=0.5)

# Tworzenie zielonych punktów na dużej kuli
zielone_kulki = [sphere(pos=p, radius=0.02, color=color.green, opacity=0) for p in punkty_pos]

# Tworzenie czerwonej kulki na środku dużej kuli
mala_kulka = sphere(pos=vector(10, 0, 0), radius=0.05, color=color.red)

# Parametry ruchu czerwonej kulki
v = vector(0, 0, 0)
dt = 0.05
czas_trwania = 100
masa_kulki = 1

# Listy do zapisywania pozycji
pozycje_x = []
pozycje_y = []
pozycje_z = []
energia_kinetyczna = []

# Pętla animacji
czas = 0  # Inicjalizacja zmiennej czasowej
while czas < czas_trwania:
    rate(100)

    # Wektory przyciągania do punktów na dużej kuli
    przyciaganie = vector(0, 0, 0)
    for zielona_kulka in zielone_kulki:
        wektor_do_punktu = zielona_kulka.pos - mala_kulka.pos
        przyciaganie += wektor_do_punktu.norm()

    # Normalizacja sumy wektorów przyciągania
    if przyciaganie.mag > 0:
        przyciaganie = przyciaganie.norm()

    # Aktualizacja prędkości i pozycji czerwonej kulki
    v += przyciaganie * dt
    mala_kulka.pos += v * dt

    # Zapisywanie pozycji do list
    pozycje_x.append(mala_kulka.pos.x)
    pozycje_y.append(mala_kulka.pos.y)
    pozycje_z.append(mala_kulka.pos.z)

    # Obliczanie i zapisywanie energii kinetycznej
    ek = 0.5 * masa_kulki * mag(v)**2
    energia_kinetyczna.append(ek)

    # Aktualizacja zmiennej czasowej
    czas += dt

    # Sprawdzenie, czy czerwona kulka nie przekroczyła granic dużej kuli
    if mag(mala_kulka.pos) > promien_duzej_kuli:
        # Umieszczenie czerwonej kulki na powierzchni dużej kuli
        mala_kulka.pos = mala_kulka.pos.norm() * promien_duzej_kuli
        v = vector(0, 0, 0)

with open('energia_kinetyczna.txt', 'w') as plik:
    for ek in energia_kinetyczna:
        plik.write(f'{ek}\n')

with open('pozycje_kulki00075.txt', 'w') as plik:
    for x, y, z in zip(pozycje_x, pozycje_y, pozycje_z):
        plik.write(f'{x}, {y}, {z}\n')
