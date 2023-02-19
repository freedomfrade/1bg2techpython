#1
# for listopad in range(1, 31):
#     print(listopad, end=", ")

#2
# for i in range(1000):
#     if i % 2 != 0:
#         print(i ** 2)
    
#3
# for i in range(1000, 10000):
#     if i % 379 == 0:
#         print(i)

#4 
# for trzy in range(100, 1000):
#     if trzy % 11 == 0 and trzy % 5 == 0 and trzy % 6 == 0:
#         print(trzy)

#5

# n = int(input())
# suma = 0

# for i in range(n):
#     nl = int(input())
#     suma += nl
# print(suma)

#6

# k = int(input())
# suma = 0

# for i in range(0, 2 * k, 2):
#     suma += i
# print(suma)

#9

# ilosc = int(input("Podaj ilość liczb: "))
# l = 21
# suma = 0
# for i in range(0,ilosc+1):
#     for a in range(0,i,l):
#         print(l)
#         suma += l
#         l += 100


# w0 = int(input("Podaj wartość początkową inwestycji: "))
# L = int(input("Ile lat ma trwać inwestycja: "))
# wartosc = 0
# for i in range(0,L * 12):
#     wartosc = w0 * 0.06 * (1/12)
#     w0 += wartosc
# print(f"Końcowy kapitał wynosi: {w0}")

# w = int(input("Kwota wejściowa: "))
# L = float(input("Liczba lat: "))
# for i in range(int(L * 12)):
#     w += w * 0.005
# print(w)