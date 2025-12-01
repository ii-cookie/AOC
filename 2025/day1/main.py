import re
point = 50
count = 0
with open("input.txt", "r") as file:
    for line in file:   # start with L = minus, R = plus
        if re.search("^L", line):
            num = re.findall("[0-9]?[0-9]?[0-9]", line)
            for i in range(int(num[0])):
                point -= 1
                if (point % 100 == 0):
                    count += 1
        if re.search("^R", line):
            num = re.findall("[0-9]?[0-9]?[0-9]", line)
            for i in range(int(num[0])):
                point += 1
                if (point % 100 == 0):
                    count += 1

print(count)