# #zad 1 

# n = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())



# #zad 3 

# n = int(input("Podaj liczbę trzycyfrowę: "))

# if n % 6 and n % 8 !=0:
#     print("tak")
# else:
#     print("nie")
    


# #zad 4

# for i in range(117, 999, 483):
#     print(i, end="")

while True:
    n = int(input())
    licz = 0
    for i in range(2, n):
        if n % i == 0:
            licz += 1
    
    if licz == 0:
        print("Liczba jest pierwsza")
    else:
        print("Liczba nie jest pierwsza")
    znak = input("Chcesz kolejną liczbe? T/N")
    if znak = 'N':
        break

