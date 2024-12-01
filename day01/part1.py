l = []
r = []
with open("input.txt", "r") as file:
    for line in file:
        formatted = line.strip().split("   ")
        l.append(int(formatted[0]))
        r.append(int(formatted[1]))

l.sort()
r.sort()
distance = 0
for i in range(len(l)):
    diff = abs(l[i] - r[i])
    distance += diff
print(distance)
