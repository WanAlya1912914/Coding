# DATA TYPE AND DATA STRUCTURE
num = 1
num = num + 2
temp = num
print (num + 5)
num = num + 5
print(num)
print(temp)

a = 10
b = 5.5
c = a+ b
print(c)
print(a + b)
d = 10
e = 25
f = 10.7
print(d * e * f)

g = 3.3
h = 5.7
print((g+h)/2)
i = g + h
print(i/2)

# Input #####################################################################################
var = input("Please enter a number : ")

# Method 1
# varInt = int(var)
# x = varInt * 2

# Method 2
x = float(var)*2
print(x)

var2 = input("Please enter your name : ")
print("My name is " + var2)

# Python List ###############################################################################
students = ["Azmi", "Ahmad", "Rajoo", "Choo", "David"]
print(students[1])
print(students[4])

studentsHeight = [150,160,167,155,170,178,158]
print(studentsHeight[0])
print(studentsHeight[2])
print(studentsHeight[6])

colours = ["red", "blue", "green"]
print(colours)
print(colours[0])
print(colours[1])
print(colours[2])
colours.append("white")         # append to add at the end of list
colours.append("yellow")
print(colours)
colours.insert(3,"red")     # insert to add at the specific index and push other to next index
print(colours)
print(colours.count("red"))     # to count the element repeated in the list
colours.clear()     # to clear the list
print(colours)

car = ["Honda", "Toyota", "Nissan", "Kia", "Hyundai", "Kia"]
print(car.count("Kia"))
car.insert(3, "Daihatsu")
print(car)
car.clear()
print(car)




