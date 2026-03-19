n = str(input())
sothuong = 0
sohoa = 0
for i in n:
    if (ord(i) >= 65) and (ord(i) <= 90):
        sohoa += 1
    if (ord(i) >= 97) and( ord(i) <= 122):
        sothuong += 1
if sothuong >= sohoa:
    print(n.lower())
else :
    print(n.upper())
