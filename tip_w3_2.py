"""
# O(n) for space + time prob #1
"""
from collections import deque

def count_unique_characters(script):
    myset = set()
    for stuff in script:
        myset.add(stuff)

    return len(myset)


script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys)) 

# problem 2 find most frequent keywords
def find_most_frequent_keywords(scenes):
    """
    the keyword(S) that appear the mosts frequently
    freq map word: freq 
    go through scenes
    
    go through freq map 
    O(n)
    """
    
    freq = {}
    
    for y in scenes.values():
        for stuff in y:
            freq[stuff] = freq.get(stuff, 0) + 1
        
    currMax = 0
    finalRes = []
    for x, y in freq.items():
        if y > currMax:
            currMax = y
            finalRes.clear()
            finalRes.append(x)
        elif y == currMax:
            finalRes.append(x)
    
    return finalRes


scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}

print(find_most_frequent_keywords(scenes)) 

from collections import deque
def manage_food_waste_with_queue(waste_records):
    """
    assume input are sorted by date correctly
    loop through list and ensure strictly decreasing
    """
    
    val = waste_records[0][1]
    waste_records = waste_records[1:]
    while waste_records:
        if val <= waste_records[0][1]:
            return False
        val = waste_records[0][1]
        waste_records = waste_records[1:]
    return True


waste_records_1 = [
    ("2024-08-01", 150),
    ("2024-08-02", 120),
    ("2024-08-03", 100),
    ("2024-08-04", 80),
    ("2024-08-05", 60)
]

waste_records_2 = [
    ("2024-08-01", 150),
    ("2024-08-02", 180),
    ("2024-08-03", 160),
    ("2024-08-04", 140),
    ("2024-08-05", 120)
]

print(manage_food_waste_with_queue(waste_records_1)) 
print(manage_food_waste_with_queue(waste_records_2))

def greater_than(lst1, lst2):
    if int(lst1[0]) > int(lst2[0]):
        return True
    elif int(lst1[1]) > int(lst2[1]):
        return True
    elif int(lst1[2]) > int(lst2[2]):
        return True
    return False

def check_expiration_order(expiration_dates):
    time = expiration_dates[0][1].split('-')
    expiration_dates = expiration_dates[1:]
    while expiration_dates:
        currTime = expiration_dates[0][1].split('-')
        if greater_than(time, currTime):
            return False
        time = expiration_dates[0][1].split('-')
        expiration_dates = expiration_dates[1:]
    return True

expiration_dates_1 = [
    ("Milk", "2024-08-05"),
    ("Bread", "2024-08-10"),
    ("Eggs", "2024-08-12"),
    ("Cheese", "2024-08-15")
]

expiration_dates_2 = [
    ("Cheese", "2024-08-15"),
    ("Bread", "2024-08-12"),
    ("Eggs", "2024-08-10"),
    ("Milk", "2024-08-05")
]

print(check_expiration_order(expiration_dates_1)) 
print(check_expiration_order(expiration_dates_2)) 