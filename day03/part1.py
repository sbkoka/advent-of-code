import re

with open("input.txt", "r") as file:
    file_content = file.read()

pattern = r"(mul\(\d{1,3},\d{1,3}\))"
muls = re.findall(pattern, file_content)

sum = 0
for mul in muls:
    digits = [int(match) for match in re.findall(r"\d+", mul)]
    sum += digits[0] * digits[1]
print(sum)
