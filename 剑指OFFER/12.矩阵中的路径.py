#题目：设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有按顺序字符的路径。
#路径可以从矩阵的任意一格开始，每一步可以在矩阵中向上下左右移动一格。
#如果一条路径经过了矩阵中的某一格，那么不能再进入该格子。

#回溯法
def getPath(A,s):
    i=0
    m=len(A)
    n=len(A[0])
    visited=[]
    pathlength=0
    for x in range(m):
        tmp=[]
        for y in range(n):
            tmp.append(0)
        visited.append(tmp)
    while i<m:
        j=0
        while j<n:
            if havePath(A,visited,i,j,s,pathlength):
                return True
            visited[i][j]=1
            j+=1
        i+=1
    return False


def havePath(A,visited,i,j,s,pathlength):
    if pathlength==len(s):
        return True
    if i>=0 and i<len(A) and j>=0 and j<len(A[0]) and \
            A[i][j]==s[pathlength] and visited[i][j]==0:
        pathlength+=1
        visited[i][j]=1
        return havePath(A,visited,i-1,j,s,pathlength) or\
                havePath(A, visited, i + 1, j, s, pathlength) or\
                havePath(A, visited, i, j-1, s, pathlength) or \
                havePath(A, visited, i, j+1, s, pathlength)



A=[["a","b","t","g"],
   ["c","f","c","s"],
   ["j","d","e","h"],]
s1="bfcehsgt"
s2="abfb"
print(getPath(A,s1))
print(getPath(A,s2))

