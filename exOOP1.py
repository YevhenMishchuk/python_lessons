class Student:

    def __init__(self, name):
        self.name = name

  
    def sayHi(self):
        print("Hi from "+ self.name)
  
s1 = Student("Yevhen")
s1.sayHi()