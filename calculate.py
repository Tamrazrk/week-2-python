print(5 < 3) 
# output False
# 5 < 3 is evaluating if 5 is less than 3, which is not true, so the result is False.

print(3 == 3)
# output True 
# 3 == 3 is evaluating if 3 is equal to 3, which is true, so the result is True.

print(3 == "3")
# output False 
# 3 == "3" is comparing an integer (3) to a string ("3").
#  Since they are of different data types and have different values, the result is False.

print("3" > 3)
# output error 
# This expression attempts to compare a string ("3") with an integer (3) using the greater than (>) operator.
# In Python, comparing objects of different types like this will raise a TypeError.

print( "Hello" == "hello")
# output False 
# "Hello" == "hello" is evaluating if the string "Hello" is equal to the string "hello". 
# Since the strings are case-sensitive, the result is False.
