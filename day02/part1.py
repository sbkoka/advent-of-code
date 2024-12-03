
num_safe = 0

with open("input.txt", "r") as file:
    for line in file:
        levels = [int(x) for x in line.split(" ")]
        increasing = True
        safe = True
        
        for i in range(1, len(levels)):
            level = levels[i]
            prev = levels[i - 1]
            if i == 1:
                if prev < level:
                    increasing = True
                elif prev > level:
                    increasing = False
                else: 
                    safe = False
                    break
            if (increasing and prev >= level) or (not increasing and prev <= level) or abs(prev - level) > 3:
                safe = False
                #print("not safe", line)
                break
        if safe:
            num_safe += 1
            #print("safe", line)
print(num_safe)

            
