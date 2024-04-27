x = [3, 5, 8, 2, 9, 10, 89, 67]
# Problem
# sum = x[0] + x[1]+ x[2]+ x[3]+ x[4]+ x[5]
############################################################3
# sum = 0
# sum = sum + x[0] #3
# sum = sum + x[1] #8
# sum = sum + x[2] #16
# sum = sum + x[3] #18
# sum = sum + x[4] #27
# sum = sum + x[5] #37



# Solution
sum = 0
for i in range(len(x)):
    sum = sum + x[i]
    # print("x[" + str(i) + "] = " + str(x[i]) + " sum is: " + str(sum))


print(sum)