class Dog:
    def __init__(self, name, breed, age):
        self.name = name  
        self.breed = breed  
        self.age = age  
        self.is_hungry = False  
        self.is_sleepy = False  
    
    def bark(self):
        print(f"{self.name} гавкає!")
    
    def eat(self):
        self.is_hungry = False
        print(f"{self.name} поїла.")
    
    def sleep(self):
        self.is_sleepy = False
        print(f"{self.name} спить.")
    
    def play(self):
        if self.is_hungry:
            print(f"{self.name} занадто голодна, щоб грати.")
        elif self.is_sleepy:
            print(f"{self.name} занадто втомлена, щоб грати.")
        else:
            print(f"{self.name} грається весело!")
    
    def feed(self):
        self.is_hungry = False
        print(f"{self.name} нагодована.")
    
    def get_older(self):
        self.age += 1
        print(f"{self.name} стала старшою на рік! Тепер їй {self.age} років.")
    
    def become_hungry(self):
        self.is_hungry = True
        print(f"{self.name} голодна.")
    
    def become_sleepy(self):
        self.is_sleepy = True
        print(f"{self.name} хоче спати.")

dog = Dog(name="Бобік", breed="Короткошерстий тер'єр", age=3)

dog.bark()
dog.eat()
dog.sleep()
dog.play()
dog.get_older()
dog.become_hungry()
dog.feed()
dog.play()
