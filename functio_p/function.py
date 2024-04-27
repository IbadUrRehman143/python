# def is_sub_string(string: str , sub_string:str)->bool :
#    if not isinstance(string, str) and not isinstance(sub_string, str): 
#       raise ValueError("both  arguments  must be a type str"  )
#    for i in range (len(string)):
#       if string [i:]== sub_string:
#          return True
#    return False
# print(is_sub_string("ibad khan","78"))

# def is_sub_string(string: str, sub_string: str) -> bool:
#     """
#     Paramaters
#     ----------
#         string
#             actual string
#         sub_string
#             sub string of the actual string
    
#     Returns
#     -------
#         True if sub_string
#         False else
#     """

#     if (not isinstance(string, str)) and (not isinstance(sub_string, str)):
#         raise ValueError("Both argumets must be of type str")
    
#     for i in range(len(string)):
#         if string[i:] == sub_string:
#             return True
#     return False
        

# print(is_sub_string("ibad khan", "khan"))



def divisible_by_b(a,b):
   next_number = (a // b + 1 )* b 
   return next_number
result=divisible_by_b(17,8)
print(result)
