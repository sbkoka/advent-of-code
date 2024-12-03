
num_safe = 0
with open("small_input.txt", "r") as file:
    for line in file:
        levels = [int(x) for x in line.split(" ")]
        print(levels)
        increasing = True
        safe = True
        tolerance = True
        prev = -1
        skipFirst = False

        for i, level in enumerate(levels):
            print("i:", i, "prev:", prev)
            # if value is at the front or end check that the difference is < 4
            if i == 0 or prev == -1:
                next = levels[i + 1]
                # if diff > 3 or == 0, skip this value
                if abs(level - next) > 3 or level == next:
                    tolerance = False
                else:
                    print("safe")
                    prev = level
            elif i == len(levels) - 1:
                print("last")
                # if diff > 3 or == 0, skip this value
                if abs(prev - level) > 3 or level == prev:
                    if not tolerance: 
                        safe = False
                        print("exit")
                    else:
                        break
            # middle vals
            else:
                # calc diff between curr,prev and curr,next
                next = levels[i + 1]
                p_diff = prev - level
                n_diff = level - next
                print(p_diff, n_diff)
                # check if both diffs are in the same direction and < 4
                # if not, check to see if removing the value will satisfy the conditions
                if ((p_diff > 0 and n_diff > 0) or (p_diff < 0 and n_diff < 0)) and abs(p_diff) < 4 and abs(n_diff) < 4:
                    print("safe")
                    prev = level
                else:
                    # if i == 1 and 2nd - 3rd val is same sign as n_diff, try removing 0th
                    if i == 1:
                        n_n_diff = next - levels[i + 2]
                        if (n_n_diff > 0 and n_diff > 0) or (n_n_diff < 0 and n_diff < 0):
                            print("ignore first val")
                            prev = level
                            tolerance = False
                    # if i == second to last index, try to remove last value
                    elif i == len(levels) - 2 and tolerance:
                        break
                    # try removing the value
                    elif abs(prev - next) < 4 and tolerance:
                        print("remove:", level)
                        prev = prev
                        tolerance = False
                    else:
                        if not tolerance:
                            print("no tolerance")
                        else:
                            print(abs(prev - next), "too big diff")
                        print("exit", i)
                        safe = False
                        break
        if safe:
            print("safe", line)
            num_safe += 1 
        else:
            print("unsafe")      
            


        '''
        for i in range(1, len(levels)):
            level = int(levels[i])
            next_prev = int(levels[i])
            if i == 1 or skipFirst:
                skipFirst = False
                if prev < level:
                    increasing = True
                elif prev > level:
                    increasing = False
                else:
                    if tolerance:
                        tolerance = False
                        skipFirst = True
                        prev = next_prev
                        continue
                        print(prev)
                    else:
                        print(level, "no tolerance", line)
                        safe = False
                        break
            if increasing and (prev >= level or abs(prev - level) > 3):
                # remove curr val and change to decreasing
                if i == 1 and int(levels[i + 1]) < prev and abs(prev - int(levels[i + 1])) < 4 and tolerance:
                    print(level, "remove curr val and change to decreasing: ", line)
                    increasing = False
                    tolerance = False
                    next_prev = prev
                # remove the curr val
                elif i + 1 < len(levels) and int(levels[i + 1]) > prev and abs(prev - int(levels[i - 1])) < 4 and tolerance:
                    print(level, "remove curr val: ", line)
                    next_prev = prev
                    tolerance = False
                else:
                    print(level, "no tolerance inc", line)
                    safe = False
                    break
            if not increasing and (prev <= level or abs(prev - level) > 3):
                if i == 1 and int(levels[i + 1]) > prev and abs(prev - int(levels[i + 1])) < 4 and tolerance:
                    print(level, "remove curr val and change to increasing: ", line)
                    increasing = True
                    tolerance = False
                    next_prev = prev
                elif i + 1 < len(levels) and int(levels[i + 1]) < prev and abs(prev - int(levels[i - 1])) < 4 and tolerance:
                    print(level, "remove curr val: ", line)
                    tolerance = False
                    next_prev = prev
                else:
                    print(level, "no tolerance dec", line)
                    safe = False
                    break
            prev = next_prev
                # check if the value before the previous element is larger
                # or if its the first value set to decreasing if the next element is smaller
        if safe:
            num_safe += 1
            #print("safe", line)
        '''
print(num_safe)

            
