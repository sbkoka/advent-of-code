

num_safe = 0

def isSafe(levels):
    increasing = True
    safe = True
    unsafe_ind = -1
    for i in range(1, len(levels)):
        level = int(levels[i])
        prev = int(levels[i - 1])
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
            unsafe_ind = i - 1
            #print("not safe", line)
            break
    return [safe, unsafe_ind]
        #print("safe", line)

with open("input.txt", "r") as file:
    for line in file:
        levels = [int(x) for x in line.split(" ")]
        safe = isSafe(levels)
        tolerance = True

        if safe[0]:
            num_safe += 1
        else:
            unsafe_ind = safe[1]
            if unsafe_ind == -1:
                r_prev = levels[1:]
            else:
                r_prev = levels[:unsafe_ind] + levels[unsafe_ind + 1:]
            r_curr = levels[:unsafe_ind + 1] + levels[unsafe_ind + 2:]
            #print(levels)
            #print(r_prev)
            #print(r_curr)
            temp_safe = False
            if isSafe(r_prev)[0] or isSafe(r_curr)[0]:
                #print(levels)
                #print(tolerance)
                num_safe += 1
                temp_safe = True
            #print(levels, safe[1], levels[safe[1]])


            for i in range(len(levels)):
                remove = levels[:i] + levels[i+1:]
                if isSafe(remove)[0]:
                    if not temp_safe:
                        num_safe += 1
                        print(levels)
                    break
print(num_safe)