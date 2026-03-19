n = input()
res = ""
for i in n:
    if i == " ":
        print(res)
        res = ""
    else:
        res += i
if res != "":
    print(res)