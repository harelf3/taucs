# Skeleton file for HW3 - Spring 2023 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw3_ID.py).

import random  # loads python's random module to use in Q5

##############
# QUESTION 3 #
##############
# Q3_1a
def find_1(lst, s):
    n = len(lst)
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2    # middle rounded down
        if s == lst[mid]:      # item found
            return mid
        if s == lst[mid+1]:
            return mid +1
        if s == lst[mid-1]:
            return mid -1
        elif s < lst[mid]:     # item cannot be in top half
            right = mid-2
        else:                    # item cannot be in bottom half
            left = mid+2           
    return None  


# Q3_1b
def sort_from_almost(lst):
    temp = 0
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            temp =lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
    return None

  


# Q3_2a
def find_2(lst, s, f, g):
    n = len(lst)
    left = 0
    right = n-1
    for func in [f,g]:
        while left <= right:
            mid = (left+right)//2    # middle rounded down
            if s == lst[mid]:      # item found
                return mid
            elif func(s) < func(lst[mid]):     # item cannot be in top half
                right = mid -1
            elif func(s) > func(lst[mid]):     # item cannot be in top half
                left = mid +1
            else:
                break
    return None



# Q3_2b
def find_3(lst, s, functions):
    n =len(lst)
    k = len(functions)
    totallen = 0
    lst2 = [lst[i*(n//k):(i+1)*(n//k)] for i in range (k) ]
    for i in range(len(functions)):
        n = len(lst2[i])
        left = 0
        right = n-1
        func = functions[i]
        while left <= right:
            mid = (left+right)//2    # middle rounded down
            if s == lst2[i][mid]:  
                return mid + totallen
            elif func(s) < func(lst2[i][mid]):     # item cannot be in top half
                right = mid -1
            elif func(s) > func(lst2[i][mid]):     # item cannot be in top half
                left = mid +1
        totallen +=n
    return None



##############
# QUESTION 4 #
##############
# Q4_a
def string_to_int(s):
    returnint = 0
    dicts = {"a":1,"b":2,"c":3,"d":4,"e":5}
    for i in range(len(s)):
        returnint += dicts[s[-i-1]]*(5**(i)) - (5**i)
        
    return returnint
# Q4_b
def int_to_string(k, n):
    s = ""
    dicts = {0:"a",1:"b",2:"c",3:"d",4:"e"}
    for i in range(k-1,-1,-1) :
        s+=dicts[n //(5**i)]
        n-= (n//(5**i))*(5**i)
    return s
        
# Q4_c
def sort_strings1(lst, k):
    RetrunList = []
    helperlist= [0 for i in range(5**k)]
    for z in lst:
        helperlist[string_to_int(z)]+=1
    
    for j in range(len(helperlist)):
        if helperlist[j] !=0:
            for i in range(helperlist[j]):
                RetrunList.append(int_to_string(k,j))
    return RetrunList

    # make a list insert a one into all the places then take it back i make a list of sorted numbers then i find the index of high numbers and add n to it 
    # then i just take all the entries 
# Q4_e
def sort_strings2(lst, k):
    RetrunList = []
    for i in range(5**k):
        for x in lst:
            if string_to_int(x) ==i:
                RetrunList.append(x)
    return RetrunList


##############
# QUESTION 5 #
##############
# Q5_a


def edit_distance(st1, st2):
    if len(st2)==len(st1):
        if st2 ==st1:
            return 0
        difference = 0 
        for i in range(len(st2)) :
            if st2[i] != st1[i]:
                difference +=1
        return difference
            
    st3 =max([st1,st2], key=len)
    st4 =min([st1,st2], key=len)
    return min([edit_distance(st3[:i]+st3[i+1:],st4)+1 for i in range(len(st3))])



# Q5_b
def relevancy_score(text, promote, L):
    min_edit_distance = min(edit_distance(text,i) for i in L)
    promotion_score =1
    if promote:
        promotion_score =2
    return (1/(1+(min_edit_distance)**2))*promotion_score


# Q5_c
def PageRank_search(G, t, p, text, pages_desc, pages_promote):
    import random
    # Initialize parameters
    curr = 0
    n = len(G)
    # Initialize visits vector
    counters = [0 for i in range(n)]
    relevancy_score_list = [relevancy_score(text,pages_promote[i],pages_desc[i]) for i in range(len(pages_desc))]
    # Run the simulation t steps
    for step in range(t):
        # With probability p and if curr is not a sink, select an outgoing link randomly
        if random.random() < p and len(G[curr]) > 0:
            weights = []
            for i in G[curr]:
                weights.append(relevancy_score_list[i])
            
            curr = random.choices(G[curr], weights, k=1)[0]
        # Otherwise, jump to a random page in the web
        else:
            curr = random.choices([z for z in range(len(pages_promote))], relevancy_score_list, k=1)[0]
        counters[curr] += 1
    # Normalize by number of steps to get a probability vector
    return [cnt/t for cnt in counters]

##########
# Tester #
##########
def test():
    # Q3
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    if find_1(almost_sorted_lst, 5) != 3:
        print("error in find_1")
    if find_1(almost_sorted_lst, 50) is not None:
        print("error in find_1")

    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    res = sort_from_almost(almost_sorted_lst)
    if res is not None:
        print("error in sort_from_almost")
    if almost_sorted_lst != sorted(almost_sorted_lst):
        print("error in sort_from_almost")

    f = lambda x: x**2
    g = lambda x: x % 10
    lst1 = [-2, 3, -4, 5, 6, 7, -9]  # sorted according to f
    lst2 = [21, 2, 33, 34, 25, 66, 47]  # sorted according to g
    if find_2(lst1, 7, f, g) != 5 or find_2(lst2, 33, f, g) != 2:
        print("error in find_2")

    lst3 = lst1 + lst2
    functions = [f, g]
    if find_3(lst3, 7, functions) != 5 or find_3(lst3, 33, functions) != 9:
        print("error in find_3")

    # Q4
    if string_to_int("aa") != 0 or string_to_int("aba") != 5:
        print("error in string_to_int")
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea', 'aacc']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")

    # Q5
    if edit_distance("sport", "spotr") != 2 or edit_distance("workout", "wrkout") != 1:
        print("error in edit_distance")

    if relevancy_score("spotr", True, ["sport", "gym", "workout"]) != 0.4:
        print("error in relevancy_score")

