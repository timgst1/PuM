from abc import ABC,abstractmethod
import random

class Duck(ABC):
    def __init__(self,name):
        self.__distance = 0
        self.__name = name
    def run(self):
        self.__distance += self.run_special()

    def get_distance(self):
        return self.__distance

    def get_name(self):
        return self.__name

    @abstractmethod
    def run_special(self):
        pass
    

class RandomDuck(Duck):
    def __init__(self, a, b):
        super().__init__("RandomDuck")
        self.__a = a
        self.__b = b

    def run_special(self):
        return random.randint(self.__a, self.__b)


class TiringDuck(Duck):
    def __init__(self, a, b):
        super().__init__("TiringDuck")
        self.__a = a
        self.__b = b
        temp = 0

    def run_special(self):
        temp = self.__b 
        self.__b -= self.__a
        return temp 


class DuckRace:
    def __init__(self):
        self.__ducks = []

    def add_duck(self, duck):
        self.__ducks.append(duck)

    def race(self):
        while True:
            for d in self.__ducks:
                d.run()
                if d.get_distance()>100:
                    return d


race = DuckRace()
race.add_duck(TiringDuck(0.5, 10))
race.add_duck(RandomDuck(5, 8))

winner = race.race()
print(winner.get_name())
