import matplotlib.pyplot as plt

# Wczytanie danych z pliku
with open('pozycje_kulki00075.txt', 'r') as plik:
    linie = plik.readlines()

# Listy do przechowywania danych
pozycje_x = []
pozycje_y = []
pozycje_z = []
czasy = []

# Przetwarzanie danych
for i, linia in enumerate(linie):
    x, y, z = map(float, linia.strip().split(', '))
    pozycje_x.append(x)
    pozycje_y.append(y)
    pozycje_z.append(z)
    czasy.append(i * 0.1)  # Zakładając, że dt = 0.1 w symulacji

# Tworzenie wykresów
plt.figure(figsize=(12, 8))

# Wykres x(t)
plt.subplot(3, 1, 1)
plt.plot(czasy, pozycje_x, label='x(t)')
plt.xlabel('Czas [s]')
plt.ylabel('Pozycja x')
plt.title('Wykres x od czasu')
plt.grid(True)
plt.legend()

# Wykres y(t)
plt.subplot(3, 1, 2)
plt.plot(czasy, pozycje_y, label='y(t)')
plt.xlabel('Czas [s]')
plt.ylabel('Pozycja y')
plt.title('Wykres y od czasu')
plt.grid(True)
plt.legend()

# Wykres z(t)
plt.subplot(3, 1, 3)
plt.plot(czasy, pozycje_z, label='z(t)')
plt.xlabel('Czas [s]')
plt.ylabel('Pozycja z')
plt.title('Wykres z od czasu')
plt.grid(True)
plt.legend()

# Wyświetlenie wykresów
plt.tight_layout()
plt.show()
