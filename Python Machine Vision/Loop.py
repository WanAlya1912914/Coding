# FOR LOOP

mylist = [1,2,3,4]
square = []

for num in mylist:
    if num<3:
        square.append(num*num)
    
print(square)

#####################################################################################################################################

# LIST COMPREHENSION

print([num*num for num in mylist if num<3])

