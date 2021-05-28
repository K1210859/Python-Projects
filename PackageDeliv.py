import copy
def shortest(connections, must_visit):
    queue = []
    visited = []
    startingConnection = 'A'
    lessCondition = False
    if len(must_visit)==2:
        queue.append([startingConnection,False,False,0])
        lessCondition=True
    if len(must_visit)==3:
        queue.append([startingConnection,False,False,False,0])
    visited.append(startingConnection)
    distance = 1000000
    #count=0
    for count in range(0,10000):
        temp_node = queue.pop(0)
        if lessCondition:
            if temp_node[0]==must_visit[0]:
                temp_node[1] = True
            if temp_node[0]==must_visit[1]:
                temp_node[2] = True
        else:
            if temp_node[0]==must_visit[0]:
                temp_node[1] = True
            if temp_node[0]==must_visit[1]:
                temp_node[2] = True
            if temp_node[0] == must_visit[2]:
                temp_node[3] = True
        if lessCondition:
            #print(str(temp_node[1])+", "+str(temp_node[2]))
            if temp_node[1]==True and temp_node[2]==True and temp_node[3]<distance:
                #print('hello')
                distance = temp_node[3]
        else:
            if temp_node[1]==True and temp_node[2]==True and temp_node[3]==True and temp_node[4]<distance:
                #print('hello')
                distance = temp_node[4]
        for x in connections:
            if x[0]==temp_node[0]:
                visited.append(x[1])
                if lessCondition:
                    queue.append([x[1],temp_node[1],temp_node[2],temp_node[3]+x[2]])
                else:
                    queue.append([x[1], temp_node[1], temp_node[2], temp_node[3], temp_node[4] + x[2]])
            if x[1]==temp_node[0]:
                visited.append(x[0])
                if lessCondition:
                    queue.append([x[0], temp_node[1],temp_node[2], temp_node[3] + x[2]])
                else:
                    queue.append([x[0], temp_node[1], temp_node[2], temp_node[3], temp_node[4] + x[2]])
        #count+=1
    return distance

def main():
    assert 19 == shortest(
        [('A', 'D', 3), ('A', 'F', 6), ('F', 'G', 2), ('F', 'B', 4), ('F', 'E', 18), ('G', 'B', 1), ('D', 'E', 2),
         ('E', 'H', 7)], ['B', 'E']), \
        "Test 1 failed to produce the correct answer"
    assert 12 == shortest(
        [('A', 'D', 3), ('A', 'F', 6), ('F', 'G', 2), ('F', 'B', 4), ('F', 'E', 18), ('G', 'B', 1), ('D', 'E', 2),
         ('E', 'H', 7)], ['D', 'H']), \
        "Test 2 failed to produce the correct answer"
    assert 7 == shortest(
        [('A', 'G', 1), ('A', 'B', 2), ('A', 'C', 3), ('A', 'D', 4), ('A', 'E', 5), ('A', 'F', 6), ('B', 'C', 7),
         ('D', 'C', 6), ('F', 'E', 2)], ['F', 'E']), "Test 3 failed to produce the correct answer"
    assert 9 == shortest(
        [('A', 'G', 1), ('A', 'B', 2), ('A', 'C', 3), ('A', 'D', 4), ('A', 'E', 5), ('A', 'F', 6), ('B', 'C', 7),
         ('D', 'C', 6), ('F', 'E', 2)], ['G', 'B', 'C']), "Test 4 failed to produce the correct answer"
    print("Success")
if __name__ == '__main__':
    main()
