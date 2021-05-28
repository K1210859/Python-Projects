def is_solvable(maze):
    visited = []
    stack = []
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if(maze[i][j]=='S'):
                visited.append((i, j))
                stack.append((i, j))
    goalR = 0
    goalC = 0
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if(maze[i][j]=='G'):
                goalC = j
                goalR = i
    while len(stack)>0:
        temp_node = stack.pop(0)
        if 0 <= temp_node[0]+1 <= len(maze)-1 and visited.__contains__((temp_node[0]+1, temp_node[1]))==False and maze[temp_node[0] + 1][temp_node[1]]!= 'W':
            visited.append((temp_node[0]+1, temp_node[1]))
            stack.insert(0,(temp_node[0]+1, temp_node[1]))
        if 0 <= temp_node[0]-1 <= len(maze)-1 and  visited.__contains__((temp_node[0]-1, temp_node[1]))==False and maze[temp_node[0] - 1][temp_node[1]]!= 'W':
            visited.append((temp_node[0]-1, temp_node[1]))
            stack.insert(0, (temp_node[0]-1, temp_node[1]))
        if 0 <= temp_node[1]+1 <= len(maze[0])-1 and visited.__contains__((temp_node[0], temp_node[1]+1))==False and maze[temp_node[0]][temp_node[1] + 1]!= 'W':
            visited.append((temp_node[0], temp_node[1]+1))
            stack.insert(0, (temp_node[0], temp_node[1]+1))
        if 0 <= temp_node[1]-1 <= len(maze[0])-1 and visited.__contains__((temp_node[0], temp_node[1]-1))==False and maze[temp_node[0]][temp_node[1] - 1]!= 'W':
            visited.append((temp_node[0], temp_node[1]-1))
            stack.insert(0, (temp_node[0], temp_node[1]-1))
        '''if 0 <= temp_node[0]+1 <= len(maze)-1 and visited.__contains__((temp_node[0]+1, temp_node[1]+1))==False and 0 <= temp_node[1]+1 <= len(maze[0])-1 and maze[temp_node[0] + 1][temp_node[1]+1]!= 'W':
            visited.append((temp_node[0]+1, temp_node[1]+1))
            stack.insert(0, (temp_node[0]+1, temp_node[1]+1))
        if 0 <= temp_node[0]-1 <= len(maze)-1 and visited.__contains__((temp_node[0]-1, temp_node[1]-1))==False and 0 <= temp_node[1]-1 <= len(maze[0])-1 and maze[temp_node[0] - 1][temp_node[1]-1]!= 'W':
            visited.append((temp_node[0]-1, temp_node[1]-1))
            stack.insert(0, (temp_node[0]-1, temp_node[1]-1))
        if 0 <= temp_node[0]+1 <= len(maze)-1 and visited.__contains__((temp_node[0]+1, temp_node[1]-1))==False and 0 <= temp_node[1]-1 <= len(maze[0])-1 and maze[temp_node[0] + 1][temp_node[1]-1]!= 'W':
            visited.append((temp_node[0]+1, temp_node[1]-1))
            stack.insert(0, (temp_node[0]+1, temp_node[1]-1))
        if 0 <= temp_node[0]-1 <= len(maze)-1 and visited.__contains__((temp_node[0]-1, temp_node[1]+1))==False and 0 <= temp_node[1]+1 <= len(maze[0])-1 and maze[temp_node[0] - 1][temp_node[1]+1]!= 'W':
            visited.append((temp_node[0]-1, temp_node[1]+1))
            stack.insert(0, (temp_node[0]-1, temp_node[1]+1))'''
    for i in visited:
        if i[0] == goalR and i[1] == goalC:
            return True
    return False

def main():
    print(is_solvable([['S', 'W', '-'],['W', '-', 'W'],['W', 'W', 'G']]))
if __name__ == '__main__':
    main()

