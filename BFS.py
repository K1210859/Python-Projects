def min_distance(maze):
    queue = []
    visited = []
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if(maze[i][j]=='S'):
                queue.append(((i, j), 0))
                visited.append((i, j))
    goalR = 0
    goalC = 0
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if (maze[i][j] == 'G'):
                goalC = j
                goalR = i
    distance = -1
    while len(queue)>0:
        temp_node = queue.pop(0)
        coords = temp_node[0]
        if coords[0]==goalR and coords[1]==goalC:
            distance = temp_node[1]
            break
        if 0 <= coords[0]+1 <= len(maze)-1 and visited.__contains__((coords[0]+1, coords[1]))==False and maze[coords[0] + 1][coords[1]]!= 'W':
            visited.append((coords[0]+1, coords[1]))
            queue.append(((coords[0]+1, coords[1]),temp_node[1]+1))
        if 0 <= coords[0]-1 <= len(maze)-1 and  visited.__contains__((coords[0]-1, coords[1]))==False and maze[coords[0] - 1][coords[1]]!= 'W':
            visited.append((coords[0]-1, coords[1]))
            queue.append(((coords[0]-1, coords[1]), temp_node[1] + 1))
        if 0 <= coords[1]+1 <= len(maze[0])-1 and visited.__contains__((coords[0], coords[1]+1))==False and maze[coords[0]][coords[1] + 1]!= 'W':
            visited.append((coords[0], coords[1]+1))
            queue.append(((coords[0], coords[1]+1), temp_node[1] + 1))
        if 0 <= coords[1]-1 <= len(maze[0])-1 and visited.__contains__((coords[0], coords[1]-1))==False and maze[coords[0]][coords[1] - 1]!= 'W':
            visited.append((coords[0], coords[1]-1))
            queue.append(((coords[0], coords[1]-1), temp_node[1] + 1))
        '''if 0 <= temp_node[0]+1 <= len(maze)-1 and visited.__contains__((temp_node[0]+1, temp_node[1]+1))==False and 0 <= temp_node[1]+1 <= len(maze[0])-1 and maze[temp_node[0] + 1][temp_node[1]+1]!= 'W':
            visited.append((temp_node[0]+1, temp_node[1]+1))
            queue.offer((temp_node[0]+1, temp_node[1]+1), temp_node[0] + temp_node[1] + 1)
        if 0 <= temp_node[0]-1 <= len(maze)-1 and visited.__contains__((temp_node[0]-1, temp_node[1]-1))==False and 0 <= temp_node[1]-1 <= len(maze[0])-1 and maze[temp_node[0] - 1][temp_node[1]-1]!= 'W':
            visited.append((temp_node[0]-1, temp_node[1]-1))
            queue.offer((temp_node[0]-1, temp_node[1]-1), temp_node[0] + temp_node[1] + 1)
        if 0 <= temp_node[0]+1 <= len(maze)-1 and visited.__contains__((temp_node[0]+1, temp_node[1]-1))==False and 0 <= temp_node[1]-1 <= len(maze[0])-1 and maze[temp_node[0] + 1][temp_node[1]-1]!= 'W':
            visited.append((temp_node[0]+1, temp_node[1]-1))
            queue.offer((temp_node[0]+1, temp_node[1]-1), temp_node[0] + temp_node[1] + 1)
        if 0 <= temp_node[0]-1 <= len(maze)-1 and visited.__contains__((temp_node[0]-1, temp_node[1]+1))==False and 0 <= temp_node[1]+1 <= len(maze[0])-1 and maze[temp_node[0] - 1][temp_node[1]+1]!= 'W':
            visited.append((temp_node[0]-1, temp_node[1]+1))
            queue.offer((temp_node[0]-1, temp_node[1]+1), temp_node[0] + temp_node[1] + 1)'''
    if distance==-1:
        return -1
    else:
        return distance

def main():
    print(min_distance([['-', 'S', 'W'], ['-', '-', 'W'], ['-', 'W', 'G'], ['-', '-', '-']]))
if __name__ == '__main__':
    main()