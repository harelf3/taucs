# Skeleton file for HW2 - Spring 2023 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw2_ID.py).

import random  # loads python's random module in order to use random.random() in question 2

##############
# QUESTION 1 #
##############
#  Q1a
def divisors(n):
    newlist = [x for x in range(1,n) if n%x==0 ]
    return newlist

#  Q1b
def perfect_numbers(n):
    plist = []
    i = 2 
    while True:
        if i ==sum(divisors(i)):
            plist.append(i) 
            if len(plist) ==n:
                return plist
        i+=1

#  Q1c
def abundant_density(n):
    count = 0
    for i in range(1,n+1):
        if i < sum(divisors(i)):
            count+=1
    return count/n

#  Q1e
def semi_perfect_4(n):
    # so the bst possible runtime is n choose k
    dlist = divisors(n)
    if sum(dlist) == n:
        if len(dlist)==4:
            return True
        else:
            return False
    if sum(dlist)<n:
        return False
    else:
        dlistrem = divisors(n)
        for i1 in dlistrem:
            for i2 in filter(lambda x: x!=i1, dlistrem):
                for i3 in filter(lambda x: x!=i1 and x!=i2, dlistrem):
                    for i4 in filter(lambda x: x!=i1 and x!=i2 and x!=i3, dlistrem):
                        if i1+i2+i3+i4 == n:
                            return True
        return False



##############
# QUESTION 2 #
##############
# Q2a
def coin():
    if random.random() <=0.5:
        return True
    return False

