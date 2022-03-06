#AD Paste the challenge written instructions here to make it easier for you to code,
# and for me to grade.

# 1. List values
# Using this list:
#
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# You need to do two separate things here and report both in your Python file. You should
# have two solutions in this file, one for item 1 and one for item 2. Item 2 is tricky so if
# you get stuck try your best (no penalty), for a hint check out the solution by desiato here.
#
# Make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python (you do not need to append to a list just print the output).




task_1_list = [1,2,3,6,8,12,20,32,46,85]
# These commands do not use a loop, so they do not meet the challenge
# # print(task_1_list)
# del task_1_list[3:]
# print(task_1_list)
# print(task_1_list[:3])

# Break statement allows us to stop the loop before
# it has looped through all the items in the list
# This code says exit the loop when i is 3
for i in task_1_list:
    print(i)
    if i == 3:
        break

#AD no need to use the break, it is bad coding practice, just use < instead of ==, as if I had a 4 in the list
# your code would not pick it up. Also you missed the requirement to make a new list rather
# than just printing the result.
new_task_1_list = []
for i in task_1_list:
    if i < 5:
        new_task_1_list.append(i)
print(new_task_1_list)


# These commands put the print statement at the end
# for i in task_1_list:
#     if i == 6:
#         break
#     print(i)

# # Trying the solution by desiato to get these commands in 1 line
# filtered = [i for i in task_1_list if i==3]
# print(i)

# Fail

#AD not sure why you commmented this out, you need it to address the challenge
print([i for i in task_1_list if i < 5])
