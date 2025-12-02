import re


sum = 0
def isInvalid(id):
    
    i = 1
    
    i = int(len(id)/2)  
    j = 0   # position of subarray
    if (id[j:j+i] == id[j+i:j+i+i]):    # when it is 123123, pos of first is 0, next one is 3
        return True
    
    # i = 2
    
    # while i < len(id):
    #     if len(id) % i != 0:
    #         continue

    #     subarrayNum = int(len(id) / i)
        
    #     j = 0   # position of subarray
    #     check = id[j:j+i]
        
    #     while j < subarrayNum:
            
    #         if (check != id[i*j:i*(j+1)]):    # when it is 123123, pos of first is 0, next one is 3
    #             return False
            
    #         j+=1      

    #     i += 1
    return False
        
# with open("input.txt", "r") as file:
#     sum = 0
#     for line in file: 
#         id_list = re.split(",", line)
#         for id in id_list:
#             start, end = re.split("-", id)
#             start = int(start)
#             end = int(end)
#             while start <= end:
#                 string = str(start)
#                 isInvalid(string)
#                 start += 1
                
line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
id_list = re.split(",", line)
for id in id_list:
    start, end = re.split("-", id)
    start = int(start)
    end = int(end)
    while start <= end:
        string = str(start)
        
        if(isInvalid(string)):
            sum += start
            print(start)
        start += 1
print(sum)