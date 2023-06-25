def binary_search(lst, key):
    """ lst better be sorted for binary search to work """
    n = len(lst)
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2    # middle rounded down
        if key == lst[mid]:      # item found
            return mid
        elif key < lst[mid]:     # item cannot be in top half
            right = mid
        else:                    # item cannot be in bottom half
            left = mid     
        print(mid)    
        print(right)
        print(left)

    #print(key, "not found")
    return None  

lst =[1,2,3,4,5,6,7,8,9,10]
print(binary_search(lst,10))