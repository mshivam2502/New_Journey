class Animal:
    def walk(self):
        print("Walking")

class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def bark(self):
        print("Woof!")

if __name__ == "__main__":
    roger = Dog("Roger")

    roger.bark()

    print(roger.name)
    roger.walk()