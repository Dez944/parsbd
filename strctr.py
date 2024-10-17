from pars import tsts, resl, dat

key_z = list(zip(tsts, resl, dat))
cl = dict.fromkeys(sorted(set(tsts)))
for i in key_z:
    if cl[i[0]] is None:
        cl[i[0]] = []
    cl[i[0]].append((i[1], i[2]))
print(cl)
