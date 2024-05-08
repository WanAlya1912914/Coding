class Person:
    def __init__(me,name ,age,sex):
        me.name = name
        me.age = age
        me.sex = sex
    
    def intro(me):
        print('my name is ' + me.name + ' and my age is ' + str(me.age)) 
        

c1 = Person('Wan Alya Athirah',23,'Female')
c1.intro()

