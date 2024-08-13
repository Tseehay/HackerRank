k = list(map(int, input().split()))
a = [input().strip() for i in range(k[0])]
b = [input().strip() for i in range(k[1])]
for j in b:
    indices = []
    for x, y in enumerate(a):
        if j == y:
            indices.append(str(x + 1))
    print(' '.join(indices) if indices else -1)
