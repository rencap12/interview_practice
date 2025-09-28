# Problem 1 - Extra Treats
# At the pet adoption center, there are two groups of volunteers:

# 'C' — Cat Lovers
# 'D' — Dog Lovers
# Each week, these groups vote to decide which type of pet should receive extra treats. The voting happens in rounds, following these rules:

# Ban a Vote: In each round, a volunteer can ban one volunteer from the opposite group. A banned volunteer loses all voting rights for the rest of the process.
# Declare Victory: If at any point all remaining volunteers are from the same group, that group can declare victory, and their preferred pet will receive the extra treats.
# You are given a string votes representing the group affiliation of each volunteer. The character at index i is either 'C' (Cat Lovers) or 'D' (Dog Lovers).

# Assuming each volunteer acts in order (from left to right) and the process repeats until one group wins, predict which group will eventually declare victory.

# Return:

# "Cat Lovers" if the Cat Lovers will win.
# "Dog Lovers" if the Dog Lovers will win.


# Understand
# 
"""
"CD"
Cque = (before adding C to Cque, check if Dque pop from Dque)
Dque = (before adding D to Dque, check if Cque pop from Cque) 
At the end, check which queue is empty -> opposite wins (if cat empty -> dog | if dog empty-> cat)

-> edge case? empty str, all c's or all d's, can both win?
"""

from collections import deque
def predictAdoption_victory(votes: str) -> str:
    # queueC = deque()
    # queueD = deque()
    
    # for x in votes:
    #     if x == "C":
    #         queueC.appendleft(x)
    #     else:
    #         queueD.appendleft(x)
    
    """ account for which comes irst
    for y in votes:
        if y == "C" and queueD:
            queueD.popleft()
        elif y == "D" and queueC:
            queueC.popleft()
            
    if queueC:
        return "Cat Lovers"
    if queueD:
        return "Dog Lovers"
    """
    
    existC = 0
    existD = 0
    
    queue = deque()
    
    for x in votes:
        #  + 1 if pop
        if queue:
            if x == "C":
                if queue[0] == "D":
                    existC -= 1
                    queue.popleft()
                    existD += 1
            elif x == "D":
                if queue[0] == "C":
                    existD -= 1
                    queue.popleft()
                    existC += 1
        else:
             queue.append(x)
    return "Cat Lovers Win" if existC > existD else "Dog Lovers win"
            

print(predictAdoption_victory("CD"))  # Cat Lovers -> this works
print(predictAdoption_victory("CDD"))  # Dog Lovers -> WIP

# Goodjob , guys! It was a great attempt, regardless!
# first approach with two queues was actually correct Thanks! see you next class

def predictAdoption_victory3(votes: str) -> str:
    queueC = deque()
    queueD = deque()
    seenIndices = set() # they are banned
    
    for x in range(len(votes)):
        if votes[x] == "C":
            queueC.appendleft(("C", x))
        else:
            queueD.appendleft(("D", x))
            
    for y in range(len(votes)):
        if votes[y] == "C" and queueD and y not in seenIndices:
            char, ind = queueD.popleft()
            seenIndices.add(ind)
        elif votes[y] == "D" and queueC and y not in seenIndices:
            car, ind = queueC.popleft()
            seenIndices.add(ind)
            
    if queueC:
        return "Cat Lovers"
    if queueD:
        return "Dog Lovers"


print('---------')
print(predictAdoption_victory3("CD"))  # Cat Lovers - good!
print(predictAdoption_victory3("CDD")) # Dog Lovers - good!
print(predictAdoption_victory3("CCDD")) # Cat Lovers - good!
print(predictAdoption_victory3("CCCDD")) # Cat Lovers - good!
print(predictAdoption_victory3("CCDDD")) # Cat Lovers - good!

