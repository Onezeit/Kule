import matplotlib.pyplot as plt
import numpy as np

# Odczytywanie danych z pliku
with open('energia_kinetyczna.txt', 'r') as plik:
    dane_energii = [float(linia.strip()) for linia in plik]

# Tworzenie osi czasu na podstawie liczby odczytanych wartości i kroku czasowego dt
dt = 0.05  # Załóżmy, że krok czasowy wynosi 0.05 sekundy
czas = [dt * i for i in range(len(dane_energii))]

# Wygładzenie danych przez uśrednienie ruchome (opcjonalnie)
rozmiar_okna = 5  # Ustalamy szerokość okna uśredniającego
dane_wygladzone = np.convolve(dane_energii, np.ones(rozmiar_okna)/rozmiar_okna, mode='valid')

# Tworzenie wykresu
plt.figure(figsize=(12, 8))
# Jeśli zdecydujemy się na wyświetlanie punktów, możemy zastosować mniejszy rozmiar i przeźroczystość
# plt.scatter(czas[:len(dane_wygladzone)], dane_wygladzone, color='blue', alpha=0.5, s=10)
plt.plot(czas[:len(dane_wygladzone)], dane_wygladzone, color='blue', linewidth=2)
plt.title("Wykres energii kinetycznej czerwonej kulki od czasu")
plt.xlabel("Czas [s]")
plt.ylabel("Energia kinetyczna [J]")
plt.grid(True)
plt.tight_layout()  # Aby zapobiec obcinaniu etykiet
plt.show()
