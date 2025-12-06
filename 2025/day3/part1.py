def findMax(string):    # goal is find the largest number in the string, then return both number and the index
    max = -1
    max_index = -1
    for index in range(len(string)):
        if string[index] == '\n':
            continue
        num = int(string[index])
        if num > max:
            max = num
            max_index = index
            
    return max_index, str(max)
        
def findFirst_digit(string):  # returns the first dig index and the first dig value, needs to remove the last digit cuz it cannot be the last digit
    # print(findMax(string[:-1]))
    return findMax(string[:-1])

def findSecond_digit(string, first_digit_index):    # second digit index wont be correct cuz start index is different but its fine cuz wont be used
    # print(findMax(string[first_digit_index+1:]))
    return findMax(string[first_digit_index+1:])

with open("input.txt", "r") as file:
    
    sum = 0
    
    for line in file:   
        line = line.strip()
        first_digit_index, first_digit_str = findFirst_digit(line)
        second_digit_index, second_digit_str = findSecond_digit(line, first_digit_index)
        
        string_val = int(first_digit_str + second_digit_str)
        sum += string_val
        print(string_val)
        
print(sum)