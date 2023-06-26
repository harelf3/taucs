# Skeleton file for HW5 - Spring 2023 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw5_ID.py).

import random, math, time


################
# Linked List  # (code from lecture)
################

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return str(self.value)


class Linked_list:
    def __init__(self, seq=None):
        self.head = None
        self.size = 0
        if seq != None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.head
        while p != None:
            out += p.__repr__() + ", "
            p = p.next
        return "[" + out[:-2] + "]"  # discard the extra ", " at the end

    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        tmp = self.head 
        self.head = Node(val)
        self.head.next = tmp
        self.size += 1

    def __len__(self):
        ''' called when using Python's len() '''
        return self.size

    def index(self, val):
        ''' find index of (first) node with value val in list
            return None of not found '''
        p = self.head
        i = 0  # we want to return the location
        while p != None:
            if p.value == val:
                return i
            else:
                p = p.next
                i += 1
        return None  # in case val not found

    def __getitem__(self, i):
        ''' called when reading L[i]
            return value of node at index 0<=i<len '''
        assert 0 <= i < len(self)
        p = self.head
        for j in range(0, i):
            p = p.next
        return p.value

    def __setitem__(self, i, val):
        ''' called when using L[i]=val (indexing for writing)
            assigns val to node at index 0<=i<len '''
        assert 0 <= i < len(self)
        p = self.head
        for j in range(0, i):
            p = p.next
        p.value = val
        return None

    def insert(self, i, val):
        ''' add new node with value val before index 0<=i<=len '''
        assert 0 <= i <= len(self)
        if i == 0:
            self.add_at_start(val)  # makes changes to self.head
        else:
            p = self.head
            for j in range(0, i - 1):  # get to position i-1
                p = p.next
            # now add new element
            tmp = p.next
            p.next = Node(val)
            p.next.next = tmp
            self.size += 1

    def append(self, val):
        self.insert(self.size, val)

    def pop(self, i):
        ''' delete element at index 0<=i<len '''
        assert 0 <= i < len(self)
        if i == 0:
            self.head = self.head.next  # bypass first element
        else:  # i >= 1
            p = self.head
            for j in range(0, i - 1):
                p = p.next

            # now p is the element BEFORE index i
            p.next = p.next.next  # bypass element at index i

        self.size -= 1


#######################
# Binary Search Tree  # (code from lecture)
#######################
class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"

def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Binary_search_tree():

    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def lookup(self, key):
        ''' return value of node with key if exists, else None '''

        node = self.root
        while node != None:
            if key == node.key:
                return node.val  # found!
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, key, val):
        ''' insert node with key,val into tree.
            if key already there, just update its value '''

        parent = None  # this will be the parent of the new node
        node = self.root

        while node != None:  # keep descending the tree
            if key == node.key:
                node.val = val  # update the val for this key
                return

            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if parent == None:  # was empty tree, need to update root
            self.root = Tree_node(key, val)
        elif key < parent.key:
            parent.left = Tree_node(key, val)  # "hang" new node as left child

        else:
            parent.right = Tree_node(key, val)  # "hang"    ...     right child

        self.size += 1
        return None

    def minimum(self):
        ''' return value of node with minimal key '''

        if self.root == None:
            return None  # empty tree has no minimum
        node = self.root
        while node.left != None:
            node = node.left
        return node.val

    def depth(self):
        ''' return depth of tree, uses recursion '''

        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)

##############
# QUESTION 1 #
##############
class LLLNode:
    def __init__(self, val):
        self.next_list = []
        self.val = val

    def __repr__(self):
        st = "Value: " + str(self.val) + "\n"
        st += "Neighbors:" + "\n"
        for p in self.next_list:
            st += " - Node with value: " + str(p.val) + "\n"
        return st[:-1]


class LogarithmicLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def add_at_start(self, val):
        node = LLLNode(val)
        if len(self) == 0:
            self.head = node
            self.len = 1
            return None

        temp =self.head # we save current head in a variable so we wont lose it 
        self.head = LLLNode(val) # switch head value 
        self.head.next_list.append(temp)
        for i in range(int(math.floor(math.log2(len(self))))):
            temp=temp.next_list[i]
            self.head.next_list.append(temp)
        # now we just need to get a list of all pointers 
        # self.head = node
        self.len += 1
        return None

    def __getitem__(self, i):
        # we want to do binary search on this log list 
        p = self.head
        if i==0:
            return p
        curr_loc = 0
        for j in range(self.len): # we will actually never use all the n steps but .. 
            if curr_loc ==i: # we check if we are in the right location if yes we return p 
                return p 
            how_far = i-curr_loc # we check how far we Need to acdvance 
            p = p.next_list[math.floor(math.log2(how_far))]
            curr_loc = curr_loc+2**(math.floor(math.log2(how_far)))

                




    # Optional - improve this code!
    def __contains__(self, val):
        p = self.head
        k = 1
        while k != 0:
            if p.val == val:
                return True
            k = 0
            m = len(p.next_list)
            while k < m and p.next_list[k].val <= val:
                k += 1
            if k > 0:
                p = p.next_list[k - 1]
        return False




##############
# QUESTION 2 #
##############
class RationalNumber:
    def __init__(self, p, q):
        """ Represents rational number by its canonical form """
        # Add your code here #
        # we do uclides algo we divide 
        a, b = max(p, q), min(p, q)
        while b > 0:
            a, b = b, a % b
        self.unique_p = int(p/a)
        self.unique_q = int(q/a)

    def __eq__(self, other):
        if self.unique_q == other.unique_q and self.unique_p == other.unique_p:
            return True
        return False

    def is_int(self):
        if self.unique_q ==1 :
            return True
        return False

    def __mul__(self, other):
        p = self.unique_p*other.unique_p
        q = self.unique_q*other.unique_q
        return RationalNumber(p,q)

    def __add__(self, other):
        p = self.unique_p*other.unique_q +self.unique_q*other.unique_p
        q = self.unique_q*other.unique_q
        return RationalNumber(p,q)

    def divides(self, other):
        p=self.unique_p*other.unique_q
        q=self.unique_q*other.unique_p
        return RationalNumber(p,q).is_int()
    

##############
# QUESTION 3 #
##############
def is_sorted(lst):
    """ returns True if lst is sorted, and False otherwise """
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True


def modpower(a, b, c):
    """ computes a**b modulo c, using iterated squaring """
    result = 1
    while b > 0:  # while b is nonzero
        if b % 2 == 1:  # b is odd
            result = (result * a) % c
        a = (a * a) % c
        b = b // 2
    return result


def is_prime(m):
    """ probabilistic test for m's compositeness """''
    for i in range(0, 100):
        a = random.randint(1, m - 1)  # a is a random integer in [1...m-1]
        if modpower(a, m - 1, m) != 1:
            return False
    return True


