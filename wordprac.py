stringToSplit = "Hello, All! My name is Nikka. My name is from my parents."

# split the given string and count wor dfreq
from collections import Counter
def splitIt(str):
    words = str.split()
    cleaned = []
    for word in words:
        word = "".join(char for char in word if char.isalnum()).lower()
        cleaned.append(word)
    
    count = Counter(cleaned)
    print(count)
    
   
    
splitIt(stringToSplit)

