
def check(s):
    if len(s) % 2 != 0:
        return False
    if s != s[::-1]:
        return False
    for char in s:
        if char not in '02468':
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n):

        if check(str(i)):
            print(str(i), end=' ')
    print()
