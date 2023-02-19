from math import gcd

# 1. Wybór 2 dużych liczb pierwszych
p = int(input())
q = int(input())

# 2. Liczmy n = p*q oraz funkcje Eulera F = (p-1) * (q-1)
n = p * q
F = (p-1) * (q-1)

# 3. Generujemy klucz publiczby e taki, że NWD(F,e) = 1
for keypub in range(2, F):
    if gcd(keypub, F) == 1:
        e = keypub
        break
print(e, keypub)

# 4. Generujemy klucz prywatny d : d*e mod F == 1
for keypr in range(2,F):
    if ((keypr*e) % F) == 1:
        d = keypr
        break
print(d, n)

# 5. Przykład jak szyfrować?
# mamy m - message - wiadomość
# c = m**e % n (c - cipher - szyfrogram, tekst zaszyfrowany)
# t = c**d % n (t - text - tekst jawny - znów wiadomość m)

mas = input()
chiper = ""
for i in mas:
    chiper += chr((ord(i)**e)%n)

print(mas)
print(chiper)

tekst = ""
for i in chiper:
    tekst += chr((ord(i)**d)%n)
print(tekst)



