def path_v2(A, s, t, k):
    if k == 0:
        return s == t
    if k == 1 :
        for i in range(len(A)):
            if A[s][i] == 1:
                if i == t:
                    return True
        return False


    for i in range(len(A)):
        mid = k // 2
        if path_v2(A, s, i, mid) and path_v2(A, i, t, k - mid):
            return True
    return False


A = [[0,1,1,0,0], [1,0,1,0,0], [0,0,0,1,0], [1,0,0,0,0],[0,0,0,0,0]]


print(eval("4+1"))