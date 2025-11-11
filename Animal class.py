class Animal(object) : 

    def __init__(self, age) : 
        self.age = age 
        self.name = None

    def __str__(self) : 
        return f"Animal named {self.name} of age {self.age}"

    def get_age(self) : 
        return self.age
    def get_name(self) : 
        return self.name
    def set_name(self, newname="") :
        self.name = newname
    def set_age(self, newage) : 
        self.age = newage 

a = Animal(5)
print(a)

def make_animals(L1,L2) : 
    """ L1 is a list of ints and L2 is a list of strs 
    L1 and L2 have the same length 
    Creates a list of animals the same lenght as L1 and L2 
    An animal object has the name and age corresponding to the same index in L1 and L2, respectively"""

    animals_list = []

    for i in range(len(L1)) : 
        a = Animal(L1[i])
        a.set_name(L2[i])
        animals_list.append(a)
    return animals_list

list1 = [2,5,1]
list2 = ['blobfish','crazyant','parafox']

for i in make_animals(list1, list2) : 
    print(i)

class Cat(Animal) : 
    def __str__(self) : 
        return f"Cat named {self.name} of age {self.age}"
    def speak(self) : 
        print("Meow")

c = Cat(5)
c.set_name("Fluffy")
print(c)
c.speak
print(c.get_age())

class Human(Animal) : 
    def __init__(self,name,age) : 
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self) : 
        return self.friends.copy()
    def add_friends(self, friend_name) : 
        if friend_name not in self.friends : 
            self.friends.append(friend_name)
    def speak(self) : 
        print("Hello")
    def age_diff(self, other) : 
        diff = self.age - other.age 
        print(f"{abs(diff)} years age difference")
    def __str__(self) : 
        return f"Human named {self.name} of age {self.age}"

def make_pet(d) : 
    """ d is a dictionnary mapping a Human object to a Cat obj
    Prints on each line the name of a person, a colon, and the name of that person's Cat """

    for key, value in d.items() : 
        human_name = key.get_name()
        animal_name = value.get_name()
        print(human_name + ":" + animal_name)


p1 = Human("ana", 86)
p2 = Human("James", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(2)
c2.set_name("fluffsphere")

dict = {p1:c1 , p2:c2}

make_pet(dict)