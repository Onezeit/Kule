from vpython import *

# Ustawienie sceny
scene = canvas()

# Tworzenie dużej kuli
duza_kula = sphere(pos=vector(0, 0, 0), radius=1, color=color.blue, opacity=0.5)

# Definiowanie pierwszego zielonego punktu na powierzchni dużej kuli
zielony_punkt_1_pos = vector(0, duza_kula.radius, 0)
zielony_punkt_1 = sphere(pos=zielony_punkt_1_pos, radius=0.05, color=color.green)

# Definiowanie drugiego zielonego punktu na powierzchni dużej kuli
zielony_punkt_2_pos = vector(duza_kula.radius, 0, 0)
zielony_punkt_2 = sphere(pos=zielony_punkt_2_pos, radius=0.05, color=color.green)

# Definiowanie trzeciego zielonego punktu na powierzchni dużej kuli
zielony_punkt_3_pos = vector(-duza_kula.radius, 0, 0)
zielony_punkt_3 = sphere(pos=zielony_punkt_3_pos, radius=0.05, color=color.green)

# Definiowanie czwartego zielonego punktu na powierzchni dużej kuli
zielony_punkt_4_pos = vector(duza_kula.radius, duza_kula.radius, duza_kula.radius)
zielony_punkt_4 = sphere(pos=zielony_punkt_4_pos, radius=0.05, color=color.green)

# Tworzenie małej czerwonej kulki na przeciwległym biegunie pierwszego zielonego punktu
mala_kulka = sphere(pos=vector(0, -duza_kula.radius, 0), radius=0.05, color=color.red)

# Parametry ruchu małej czerwonej kulki
v = vector(0, 0, 0)  # Początkowa prędkość małej czerwonej kulki
dt = 0.01  # Krok czasowy

# Pętla animacji
while True:
    rate(100)

    # Wektory przyciągania do obu zielonych punktów
    przyciaganie_1 = zielony_punkt_1_pos - mala_kulka.pos
    przyciaganie_2 = zielony_punkt_2_pos - mala_kulka.pos
    przyciaganie_3 = zielony_punkt_3_pos - mala_kulka.pos
    przyciaganie_4 = zielony_punkt_3_pos - mala_kulka.pos

    # Normalizacja i skalowanie wektorów przyciągania
    przyciaganie = (przyciaganie_1.norm() + przyciaganie_2.norm() + przyciaganie_3.norm() + przyciaganie_4.norm()) * 0.005

    # Aktualizacja prędkości i pozycji małej czerwonej kulki
    v += przyciaganie
    mala_kulka.pos += v * dt
