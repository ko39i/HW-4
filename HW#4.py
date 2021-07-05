1


class Vehicle:
    def __init__(self, max_speed, mileage_instance):
        self.max_speed = max_speed
        self.mileage_instance = mileage_instance


2


class Bus(Vehicle):
    def __init__(self, max_speed, mileage_instance, seating_capacity):
        super().__init__(max_speed, mileage_instance)
        self.seating_capacity = seating_capacity


3
class_bus = Bus(80, 5000, 25)
check = isinstance(class_bus, Bus)
print(check)

4
check_slass = issubclass(Bus, Vehicle)
print(check_slass)

5


class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students


6


class SchoolBus(School, Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage_instance, seating_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage_instance, seating_capacity)
        self.bus_school_color = bus_school_color


7


class Bear:
    def make_sound(self, sound=''):
        print(sound)
        print('Growl')


class Wolf:
    def make_sound(self, sound=''):
        print(sound)
        print('Howl')


bear = Bear
wolf = Wolf
for animal in (bear, wolf):
    animal.make_sound('')
8


class City:
    def __int__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        x = super(City, cls).__new__(cls)

        if population < 1500:
            return print('Your city is too small')
        else:
            return x


9


def __str__(self):
    return f'The population of the city {self.name} is {self.population}'


city_1 = City('Lviv', 100000)
print(city_1)

city_2 = City('Avdeevka', 1100)
print(city_2)

10


class Add:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        self.other = other
        if self.other > 10:
            return self.other * self.a
        else:
            return self.other + self.a


11


class Sum:
    def __call__(self, a, b):
        d = a + b
        return d


12

class MyOrder:
    def __int__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        return len(self.cart) > 0

































































































