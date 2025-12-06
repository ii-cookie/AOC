
def isPaperRoll(char):
    if char == "@":
        return True
    else: 
        return False
    
def checkSurround(row, col, map):
    sum = 0
    if isPaperRoll(map[row + 1][col + 1]):
        sum += 1
    if isPaperRoll(map[row + 1][col]):
        sum += 1
    if isPaperRoll(map[row + 1][col - 1]):
        sum += 1

    if isPaperRoll(map[row][col + 1]):
        sum += 1
    if isPaperRoll(map[row][col - 1]):
        sum += 1

    if isPaperRoll(map[row - 1][col + 1]):
        sum += 1
    if isPaperRoll(map[row - 1][col]):
        sum += 1
    if isPaperRoll(map[row - 1][col - 1]):
        sum += 1
    return sum

def canAccess(row, col, map):
    if isPaperRoll(map[row][col]):
        if checkSurround(row, col, map) < 4:
            # print(map[row + 1][col + 1] + map[row + 1][col] + map[row + 1][col - 1] + "\n" + map[row][col + 1] + map[row][col] + map[row][col - 1] + "\n" + map[row - 1][col + 1] + map[row - 1][col] + map[row - 1][col - 1])
            # print("==========")
            return True
    return False

def countAccess(map):
    access_list = []
    count = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if canAccess(row,col,map):
                # print(count)
                access_list.append([row, col])
                count += 1
                
    return count, access_list

def removePaperRoll(map, access_list):
    for paper in access_list:
        row = paper[0]
        col = paper[1]
        map[row][col] = '.'
    return map

def recursiveCount(map, sum):
    count, access_list = countAccess(map)
    if count == 0:
        return sum
    sum += count
    map = removePaperRoll(map, access_list)
    return recursiveCount(map, sum)
        

grid_map = []

with open("input.txt", "r") as file:
    width = -1
    for line in file:
        width = len(line)
        grid_row = []
        for i in range(len(line)):
            grid_row.append(line[i])
        grid_map.append(grid_row)
    
    last_row = []
    for i in range(width):
        last_row.append(".")
    grid_map.append(last_row)


print(recursiveCount(grid_map, 0))