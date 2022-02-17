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

# These commands put the print statement at the end
# for i in task_1_list:
#     if i == 6:
#         break
#     print(i)

# # Trying the solution by desiato to get these commands in 1 line
# filtered = [i for i in task_1_list if i==3]
# print(i)

# Fail