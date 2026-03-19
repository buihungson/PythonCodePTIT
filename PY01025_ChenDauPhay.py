n = input()
s = n[::-1]
cnt = 0
res = ""
for i in s:
    if cnt == 3:
        res += ","
        cnt = 0
    res += i
    cnt += 1
res = res[::-1]
print(res)


