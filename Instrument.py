import collections
import numpy as np

k = np.power(2,1./12)

def get_keys():
    aha = []
    n = 0
    for i in range(2,63):
        if(i%7==0):
            n=n+1
        nota = chr(ord('A')+(i%7)) + str(n)
        aha.append(nota)
    return aha

def get_vals():
    vals = [16,18,21,22,25,28,31,33,37,41,44,49,55,62,65,73,82,87,98]
    for i in range(-1,43):
        if((i%7==1) or (i%7==4)):
            tmp = vals[-1]*k
            vals.append(round(tmp))
        else:
            tmp = vals[-1]*k
            tmp = tmp * k
            vals.append(tmp)
    return vals

notes_freqs = dict(zip(get_keys(),get_vals()))

for key in notes_freqs:
    print(key,notes_freqs[key])