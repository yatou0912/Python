def triangles():
    L = [1]
    while True:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i+1] for i in range(len(L)-1)]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)
