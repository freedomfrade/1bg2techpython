# # sprawdzienie czy liczba jest pierwsza
# # n = int(input())

# # for i in range(2, n):
# #     if n % i == 0:
# #         print("Liczba jest pierwsza: ")
# #         exit(0)

# # print("Liczba nie jest pierwsza: ")

# # generowanie liczb pierwszych w przedziale p, q

# # p = int(input())
# # q = int(input())

# # for j in range(p, q+1):
# #     flaga = True
# #     for i in range(2, j):
# #         if j % i == 0:
# #             flaga = False
# #             break
# #     if flaga == True:
# #         print(j, end = "")

# # generowanie liczb pierwszych (pierwsze n liczb pierwszych)

# n = int(input("Podaj ile chcesz liczb pierwsczych"))
# k = 2
# ilosc = 0

# while 1:
#     flaga = True
#     for i in range(2, k):
#          if k % i == 0:
#              flaga = False
#              break
#     if flaga == True:
#         print(k, end=" ")
#         ilosc = ilosc + 1
#     if ilosc == n:
#         break
#     k = k + 1

# nwwwwwwwwwwwwwwwwwwwwwwwww

# a = int(input())
# b = int(input())

# while a != b:
#     if a > b: a = a - b
#     if b > a: b = b - a
# print(a)

# module

# a = int(input())
# b = int(input())

# while b > 0:
#     a, b = b, a % b
# print(a)


# def nww(a, b):
#     return a * b // nwd(a, b)


# a = int(input())
# b = int(input())

# w = a * b
# while b > 0:
#     a, b = b, a % b

# NWD = a
# NWW = w / NWD

# print(NWW)


# a = 1

# while True:
#     print(a ** 2)
#     a += 2


# suma = 0

# for i in range(10, 100):
#     suma = suma + i
# print(suma)

n = input()
suma = 0

for i in range(n):
    x = input()
    suma = suma + x
print(suma)

