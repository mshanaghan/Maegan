# # Using this dictionary, ask the user for a word and compute the scrabble word score for that word
#
# score = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }
#
#
# # # Creates a function which takes 1 argument
# def scrabble_score(word):
#     total = 0;
#     for i in word:
#         i = i.lower();
#         total = total + score[i];
#     return total;
# your_word = input("Word score: ");
# print(scrabble_score(your_word));

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word): #Returns the scrabble score for a given word

    points = 0

    for letter in word.lower():
        points += score[letter]

    return points

print(scrabble_score("Apple"))










