"""
def check_stock(inventory, part_id):
    # handle edge -> if len inven is 1?
    left = 0
    right = len(inventory) -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if part_id < inventory[mid]:
            right = mid - 1
            
        elif part_id > inventory[mid]:
            left = mid + 1
        
        else:
            return True
        
    return False


#print(check_stock([], 1))
#print(check_stock([1, 2, 5, 12, 20], 100))

# recursive
def check_stockRecursive(inventory, part_id):
    if not inventory:
        return False
    
    left = 0
    right = len(inventory)-1
    mid = (left + right) // 2
    
    if part_id < inventory[mid]:
        right = mid
        return check_stockRecursive(inventory[:right], part_id)
            
    elif part_id > inventory[mid]:
        left = mid + 1
        return check_stockRecursive(inventory[left:], part_id)    
    else:
        return True

print(check_stockRecursive([1,2,5,12,20], 20))
print(check_stockRecursive([1], 100))

"""


def find_frequency_positions(transmissions, target_code):
    """
    return tuple that has the first index, last index of when target occurs
    
    logn -> BST -> move left/right until lands
    l = 0 , r = n - 1
    """
    l = 0
    r = len(transmissions) - 1
    
    foundS = -1
    foundR = -1
    foundSFlag = False
    foundRFlag = False
    
    while l <= r:
        if transmissions[l] == target_code and not foundSFlag:
            foundS = l
            foundSFlag = True
        if transmissions[r] == target_code:
            foundR = r
            foundRFlag = True
        
        if not foundSFlag:
            l += 1
        if not foundRFlag:
            r -= 1
            
        if foundRFlag and foundSFlag:
            return (foundS, foundR)
        
    return (foundS,foundR)
    

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))