# Q2b
def roll_dice(d):
    return int(random.random()//(1/d))+1

# Q2c
def monty_hall(switch, times):
    won =0 
    for i in range(times):
        doors = {1:"stone",2:"stone",3:"stone"}
        car = roll_dice(3)
        doors[car]="car"
        player = roll_dice(3)
        if switch == False:
            if doors[player]=="car":
                won+=1
        if switch ==True :
            DtoRemove = [1,2,3]
            if car ==player:
                DtoRemove.remove(car)
                player = DtoRemove[roll_dice(2)-1]
                if doors[player]=="car":
                    won +=1
            else :
                DtoRemove.remove(car)
                DtoRemove.remove(player)
                doors.pop(DtoRemove[0])
                doors.pop(player)

                player = list(doors.keys())[0]
                if doors[player]=="car":
                    won +=1
    return won/times
    
# Q2d
def random_sublist(lst, k):
    templist = list(lst.copy())
    sublist = []
    for i in range(k) : 
        z =roll_dice(len(templist))-1
        sublist.append(templist[z])
        templist.remove(templist[z])
    return sublist


##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    for i in range(len(binary)):
        binlst = list(binary[::-1])
        if binlst[i] == "0" :
            binlst[i]="1"
            binlst[:i] = ["0"] * ((i))
            break 
        else :
            if i==len(binary)-1:
                binlst.append("1")
                binlst[:i+1] = ["0"] * ((i+1))
                break
            
    return "".join(binlst)[::-1]

# Q3b
def add(bin1, bin2):
    carry = 0
    binlst = []
    bin1 =bin1[::-1]
    bin2 =bin2[::-1]
    for i in range(max(len(bin1),len(bin2))):
        if i >= (min(len(bin1),len(bin2))):
            maxbin = max([bin1,bin2], key=len)
            if carry == 0:
                binlst.append(str(maxbin[i]))
            if carry ==1 and maxbin[i] =="0":
                binlst.append("1")
                carry =0 
            if carry ==1 and maxbin[i] == "1" :
                binlst.append("0")
                carry = 1
        else : 
            if carry == 0: 
                if bin1[i] == "0" and bin2[i] == "0" :
                    binlst.append("0")
                if bin1[i] != bin2[i]:
                    binlst.append("1")
                if bin1[i] == "1" and bin2[i] == "1":
                    binlst.append("0")
                    carry = 1
            else:
                if bin1[i] == "0" and bin2[i] == "0":
                    binlst.append("1")
                    carry = 0 
                if bin1[i] != bin2[i]:
                    binlst.append("0")
                    carry=1
                if bin1[i] == "1" and bin2[i] == "1":
                    binlst.append("1")
                    carry =1
            
    if carry ==1 :
        binlst.append("1")
    return "".join(binlst[::-1])



# Q3c
def mod_two(binary, power):
    cleanbinary = binary[-power:]
    for i in cleanbinary:
        if i =="0":
            cleanbinary =cleanbinary[1:]
        if len(cleanbinary) ==1:
            return cleanbinary
        else :
            break
    return cleanbinary



# Q3d
def div_two(binary, power):
    if len(binary)<power:
        return "0"
    else: 
        return binary[:len(binary)-power]

# Q3e
def min_bin(lst):
    return min(lst)

##############
# QUESTION 4 #
##############
# Q4a
def lychrel_loops(n):
    word = n
    i=0
    while True:
        word=int(str(word)[::-1])+word
        i+=1
        if str(word) == str(word)[::-1]:
            return i


# Q4b
def is_lychrel_suspect(n, t):
    word = n
    i=0
    while True:
        if i ==t:
            return True
        word=int(str(word)[::-1])+word
        i+=1
        if str(word) == str(word)[::-1]:
            return False

##############
# QUESTION 5 #
##############
# Q5a
def daily_summary(opening_stock, closing_stock):
    daily_earning = 0
    amount_bought= 0
    inventory = []
    for i in range(len(opening_stock)):
        amount_bought += opening_stock[i][1]-closing_stock[i][1]
        daily_earning += opening_stock[i][2]*(opening_stock[i][1]-closing_stock[i][1])
        if closing_stock[i][1] ==0 and opening_stock[i][1]!= 0:
            inventory.append(closing_stock[i][0])

    return (daily_earning,amount_bought,inventory)

# Q5b
def make_transaction(stock, shopping_cart):
    total = 0 
    for cart_item in range(len(shopping_cart)):
        for stock_item in range(len(stock)) : 
            if shopping_cart[cart_item][0] == stock[stock_item][0]:
                total += shopping_cart[cart_item][1]*stock[stock_item][2]
                stock[stock_item][1] = stock[stock_item][1]-shopping_cart[cart_item][1]
    return total


# Q5c
def valid_daily_transactions(opening_stock, closing_stock, transactions):
    for i in transactions:
        make_transaction(opening_stock,i)
    if opening_stock == closing_stock:
        return True
    return False



##########
# Tester #
##########

def test():
    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("Error in Q1a")

    if perfect_numbers(2) != [6, 28]:
        print("Error in Q1b")

    if abundant_density(20) != 0.15:
        print("Error in Q1c")

    if not semi_perfect_4(20) or semi_perfect_4(28):
        print("Error in Q1e")

    for i in range(10):
        if coin() not in {True, False}:
            print("Error in Q2a")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("Error in Q2b")
            break

    for i in range(10):
        if monty_hall(True, 4) not in {0.0, 0.25, 0.5, 0.75, 1.0}:
            print("Error in Q2c")
            break

    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("Error in Q3a")

    if add("0", "1") != "1" or \
            add("1", "1") != "10" or \
            add("110", "11") != "1001" or \
            add("111", "111") != "1110":
        print("Error in Q3b")

    if mod_two("110", 2) != "10" or \
            mod_two("101", 2) != "1" or \
            mod_two("111", 4) != "111":
        print("Error in Q3c")

    if div_two("10", 1) != "1" or \
            div_two("101", 1) != "10" or \
            div_two("1010", 2) != "10" or \
            div_two("101010", 3) != "101":
        print("Error in Q3d")

    if min_bin(["1010", "0", "11"]) != "0":
        print("Error in Q3e")

    if lychrel_loops(28) != 2 or lychrel_loops(110) != 1:
        print("Error in Q4a")

    if (not is_lychrel_suspect(28, 1)) or is_lychrel_suspect(28, 2) or is_lychrel_suspect(28, 3):
        print("Error in Q4b")

    opening_stock = [["tomato", 6, 1.5], ["bread", 10, 5.0], ["milk", 2, 5.5], ["rice", 0, 6.0]]
    closing_stock = [["tomato", 2, 1.5], ["bread", 9, 5.0], ["milk", 0, 5.5], ["rice", 0, 6.0]]
    if daily_summary(opening_stock, closing_stock) != (22.0, 7, ["milk"]):
        print("Error in Q5a")

    stock = [["tomato", 6, 1.5], ["bread", 10, 5.0], ["milk", 2, 5.5], ["rice", 0, 6.0]]
    shopping_cart = [["bread", 2], ["tomato", 6]]
    if make_transaction(stock, shopping_cart) != 19 or \
        stock != [["tomato", 0, 1.5], ["bread", 8, 5.0], ["milk", 2, 5.5], ["rice", 0, 6.0]]:
        print("Error in Q5b")

    opening_stock = [["tomato", 6, 1.5], ["bread", 10, 5.0], ["milk", 2, 5.5], ["rice", 0, 6.0]]
    closing_stock = [["tomato", 0, 1.5], ["bread", 7, 5.0], ["milk", 0, 5.5], ["rice", 0, 6.0]]
    transactions = [[["bread", 2], ["tomato", 6]], [["milk", 1], ["bread", 1]]]
    if valid_daily_transactions(opening_stock, closing_stock, transactions):
        print("Error in Q5c")

    opening_stock = [["tomato", 6, 1.5], ["bread", 10, 5.0], ["milk", 2, 5.5], ["rice", 0, 6.0]]
    closing_stock = [["tomato", 0, 1.5], ["bread", 7, 5.0], ["milk", 0, 5.5], ["rice", 0, 6.0]]
    transactions = [[["bread", 2], ["tomato", 6]], [["milk", 2], ["bread", 1]]]
    if not valid_daily_transactions(opening_stock, closing_stock, transactions):
       print("Error in Q5c")

