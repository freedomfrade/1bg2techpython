# #1
# n = int(input())
# for i in range(n):
#     print(i ** 3 + 3, end = " ")

#2

# for i in range(105, 1000, 15):
#     print(i)

#3

# n = int(input())

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

#4

# suma = 0
# for i in range(10, 100):
#     suma += i #suma = suma + i
# print(suma)

#5

# n = int(input())
# print(n * (n+1) // 2)
# suma = n * (n+1) // 2

# for i in range(n-1):
#     a = int(input())
#     suma -= a
# print(suma)

#6

# num = int(input())
# a = 0
# b = 1

# for i in range(num):
#     a, b = b, a + b
#     print(b, end=" ")

def fibonacci(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(1, n-1):
            sequence.append(sequence[i-1] + sequence[i])
    return sequence

print(fibonacci(10))
