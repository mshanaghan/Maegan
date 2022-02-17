list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

# Which items are present in both lists?
# def intersection(list_a, list_b):
#     list_c = [value for value in list_a if value in list_b]
#     return list_c
# print(intersection(list_a, list_b))

# Another quicker way:
# print(list(set(list_a) & set(list_b)))

# Which items do not overlap?
print(list(set(list_a) ^ set(list_b)))

# Yay! Got it. Stackoverflow provided the code.