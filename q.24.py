a=True
b=True
c=True
d=True
print(c) # ----> True
print(d) # ----> True
print(not a)   # ----> False
print(not b)   # ----> False
print(not c)   # ----> False
print(not d)   # ----> False
print(a and b)  # ----> True
print(a or b)   # ----> True
print(a and b or c)  # ----> True
print(not a or b or c)   # ----> True
print(not a or not b or not c)  # ----> False
print(not(not a or not b or not c))   # ----> True