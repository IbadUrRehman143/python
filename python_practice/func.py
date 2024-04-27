def list(open):
    ali=0
    for i in range (len(open)):
       ali=ali*open[i]

    # print(ali)
    return ali


p1=[23,2,4,5,7]
p2=[12,45,6,34,]
ibad = list(p1)
gulalam = list(p2)
s = ibad+gulalam
print(s)
     