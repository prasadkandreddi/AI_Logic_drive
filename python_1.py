n = int(input())
a = []
for _ in range(n):
    s, e = map(int, input().split())
    a.append((s, e))
    
a.sort()

res = [a[0]]
for s, e in a[1:]:
    if s <= res[-1][1]:
        res[-1] = (res[-1][0], max(res[-1][1], e))
    else:
        res.append((s, e))

for s, e in res:
    print(s, e)