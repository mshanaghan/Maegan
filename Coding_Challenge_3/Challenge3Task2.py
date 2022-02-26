# 2. Push sys.argv to the limit
# Construct a rudimentary Python script that takes a series of inputs as a
# command from a bat file using sys.argv, and does something to them. The rules:
#
# Minimum of three arguments to be used.
# You must do something simple in 15 lines or less within the Python file.
# Print or file generated output should be produced.
import sys
# I turned my scrabble code from last week into code that takes arguments from the .bat file.
# There is definitely a shorter way of writing this,
# but I have already spent too long getting this code to work.

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for i in word:
        i = i.lower()
        total = total + score[i]
    return total
def main(arg):
    your_word = input(sys.argv[1])
print(scrabble_score(sys.argv[1]))
def main(arg):
    your_word = input(sys.argv[2])
print(scrabble_score(sys.argv[2]))
def main(arg):
    your_word = input(sys.argv[3])
print(scrabble_score(sys.argv[3]))








