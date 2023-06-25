# Skeleton file for HW4 - Spring 2023 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).
import math, random, time

##############
# Question 1 #
##############

def quicksort(lst, rand=True):
    """ quick sort of lst """
    if len(lst) <= 1:
        return lst
    else:
        pivot = random.choice(lst) if rand else lst[0]
        smaller = [elem for elem in lst if elem < pivot]
        equal = [elem for elem in lst if elem == pivot]
        greater = [elem for elem in lst if elem > pivot]

        return quicksort(smaller, rand) + equal + quicksort(greater, rand)


def quick_comparison_random_input(n, t):
    n_list = [i for i in range(n)] # n complexity 
    rand_lists =[random.sample((n_list), len(n_list)) for i in range(t)] # t complexity times the time it takes to shuffle which is probs n so n*t
    quick_sort_times = []
    rand_quick_sort_times =[]
    for i in range(t):
        t0 = time.perf_counter()
        quicksort(rand_lists[i],False)
        t1 = time.perf_counter()
        quick_sort_times.append(t1-t0)
        t0 = time.perf_counter()
        quicksort(rand_lists[i])
        t1 = time.perf_counter()
        rand_quick_sort_times.append(t1-t0)
    return (sum(rand_quick_sort_times)/t,sum(quick_sort_times)/t)


def quick_comparison_ordered_input(n, t):
    n_list = [i for i in range(n)] # n complexity 
    quick_sort_times = []
    rand_quick_sort_times =[]
    for i in range(t):
        t0 = time.perf_counter()
        quicksort(n_list,False)
        t1 = time.perf_counter()
        quick_sort_times.append(t1-t0)
        t0 = time.perf_counter()
        quicksort(n_list)
        t1 = time.perf_counter()
        rand_quick_sort_times.append(t1-t0)
    return (sum(rand_quick_sort_times)/t,sum(quick_sort_times)/t)


##############
# Question 2 #
##############
#2b
def max_v1_improved(L):
    left = 0
    right = len(L)-1
    return max_v10_engine(L,left,right)
    

def max_v10_engine(L,left,right):
    if right-left <=1:
        return max(L[right],L[left])
    mid =(right+left )//2
    z = max(max_v10_engine(L,left,mid),max_v10_engine(L,mid,right))
    return z



def max_v2_improved(L):
    left = 0
    right =len(L)-1
    return max_v12_engine(L,left,right)

def max_v12_engine(L,left,right):
    if left==right:
        return L[left]
    return max(L[left],max_v12_engine(L,left+1,right))

#2c

def reverse(L):
    start = 0 
    stop = len(L)-1
    return rev(L,start,stop)

def rev(L,start,stop):
    if start >= stop :
        return L
    temp = L[start]
    L[start] = L[stop]
    L[stop] = temp
    return rev(L,start+1,stop-1)
    
    

##############
# Question 3 #
##############
#3b
def is_good_mem(board):
    d = {}
    return is_good_mem_rec(board, d)
    # we use dictionary for memo

def is_good_mem_rec(board, d):
    if sum(board)==0: # empty board, getting here means my opponent has lost
        return True   # so the board is good
    # is this board good ? we check if it is empty is is good 
    m = len(board)
    
    for i in range(m):  # for every column 0<=i<m
        for j in range(board[i]): # for every possible cell (i,j) in column i
            # generate new chomped board check all possible boards 
            chomped_board = board[0:i] + [min(board[k], j) for k in range(i,m)]
            if tuple(chomped_board) in d: # we check if they are in dict  
                if not d[tuple(chomped_board)]:# if thier value is false then this board is good 
                    return True # rerturns true for good board
            else :
                if not is_good_mem_rec(chomped_board,d): # if it is not in dictiory we ask it what is its value now we want it to be false  
                    d[tuple(chomped_board)] = False # it is false indeed so we memo 
                    return True # retun true because the current board is good
                d[tuple(chomped_board)] = True  # we memo just in case 

    return False # current player cannot guarantee win, bad board



##############
# Question 4 #
##############
# 4a
def legal_path(A, vertices):
    for i in range(len(vertices)-1):
        if not A[vertices[i-1]][vertices[i]] ==1:
            return False
    return True




