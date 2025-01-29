class dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
ob=dog("German Shepherd",8)
ob1=dog("Husky",6) 
print("{} is {} years old".format( ob.name, ob.age)) 
print("{} is {} years old".format( ob1.name, ob1.age))      
        