# OBJECT ORIENTED PROGRAMMING (OOP)
class Student:  # Constructor/Initialization
    def __init__(self,height,year,hometown):
        self.height = height
        self.year = year
        self.hometown = hometown

    def learning(self):    # Method/Function specifically for class Student
        print("This student is studying at university")

    def gotohometown(self):
        print("This student hometown is " + self.hometown)

ali = Student(170, 3,"Saudi")
print(ali.height)
print(ali.year)
print(ali.hometown)
ali.learning()
ali.gotohometown()


class Fruit:
    def __init__(self,price,colour,taste):
        self.price = price
        self.colour = colour
        self.taste = taste

    def ripe(self):
        print("The fruit is ripe")

    def spoil(self):
        print("The fruit is already spoiled")

watermelon = Fruit(20,"red","sweet")
print(watermelon.price)
print(watermelon.colour)
print(watermelon.taste)
watermelon.ripe()
watermelon.spoil()

durian = Fruit(30,"yellow","very sweet")
print(durian.price)
print(durian.colour)
print(durian.taste)
durian.ripe()
durian.spoil()

oren = Fruit(15,"orange","sour")
print(oren.price)
print(oren.colour)
print(oren.taste)
oren.ripe()
oren.spoil()