# 4c
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


# 4d # Fix this code without deleting any existing code #
def path_v4(A, s, t):
    L = [False for i in range(len(A))]
    return path_rec(A, s, t, L)

def path_rec(A, s, t, L):
    if s == t:
        return True
    L[s] = True
    for i in range(len(A)):
        if L[i] ==False: 
            if A[s][i] == 1:
                if path_rec(A, i, t, L):
                    return True
    return False

##############
# Question 5 #
##############
# 5a
def can_create_once(s, L):
    if len(L) == 1:
        if s-L[0] == 0 or s+L[0] ==0:
            return True
        else:
            return False 
    
    return can_create_once(s-L[0],L[1:]) or can_create_once(s+L[0],L[1:])
    
# 5b
def can_create_twice(s, L):
    M = {i : False for i in L}
    return can_create_env(s,L*2,M)


def can_create_env(s,L,M):
    if False not in M :
        if L[0] == s:
            return True
    if len(L) == 1:
        if s-L[0] == 0 or s+L[0] ==0:
            return True
        else:
            return False 
    M[L[0]] =True
    return can_create_env(s-L[0],L[1:],M) or can_create_env(s+L[0],L[1:],M)

# 5c
def valid_braces_placement(s, L):
    Valid_places = [("(" if i%4==0 else ")") if i%2==0 else L[i//2] for i in range(len(L)*2+1) ]
    count = 0 
    loopnum =0
    return braces(s,Valid_places,count,loopnum)
    # m="".join(str(i) for i in L)
    # print(eval(m))
    # # if eval(m) == s:
    # #     return True
    # i want to recursively go over all parenthesses 
    
    
def braces(s,L,count,loopnum):
    loopnum +=2
    if loopnum >= len(L):
        return False
    m="".join(str(i) for i in L)
    try:
        if eval(m) ==s:
            return True
    except:
        pass
    L1= L.copy()
    # i know this does nothing after i used try and except but aa the old saying goes "if it aint broke dont fix it"  
    count1 = L.count("(")-L.count(")")
    if L[loopnum] =="(":
        count =count-1
    elif L[loopnum] ==")" :
        count = count+1
    L[loopnum] = ''
    

    return braces(s,L,count,loopnum) or braces(s,L1,count1,loopnum)
    



##########
# Tester #
##########
def test():

    # 2b
    if max_v1_improved([1, 5, 3, 4, -1]) != 5 or max_v1_improved([1]) != 1:
        print("error in max_v1_improved")

    if max_v2_improved([1, 5, 3, 4, -1]) != 5 or max_v2_improved([1]) != 1:
        print("error in max_v2_improved")

    # 2c
    if reverse([1, 5, "hello"]) != ["hello", 5, 1] or reverse([1]) != [1]:
        print("error in reverse")

    # 3b
    if is_good_mem([5, 5, 3]) or not is_good_mem([5, 5, 5]):
        print("error in is_good_mem")

    # 4a
    A = [[0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    if not legal_path(A.copy(), [0, 1, 2, 3]) or \
            not legal_path(A.copy(), [0, 1, 2, 3, 0, 1]) or \
            legal_path(A.copy(), [1, 2, 3, 4]):
        print("error in legal_path")

    # 5a
    if not can_create_once(6, [5, 2, 3]) or not can_create_once(-10, [5, 2, 3]) \
            or can_create_once(9, [5, 2, 3]) or can_create_once(7, [5, 2, 3]):
        print("error in can_create_once")
    # 5b
    if not can_create_twice(6, [5, 2, 3]) or not can_create_twice(9, [5, 2, 3]) \
        or not can_create_twice(7, [5, 2, 3]) or can_create_once(19, [5, 2, 3]):
        print("error in can_create_twice")
    # 5c
    L = [6, '-', 4, '*', 2, '+', 3]
    if not valid_braces_placement(10, L.copy()) or \
            not valid_braces_placement(1, L.copy()) or \
            valid_braces_placement(5, L.copy()):
        print("error in valid_braces_placement")

