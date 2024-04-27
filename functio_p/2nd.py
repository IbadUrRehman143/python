def function_name(product):
    pasa=1
    for i in range (len(product)):
        pasa = pasa*product[i]
    return pasa
    
li=[2,4,6,8]
s=function_name(li)
print(s)
