# l1=["apple", "banana", "mango", "potato", "tomato "]
# l2=[8888, 6789, 9999, 7777, 8888]
# namePrice=[]

# for i in range(len(l1)):
#     namePrice.append([l1[i], l2[i]])

# print(namePrice)

"""
+---+---+---+---+---+---+---+
| 2 | 5 | 6 | 7 | 9 | 8 | 1 |
+---+---+---+---+---+---+---+
"""
license=[2, 5, 6, 7, 8, 9, 7]


for i in range(len(license)):
    print(" | ",license[i],end="",)
    if i == 6:
        print(" | ") 
