#Skeleton file for HW1 - Spring 2023 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.
#you can add new functions if needed.

#Change the name of the file to include your ID number (hw1_ID.py).

# Question 4a
def intersect(st1, st2):
    if st1=="" or st2 =="":
        return ""
    interset = set()
    for i in st1:
        if i in st2:
            interset.add(i)
    return "".join(interset)

            


# Question 4b
def intersect_lst(lst):
    interlist = lst[0]

    for i in range(len(lst)-1):
        interval = intersect(interlist,lst[i+1])
        interlist = interval
    return interlist


# Question 4c
def least_pal(text):
    lentxt = len(text)
    k=0
    for i in range(lentxt//2):
        if text[i]!=text[(lentxt-i-1)]:
            k +=1
    return k 

# Question 4d
def most_frequent(text):
    thedicc = {}
    for i in text:
        thedicc[i]=0
    for i in text:
        thedicc[i]+=1
    max_value = max(thedicc, key=thedicc.get)
    return max_value



# Question 4e
def rev_words(text):
    lst = text.split()
    word = ""
    for i in lst:
        word = word +str(i[::-1])+' '
    return str(word[:-1])


# Question 4f
def is_int(text):
    tlen = len(text)
    if tlen >=2 and text[0]=="0":
        return False
    if text[:2] == "-0":
        return False
    number_list =["0","1","2","3","4","5","6","7","8","9"]
    for i in text : 
        if i not in number_list:
            if i == "-"and text.index('-')==0:
                continue
            else : 
                return False
    return True
    

#Question 4g
def merge(text1, text2):
    pass
    
#Question 5
def calc(expression):
    lst = expression.split("'")
    if lst[0] =='':
        lst.remove(lst[0])
    if lst[-1]=='':
        lst.remove(lst[-1])
    word=str([lst[0]][0])
    for i in range(len(lst)):
        if lst[i] =="+":
            word =word + str(lst[i+1])
        if lst[i] =="*":
            word =word*int(lst[i+1])
        if lst[i] =="!":
            word =word[::-1]
            if int(i+1)==int(len(lst)):
                continue
            else:
                word =word+lst[i+1]
    return str(word)



# Question 6a
def eval_mon(monomial, val):
    monlst = monomial.split("x^")
    monsum = int(monlst[0])*int(val)**int(monlst[1])
    return monsum


# Question 6b
def eval_pol(polynomial, val):
    polist =[]
    poly = ""
    for i in range(len(polynomial)):
        if polynomial[i] =="+"or polynomial[i]=="-":
            if i ==0: 
                poly = poly+polynomial[i]
            else:
                polist.append(poly)
                poly =""
                poly = poly+polynomial[i]
        
        else :
            poly = poly+polynomial[i]
            if i == (len(polynomial)-1):
                polist.append(poly)
    sumslst =[]
    for i in polist:
        sumslst.append(eval_mon(i,val))
    polysum =sum(sumslst)
    return polysum

########
# Tester
########

def test():
    #testing Q4
    if "".join(sorted(intersect("aabcccdde", "bccaxyz"))) != "abc":
        print("error in intersect - 1")
    if intersect("xyz", "abc") != "":
        print("error in intersect - 2")

    if "".join(sorted(intersect_lst(["aabbcccdd", "bbcpold", "dcbxyz"]))) != "bcd":
        print("error in intersect_lst - 1")
    if "".join(sorted(intersect_lst(["xyz1", "1zyx", "11xxyyzz", "xy1"]))) != "1xy":
        print("error in intersect_lst - 2")
    
    if least_pal("abcdefgh") != 4:
        print("error in least_pal - 1")
    if least_pal("radarr") != 2:
        print("error in least_pal - 2")

    if most_frequent("abcdee") != "e":
        print("error in most_frequent - 1")
    if most_frequent("x11x22x33x") != "x":
        print("error in most_frequent - 2")

    if rev_words("hello world its a beautiful day") != "olleh dlrow sti a lufituaeb yad":
        print("error in rev_words - 1")
    if rev_words("hello") != "olleh":
        print("error in rev_words - 2")

    if is_int("12x"):
        print("error in is_int - 1")
    if is_int("-0"):
        print("error in is_int - 2")
    if not is_int("42"):
        print("error in is_int - 3")
        
    if merge("abcd", "") != "abcd":
        print("error in merge - 1")
    if merge("aabbddfgk", "adkox") != "aaabbdddfgkkox":
        print("error in merge - 2")

    #testing Q5
    if calc("'123321'*'2'") != "123321123321":
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
        print("error in calc - 2")
    if calc("'hi+fi'*'2'*'2'") != "hi+fihi+fihi+fihi+fi":
        print("error in calc - 3")
    if calc("'a'*'2'+'b'*'2'") != "aabaab":
        print("error in calc - 4")
    if calc("'a'+'b'*'2'+'c'!'b'") != "cbabab":
        print("error in calc - 5")
    if calc("'abc'+'d'*'2'!") != "dcbadcba":
        print("error in calc - 6")

    #testing Q6
    if eval_mon("+5x^3", 4) != 320:
        print("error in eval_mon - 1")
    if eval_mon("-5x^0", 1000) != -5:
        print("error in eval_mon - 2")
    if eval_mon("+1x^10", 2) != 1024:
        print("error in eval_mon - 3")

    if eval_pol("+5x^3-4x^2+7x^1-5x^0", 4) != 279:
        print("error in eval_pol - 1")
    if eval_pol("+1x^0+1x^1+1x^2+1x^3+1x^4+1x^5", 5) != 3906:
        print("error in eval_pol - 2")
    if eval_pol("+1x^0+1x^1+1x^2+1x^3+1x^4+1x^5", 2) != 63:
        print("error in eval_pol - 3")

