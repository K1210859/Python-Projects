def trip_distance(map):
    queue = []
    visited = []
    for i in range(0,len(map)):
        for j in range(0,len(map[0])):
            if(map[i][j]=='S'):
                queue.append(((i, j), 0))
                visited.append((i, j))
    goalR = 0
    goalC = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if (map[i][j] == 'D'):
                goalC = j
                goalR = i
    distance = -1
    while len(queue)>0:
        temp_node = queue.pop(0)
        coords = temp_node[0]
        oCondition = False
        if coords[0]==goalR and coords[1]==goalC:
            distance = temp_node[1]
            break
        if 0 <= coords[1]+1 <= len(map[0])-1 and visited.__contains__((coords[0], coords[1]+1))==False and map[coords[0]][coords[1] + 1]!= 'M':
            visited.append((coords[0], coords[1]+1))
            if map[coords[0]][coords[1]+1]!='O':
                queue.append(((coords[0], coords[1]+1), temp_node[1] + 1))
            else:
                queue.append(((coords[0], coords[1]+1), temp_node[1] + 2))
        if 0 <= coords[1]-1 <= len(map[0])-1 and visited.__contains__((coords[0], coords[1]-1))==False and map[coords[0]][coords[1] - 1]!= 'M':
            visited.append((coords[0], coords[1]-1))
            if map[coords[0]][coords[1]-1]!='O':
                queue.append(((coords[0], coords[1]-1), temp_node[1] + 1))
            else:
                queue.append(((coords[0], coords[1]-1), temp_node[1] + 2))
        if 0 <= coords[0]+1 <= len(map)-1 and visited.__contains__((coords[0]+1, coords[1]))==False and map[coords[0] + 1][coords[1]]!= 'M':
            visited.append((coords[0]+1, coords[1]))
            if map[coords[0]+1][coords[1]]!='O':
                queue.append(((coords[0] + 1, coords[1]), temp_node[1] + 1))
            else:
                queue.append(((coords[0]+1, coords[1]),temp_node[1]+2))
        if 0 <= coords[0]-1 <= len(map)-1 and  visited.__contains__((coords[0]-1, coords[1]))==False and map[coords[0] - 1][coords[1]]!= 'M':
            visited.append((coords[0]-1, coords[1]))
            if map[coords[0]-1][coords[1]]!='O':
                queue.append(((coords[0]-1, coords[1]), temp_node[1] + 1))
            else:
                queue.append(((coords[0]-1, coords[1]), temp_node[1] + 2))
    if distance==-1:
        return -1
    else:
        return distance

def main():
    print(trip_distance([['O', 'M', 'D', 'M'], ['O', 'O', '-', 'M'], ['-', '-', '-', 'O'], ['O', 'S', '-', 'O']]))
if __name__ == '__main__':
    main()