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
    # print(findMax(string[first_digit_index+1:]))  # to fix the start index, imagine 012345, wanted ans = 4, first digit index = 2, array started with 3, returned with 1,
    return findMax(string[first_digit_index+1:])    #  fixed ans = returned + 1 + first index

# with 12 digits, first digit cannot be last 12 digit of string, meaning [:-11] -11 = - (12-1)
# second would be [first digit index + 1:-10] ... 11th would be [previous digit index + 1:-1] - (12-11)

class data:
    def __init__(self, index, value):
        self.index = index
        self.value = value

def find12_digits(string):
    start_index = 0
    string_of_12digit = ""
    for i in range(12):
        end_index = -1 * (12 - i - 1)
        number = data()
        number.index, number.value = findMax(string[start_index : end_index])
        string_of_12digit += number.value
        start_index = number.index + 1 + start_index
    print(string_of_12digit)
    return string_of_12digit
        
        

with open("input.txt", "r") as file:
    
    sum = 0
    
    for line in file:   
        line = line.strip()
        find12_digits(line)
        # sum += string_val
        # print(string_val)
        
print(sum)