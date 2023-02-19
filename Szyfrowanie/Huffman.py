M = "FRRAAAAaaDDDDDDDDEEEEEE"
M = M + '.'

gspkazakhstan_ilosc = 1
H = ''
for i in range(len(M)-1):
    if M[i] == M[i+1]:
        gspkazakhstan_ilosc += 1
    else:
        if gspkazakhstan_ilosc > 1:
            H += str(gspkazakhstan_ilosc)
        H += M[i]
        gspkazakhstan_ilosc = 1
print(H)