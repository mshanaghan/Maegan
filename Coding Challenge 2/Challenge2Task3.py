# Count the occurrence of each word and print the word plus the count
string = 'hi dee hi how are you mr dee'

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count(string))

# Success, w3resource.com supplied the code