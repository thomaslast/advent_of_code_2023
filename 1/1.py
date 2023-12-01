import regex as re

output = []
text_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
total = 0
with open("input.txt") as f:
    input_lines = f.readlines()

txt_num_regex = ""
for key in text_numbers.keys():
    txt_num_regex += f"{key}|"

for line in input_lines:
    matches = re.findall(f"{txt_num_regex}[0-9]", line, overlapped=True)
    numbers_list = []
    for num in matches:
        if num in text_numbers.keys():
            numbers_list.append(text_numbers[num])
        else:
            numbers_list.append(num)

    cal = int(f"{numbers_list[0]}{numbers_list[-1]}")
    total += cal
    output.append(cal)

print(total)