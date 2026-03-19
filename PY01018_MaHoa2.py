p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    t = input().split()
    k = int(t[0])
    if k == 0:
        break
    s = t[1]

    res = ""
    for ky_tu in s:
        i = p.find(ky_tu)

        vi_tri_moi = (i+k) % 28
        res += p[vi_tri_moi]
    last_res = res[::-1]
    print(last_res)