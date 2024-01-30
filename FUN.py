# glowny.py
from vpython import sphere, color, canvas, rate, vector, mag
from punkty import punkty_pos

# Ustawienie sceny
scene = canvas()

# Tworzenie dużej kuli
promien_duzej_kuli = 1
duza_kula = sphere(pos=vector(0, 0, 0), radius=promien_duzej_kuli, color=color.blue, opacity=0.5)

# Tworzenie zielonych punktów na dużej kuli
zielone_kulki = [sphere(pos=p, radius=0.05, color=color.green) for p in punkty_pos]

# Wybieramy pozycję startową czerwonej kulki jako pozycję pierwszego zielonego punktu
# i przesuwamy ją nieznacznie
pozycja_startowa = punkty_pos[0]
przesuniecie = vector(1, 1, 1)  # Nieznaczne przesunięcie
pozycja_startowa_czerwonej_kulki = pozycja_startowa + przesuniecie

# Tworzenie większej czerwonej kulki w nieznacznie przesuniętej pozycji
promien_malej_kulki = 0.1
mala_kulka = sphere(pos=pozycja_startowa_czerwonej_kulki, radius=promien_malej_kulki, color=color.red)

# Parametry ruchu większej czerwonej kulki
v = vector(0, 0, 0)
dt = 0.01

# Pętla animacji
while True:
    rate(100)

    # Wektory przyciągania do punktów na dużej kuli
    przyciaganie = vector(0, 0, 0)
    for zielona_kulka in zielone_kulki:
        wektor_do_punktu = zielona_kulka.pos - mala_kulka.pos
        odleglosc_do_punktu = mag(wektor_do_punktu)
        if odleglosc_do_punktu > mala_kulka.radius:
            przyciaganie += wektor_do_punktu.norm() * (1 / odleglosc_do_punktu ** 2)

    # Aktualizacja prędkości i pozycji większej czerwonej kulki
    v += przyciaganie * dt
    mala_kulka.pos += v * dt

    # Odbicie od ściany dużej kuli
    if mag(mala_kulka.pos) > promien_duzej_kuli - promien_malej_kulki:
        # Ustawienie pozycji małej kulki na powierzchni dużej kuli
        mala_kulka.pos = mala_kulka.pos.norm() * (promien_duzej_kuli - promien_malej_kulki)
        # Odbicie (zmiana kierunku prędkości na przeciwny)
        v = -v  # Uwzględnienie utraty energii podczas odbicia
