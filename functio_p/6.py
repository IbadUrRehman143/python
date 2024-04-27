def input_45(it): 
    ab=1
    for i in range (len(it)):
        ab = ab//it[i]
    return ab 
p1 =[566/8]
s=input_45(p1)
print(s)