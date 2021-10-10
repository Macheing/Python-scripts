class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = 'riptile'

print(Turtle.category)

class Snake(Animal):
    category ='reptile'

print(Snake.category)

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.category] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            #if self.category == category:
            if animal == Snake.category or Turtle.category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle('turtle') #create an instance of the Turtle class
snake = Snake('snake') #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category