class FactoredInteger:
    def __init__(self, factors, verify=True):
        """ Represents an integer by its prime factorization """
        if verify:
            assert is_sorted(factors)
        number = 1
        for p in factors:
            if verify:
                assert (is_prime(p))
            number *= p
        self.number = number
        self.factors = factors

    def __repr__(self):
        st ="<"+str(self.number)+":"
        for i in self.factors:
            st =st+str(i)+"*"
        st=st[:-1]
        st=st+">"
        return st
    def __eq__(self, other):
        if self.number==other.number:
            return True
        return False

    def __mul__(self, other):
        lst =[]
        # we need to merge sort this bitch 
        a=0
        b=0
        for i in range(len(self.factors)+len(other.factors)):
            if a<len(self.factors)and b<len(other.factors):
                if self.factors[a]<=other.factors[b]:
                    lst.append(self.factors[a])
                    a+=1
                else:
                    lst.append(other.factors[b])
                    b+=1
            else:
                if a>=len(self.factors):
                    lst.append(other.factors[b])
                    b+=1
                if b>=len(other.factors):
                    lst.append(self.factors[a])
                    a+=1
        return FactoredInteger(lst)

    def __pow__(self, other):
        lst=[]
        for k in self.factors:
            for i in range(other.number):
                lst.append(k)
        return FactoredInteger(lst)

    def gcd(self, other):
        fac_dict = {}
        lst=[]
        for j in [self.factors,other.factors]:
            for i in j:
                if i in fac_dict:
                    fac_dict[i] +=1
                else :
                    fac_dict[i] = 1
        for key in fac_dict:
            for i in range(fac_dict[key]//2):
                lst.append(key)
        return FactoredInteger(lst)
        # game plan we know we need to use factors and find the sublist that both of them have the lists are sorted so it is easier 
    

    def lcm(self, others):
        my_set = set()
        lists = [self.factors] + [x.factors for x in others] #list of all factors 
        f_i_d = [{f: 0 for f in x} for x in lists] # a list og dictionary of all factors 
        for i in range(len(lists)): # iterate over all entries 
            for f in lists[i]:
                my_set.add(f) # we add it to a set 
                f_i_d[i][f] += 1 # we add to the dictionary 
        f_m_d = {x: 0 for x in my_set}
        for f_d in f_i_d: # we itarate over each self other 
            for f in f_d.keys(): # we iterate over all keys 
                if f_d[f] > f_m_d[f]:# we check the largest amount that we have a certian prime in a certian number 
                    f_m_d[f] = f_d[f]
        result = []
        for k, v in f_m_d.items():
            result += [k] * v
        return FactoredInteger(result, verify=False)
    

##############
# QUESTION 4 #
##############

def build_balanced(n):
    t = Binary_search_tree()
    t.root = Tree_node(2**(n-1),True)
    if n==1:
        return t
    
    l = t.root.left = Tree_node(2**(n-1)-2**(n-2),True)
    r = t.root.right = Tree_node(2**(n-1)+2**(n-2),True)
    n=n-1
    bb_env(n-1,t,l) ,bb_env(n-1,t,r)
    return t

def bb_env(n,t,node):
    if n ==0:
        return
    
    l =node.left = Tree_node(node.key-2**(n-1),True)
    r =node.right = Tree_node(node.key+2**(n-1),True)
    
    
    return bb_env(n-1,t,l),bb_env(n-1,t,r)
        




# The following signature allows us to add more methods to the previously declared Binary_search_tree class
class Binary_search_tree(Binary_search_tree):
    def first_connecting_node(self, n1, n2):
        lst1=[]
        lst2=[]
        node = self.root
        print(self)
        for l in [(n1,lst1),(n2,lst2)]:
            node = self.root
            l[1].append(node.key)
            while node != None:
                if l[0] == node.key:
                    break  # found!
                elif l[0] < node.key:
                    node = node.left
                    l[1].append(node.key)
                else:
                    node = node.right
                    l[1].append(node.key)
        for i in lst1[::-1]:
            if i in lst2 :
                return i
class Binary_search_tree(Binary_search_tree):
    def first_connecting_node(self, n1, n2):
        root =self.root
        return first_node(root,n1,n2)
            

def first_node(root,n1,n2):
    if root.key < n1 and root.key < n2 :
        node =root.right
        return first_node(node,n1,n2)
    if root.key > n1 and root.key > n2 : 
        node = root.left 
        return first_node(node,n1,n2)
    else : 
        return root 

class Binary_search_tree(Binary_search_tree):
    def first_connecting_node(self, n1, n2):        
        pass
    def env_first(t,n1,n2):
        if t.val <n1.val and n2.val:
            t.env_first(t.right)

##############
# QUESTION 5 #
##############
def prefix_suffix_overlap(lst, k):
    ret_list = []
    for ls in range(len(lst)) : # i get all the lists 
        for i in range(len(lst)):
            if i==ls:
                continue
            if lst[ls][:k] == lst[i][-k:]:
                ret_list.append((ls,i))
    return ret_list



class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        lst=[]
        Dict_key = self.hash_mod(key)
        for i in self.table[Dict_key] :
            if i[0] == key:
                lst.append(i)
        return lst


def prefix_suffix_overlap_hash1(lst, k):
    lstr=[]
    d1=Dict(len(lst))
    for i in range(len(lst)) :
        d1.insert(lst[i][:k],i)
    print(d1)
    for i in range(len(lst)):
        z=d1.find(lst[i][-k:])
        print(z)
        if len(z)!=0:
            for j in range(len(z)):
                if i == z[j][1]:
                    continue 
                lstr.append((i,z[j][1]))
    return lstr
d = Dict(3)
d.insert("a", 56)
d.insert("a", 34)
if sorted(d.find("a")) != sorted([56, 34]) or d.find("b") != []:
    print("5 - error in Dict.find")

lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
k = 2
if sorted(prefix_suffix_overlap_hash1(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
    print("5 - error in prefix_suffix_overlap_hash1")
##############
# QUESTION 6 #
##############
def cycle_length(L):
    pass  # replace this with your code

##############
# QUESTION 7 #
##############

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.sqrt(x ** 2 + y ** 2)
        self.theta = math.atan2(y, x)
        if self.theta < 0:
            self.theta += 2*math.pi

    # 7a
    def angle_between_points(self, other):
        pass  # replace this with your code

# 7b
def find_optimal_angle(trees, alpha):
    pass  # replace this with your code



def test():
    # Q1
    lst = LogarithmicLinkedList()
    lst.add_at_start(1)
    lst.add_at_start("hello")
    lst.add_at_start(True)
    if lst[0] != True or len(lst) != 3:
        print("1 - error in LogarithmicLinkedList")

    # Q2
    num1 = RationalNumber(10, 4)
    if num1.unique_p != 5 or num1.unique_q != 2:
        print("2 - error in RationalNumber's __init__")

    num2 = RationalNumber(20, 8)
    if num1 != num2:
        print("2 - error in RationalNumber's __eq__")

    num2 = RationalNumber(6, 3)
    if not num2.is_int:
        print("2 - error in RationalNumber's is_int")

    num2 = RationalNumber(12, 8)
    res = num1 * num2
    if res.unique_p != 15 or res.unique_q != 4:
        print("2 - error in RationalNumber's __mul__")

    res = num1 + num2
    if res.unique_p != 4 or res.unique_q != 1:
        print("2 - error in RationalNumber's __add__")

    num2 = RationalNumber(5, 1)
    if not num1.divides(num2):
        print("2 - error in RationalNumber's divides")

    # Q3
    n1 = FactoredInteger([2, 3])  # n1.number = 6
    n2 = FactoredInteger([2, 5])  # n2.number = 10
    n3 = FactoredInteger([2, 2, 3, 5])  # n3.number = 60
    if str(n3) != "<60:2*2*3*5>":
        print("3 - error in FactoredInteger.__repr__")
    if n1 != FactoredInteger([2, 3]):
        print("3 - error in FactoredInteger.__eq__")
    if n1 * n2 != n3:
        print("3 - error in FactoredInteger.__mult__")
    if n1 ** n2 != FactoredInteger([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]):
        print("3 - error in FactoredInteger.__pow__")

    n4 = FactoredInteger([2, 2, 3])  # n4.number = 12
    n5 = FactoredInteger([2, 2, 2])  # n5.number = 8
    n6 = FactoredInteger([2, 2])  # n6.number = 4
    if n4.gcd(n5) != n6:
        print("3 - error in gcd")

    n7 = FactoredInteger([2, 3])  # n7.number = 6
    n8 = FactoredInteger([5, 7])  # n8.number = 35
    n9 = FactoredInteger([])  # represents 1
    if n7.gcd(n8) != n9:
        print("3 - error in gcd")

    # Q4
    T = build_balanced(3)
    if T.size != 7 or T.depth() != 2:
        print("4 - error in build_balanced")
    if T.first_connecting_node(T.root, T.root.left) is not T.root:
        print("4 - error in first_connecting_node")

    # Q5
    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("5 - error in prefix_suffix_overlap")

    d = Dict(3)
    d.insert("a", 56)
    d.insert("a", 34)
    if sorted(d.find("a")) != sorted([56, 34]) or d.find("b") != []:
        print("5 - error in Dict.find")

    lst = ["abcd", "cdab", "aaaa", "bbbb", "abff"]
    k = 2
    if sorted(prefix_suffix_overlap_hash1(lst, k)) != sorted([(0, 1), (1, 0), (4, 1)]):
        print("5 - error in prefix_suffix_overlap_hash1")

    # Q6
    lst = Linked_list(seq=[0, 1, 2, 3, 4])
    lst.head.next.next.next.next.next = lst.head.next
    if cycle_length(lst) != 4:
        print("6 - error in cycle_length")

    # Q7
    p1 = Point(1, 1)  # theta = pi / 4
    p2 = Point(0, 3)  # theta = pi / 2
    if Point.angle_between_points(p1, p2) != 0.25 * math.pi or \
            Point.angle_between_points(p2, p1) != 1.75 * math.pi:
        print("7 - error in angle_between_points")

    trees = [Point(2, 1), Point(0, 3), Point(-1, 3), Point(-1, 1), Point(-1, -1), Point(0, -5)]
    if find_optimal_angle(trees, 0.25 * math.pi) != 0.5 * math.pi:
        print("7 - error in find_optimal_angle")
