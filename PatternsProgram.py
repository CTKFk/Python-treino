### Pattern 1 ###
# Rows = 5
# for i in range(0,Rows):
#     for j in range(0,i + 1):
#         print("*", end=" ")
#     print("*\r")  # New line after each row

### Pattern 2 ###
# Rows = 5
# for j in range(1, Rows + 1):
#     print("* " * j)

### Pattern 3 ###
# Rows = 5
# k = 2 * Rows - 2
# for i in range(0, Rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")