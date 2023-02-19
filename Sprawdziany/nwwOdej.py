a, b = int(input()), int(input())
iloczyn = a * b

while a != b:
    if a > b: a = a - b
    if b > a: b = b - a
nwd = a

print(ilocyn // nwd)


# NWW 
 a,b = float(input()), float(input()) 
 il = a * b 
 while b > 0: 
     a, b = b, a % b 
 print(il / a)