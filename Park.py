def can_trail(park):
    visited = []
    stack = []
    for i in range(0,len(park)):
        for j in range(0,len(park[0])):
            if(park[i][j]=='S'):
                visited.append((i, j))
                stack.append((i, j))
    goalR = 0
    goalC = 0
    for i in range(0,len(park)):
        for j in range(0,len(park[0])):
            if(park[i][j]=='G'):
                goalC = j
                goalR = i
    while len(stack)>0:
        temp_node = stack.pop(0)
        if park[temp_node[0]][temp_node[1]]=='W':
            if 0 <= temp_node[0]+1 <= len(park)-1 and visited.__contains__((temp_node[0]+1, temp_node[1]))==False and park[temp_node[0] + 1][temp_node[1]]!= 'T' and park[temp_node[0] + 1][temp_node[1]]!= 'W':
                visited.append((temp_node[0]+1, temp_node[1]))
                stack.insert(0,(temp_node[0]+1, temp_node[1]))
            if 0 <= temp_node[0]-1 <= len(park)-1 and  visited.__contains__((temp_node[0]-1, temp_node[1]))==False and park[temp_node[0] - 1][temp_node[1]]!= 'T' and park[temp_node[0] - 1][temp_node[1]]!= 'W':
                visited.append((temp_node[0]-1, temp_node[1]))
                stack.insert(0, (temp_node[0]-1, temp_node[1]))
            if 0 <= temp_node[1]+1 <= len(park[0])-1 and visited.__contains__((temp_node[0], temp_node[1]+1))==False and park[temp_node[0]][temp_node[1] + 1]!= 'T' and park[temp_node[0]][temp_node[1] + 1]!= 'W':
                visited.append((temp_node[0], temp_node[1]+1))
                stack.insert(0, (temp_node[0], temp_node[1]+1))
            if 0 <= temp_node[1]-1 <= len(park[0])-1 and visited.__contains__((temp_node[0], temp_node[1]-1))==False and park[temp_node[0]][temp_node[1] - 1]!= 'T' and park[temp_node[0]][temp_node[1] - 1]!= 'W':
                visited.append((temp_node[0], temp_node[1]-1))
                stack.insert(0, (temp_node[0], temp_node[1]-1))
        else:
            if 0 <= temp_node[0]+1 <= len(park)-1 and visited.__contains__((temp_node[0]+1, temp_node[1]))==False and park[temp_node[0] + 1][temp_node[1]]!= 'T':
                visited.append((temp_node[0]+1, temp_node[1]))
                stack.insert(0,(temp_node[0]+1, temp_node[1]))
            if 0 <= temp_node[0]-1 <= len(park)-1 and  visited.__contains__((temp_node[0]-1, temp_node[1]))==False and park[temp_node[0] - 1][temp_node[1]]!= 'T':
                visited.append((temp_node[0]-1, temp_node[1]))
                stack.insert(0, (temp_node[0]-1, temp_node[1]))
            if 0 <= temp_node[1]+1 <= len(park[0])-1 and visited.__contains__((temp_node[0], temp_node[1]+1))==False and park[temp_node[0]][temp_node[1] + 1]!= 'T':
                visited.append((temp_node[0], temp_node[1]+1))
                stack.insert(0, (temp_node[0], temp_node[1]+1))
            if 0 <= temp_node[1]-1 <= len(park[0])-1 and visited.__contains__((temp_node[0], temp_node[1]-1))==False and park[temp_node[0]][temp_node[1] - 1]!= 'T':
                visited.append((temp_node[0], temp_node[1]-1))
                stack.insert(0, (temp_node[0], temp_node[1]-1))
    for i in visited:
        if i[0] == goalR and i[1] == goalC:
            return True
    return False

def main():
    print(can_trail([['S', '-', '-', 'T', 'T', 'T', '-'],['-', 'T', '-', '-', 'W', 'W', 'G']]))
if __name__ == '__main__':
    main()

