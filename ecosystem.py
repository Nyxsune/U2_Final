"""
Connor Cox
U2 Project
Bear Fish River
"""
from random import choice
from random import randint
import random

class River:

  def __init__(self, size, num_bears, num_fish):
    self.river = [['🟦 ']*size for i in range(size)]
    self.size = size
    self.num_bears = num_bears
    self.num_fish = num_fish
    self.animals = []
    self.population = 0
    self.__initial_population()

  def __str__(self):
    self.redraw_cells()
    out = ""
    for row in self.river:
      for cell in row:
        out += str(cell)
      out += "\n"

    return out

  def __getitem__(self, index):
    return self.river[index]

  def animal_death(self, animal):
    self.population -= 1
    index = self.animals.index(animal)
    del self.animals[index]

  def redraw_cells(self):
    self.river = [['🟦 ']*self.size for i in range(self.size)]
    for animal in self.animals:
      self.river[animal.y][animal.x] = animal
  
  def __initial_population(self):
    for i in range(self.num_bears + self.num_fish):
      x = randint(0, self.size-1)
      y = randint(0, self.size-1)
      for animal in self.animals:
        if animal.y == y and animal.x == x:
          direction_moved = choice(['x', 'y'])
          if direction_moved == 'x':
            L_or_R = choice(['l', 'r'])
            if L_or_R == 'l':
              if x == 0:
                x += 1
              else:
                x -= 1
            else:
              if x == self.size-1:
                x -= 1
              else:
                x += 1
          else:
            U_or_D = choice(['u', 'd'])
            if U_or_D == 'u':
              if y == 0:
                y += 1
              else:
                y -= 1
            else:
              if y == self.size-1:
                y -= 1
              else:
                y += 1
      if i < self.num_bears:
        bear = Bear(x, y)
        self.animals.append(bear)
      else:
        fish = Fish(x, y)
        self.animals.append(fish)
      self.population += 1
    
  
  def place_baby(self, species):
    x = randint(0, self.size-1)
    y = randint(0, self.size-1)
    for animal in self.animals:
      if animal.y == y and animal.x == x:
        direction_moved = choice(['x', 'y'])
        if direction_moved == 'x':
          L_or_R = choice(['l', 'r'])
          if L_or_R == 'l':
            if x == 0:
              x += 1
            else:
              x -= 1
          else:
            if x == self.size-1:
              x -= 1
            else:
              x += 1
        else:
          U_or_D = choice(['u', 'd'])
          if U_or_D == 'u':
            if y == 0:
              y += 1
            else:
              y -= 1
          else:
            if y == self.size-1:
              y -= 1
            else:
              y += 1
    if species == "bear":
      bear = Bear(x, y)
      self.animals.append(bear)
    elif species == "fish":
      fish = Fish(x, y)
      self.animals.append(fish)
    self.population += 1
  
  def new_day(self):
    for animal in self.animals:
      animal.move(self)
    for animal in self.animals:
      if type(animal) == Bear:
        if animal.eaten_today == False:
          animal.starve(self)




class Animal:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.bred_today = False

  def death(self, River):
    animal = self
    River.animal_death(animal)

  def move(self, River):
    direction_moved = choice(['x', 'y'])
    if direction_moved == 'x':
      L_or_R = choice(['l', 'r'])
      if L_or_R == 'l':
        if self.x == 0:
          self.x += 1
        else:
          self.x -= 1
      else:
        if self.x == River.size-1:
          self.x -= 1
        else:
          self.x += 1
    else:
      U_or_D = choice(['u', 'd'])
      if U_or_D == 'u':
        if self.y == 0:
          self.y += 1
        else:
          self.y -= 1
      else:
        if self.y == River.size-1:
          self.y -= 1
        else:
          self.y += 1

    for animal in River.animals:
      if animal.x == self.x and animal.y == self.y and animal != self:
        self.collision(animal, River)
  
  def collision(self, animal, River):
    if type(animal) == type(self):
      if type(animal) == Bear:
        species = "bear"
      elif type(animal) == Fish:
        species = "fish"

      multi_birth = random.uniform(0, 1)
      if multi_birth <= 0.001:
        River.place_baby(species)
        River.place_baby(species)
        print(f"A {species} Had Triplets!")
      elif multi_birth <= 0.01:
        River.place_baby(species)
        print(f"A {species} Had Twins!")
      else:
        print(f"New Baby {species}")
      River.place_baby(species)
      self.bred_today == True
      animal.bred_today == True
    else:
      if type(animal) == Bear:
        animal.consume(self, River)
      elif type(self) == Bear:
        self.consume(animal, River)

class Fish(Animal):
  
  def __str__(self):
    return "🐟 "
  
class Bear(Animal):

  def __init__(self, x, y):
    Animal.__init__(self, x, y)
    self.max_lives = 5
    self.lives = 5
    self.eaten_today = False

  def __str__(self):
    return "🐻 "
  
  def starve(self, River):
    self.lives -= 1
    if self.lives == 0:
      self.death(River)
      print("A Bear Starved to Death")
  
  def consume(self, fish, River):
    self.lives = self.max_lives
    fish.death(River)
    self.eaten_today == True
    print("A Fish Was Eaten")


    
  