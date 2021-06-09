def triplets(n):
    l = []
    for i in range(2, n):
        for j in range(1, i//2+1):
            l.append((j, i-j, i))
    return l

n = int(input())
print(triplets(n))