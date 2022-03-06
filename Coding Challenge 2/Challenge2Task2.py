#AD Paste the challenge written instructions here to make it easier for you to code,
# and for me to grade.

# 2. List overlap
# Using these lists:
#
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# Determine which items are present in both lists.
# Determine which items do not overlap in the lists.

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

# Which items are present in both lists?
def intersection(list_a, list_b):
    list_c = [value for value in list_a if value in list_b]
    return list_c
print(intersection(list_a, list_b))

#AD please do not comment out your responses to challenges.

# Another quicker way:
# print(list(set(list_a) & set(list_b)))

# Which items do not overlap?
print(list(set(list_a) ^ set(list_b)))
#AD you can get away without using the set function, use two for loops.


# Yay! Got it. Stackoverflow provided the code.