def check(a):
    b = a[::-1]
    if b != a or len(a) % 2 != 0: return False

    for x in a:
        if int(x) % 2 == 1:
            return False
    return True



for _ in range(int(input())):
    n = int(input())
    for i in range(22, n, 2):
        if check(str(i)):
            print(i, end=" ")
    print()
