from collections import Counter

l = []
r = []
with open("input.txt", "r") as file:
    for line in file:
        formatted = line.strip().split("   ")
        l.append(int(formatted[0]))
        r.append(int(formatted[1]))

r_c = Counter(r)

l.sort()
r.sort()
similarity = 0
for i in range(len(l)):
    curr = l[i]
    if curr in r_c:
        similarity += curr * r_c[curr]
print(similarity)
