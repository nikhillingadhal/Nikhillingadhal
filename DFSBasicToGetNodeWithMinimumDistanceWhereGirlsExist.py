# Tasks to be done
# Task 1 : Get N as input and n-1 connections
# Task 2 : Build a matrix
# Task 3 : Establish the connections
# Task 4 : Assign Min variable
# Task 5 : Create a visited array
# Task 6 : DFS and parameters Matrix, Visited, Min
# Task 7 : print the minimum
# Task 6 continued
def DFS(Matrix,visited,Min):
    stack=[]
    stack.append(0)
    visited[0]=1
    top=0
    MinElements=len(Matrix[0])+1
    while(len(stack)!=0):
        for i in range(0,len(Matrix[0])):
            if Matrix[top][i] > 0 and visited[i] !=1:
                stack.append(i)
                if Matrix[top][i] == 2:
                    if MinElements > len(stack) :
                        MinElements = len(stack)
                        Min = i
                break
        top = stack.pop()
        visited[top]=1
    return Min
# Task 6 ended completely
# Task 1
N = int(input())
# Task 1 is done
# Task 2
Matrix=[]
for i in range(N):
    l=[]
    for j in range(N):
        l.append(0)
    Matrix.append(l)
# Task 2 is done
# Task 3
for i in range(N-1):
    startNode , endNode = map(int,input().split())
    Matrix[startNode-1][endNode-1] = 1
    Matrix[endNode-1][startNode-1] = 1
Q=int(input())
for i in range(Q):
    girl = int(input())
    for i in range(N):
        if i != girl - 1:
            Matrix[i][girl - 1] = 2
# Task 3 is done

# Task 4
Min = 0
# Task 4 is done
# Task 5
visited = [0]*N
# Task 5 is done
# Task 6
result = DFS(Matrix,visited,Min)
# Task 6 is done
# Task 7
print(result+1)
# Task 7 is done
