class Dog: #class name is called Dog
    def __init__(self, name,legs): #used innit function to assign values to object properties
        self.name = name
        self.legs = legs

    def speak(self):
        print(self.name + 'says: bark !')

d1 = Dog("Bobby", 4) #created an object which was d1
print(d1.name) #used the object we created to print out the name and legs
print(d1.legs)
d1.speak()

