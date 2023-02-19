napis = input("Napisz slowo: ")
szyfr = ""

for i in range(len(napis)):
    szyfr += chr(65 + (ord(napis[i])-65+3) % 26)
print(napis)
print(szyfr)

