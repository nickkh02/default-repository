from sys import argv
import itertools

script, n, m = argv

n, m = int(n), int(m)
d = ([*range(1, n+1)])
z = d
g = [1, ]

g.append(*list(itertools.islice(d, m-1, None, m-1)))

while True:
    z = z[m-1:] + z[:m-1]
    g.append(*list(itertools.islice(z, m-1, None, m-1)))
    if g[0] == g[-1] and len(g) > 0:
        g.pop(-1)
        print(*g, sep='')
        break
    else:
        pass