import re

with open("small_input_2.txt", "r") as file:
    file_content = file.read()

sum = 0
pattern = r"(mul\(\d{1,3},\d{1,3}\))"
segments = file_content.split("don't()")
for i, segment in enumerate(segments):
    after_do = segment[segment.find("do()"):]
    if i == 0:
        after_do = segment
    muls = re.findall(pattern, after_do)
    for mul in muls:
        digits = [int(match) for match in re.findall(r"\d+", mul)]
        sum += digits[0] * digits[1]
print(sum)
