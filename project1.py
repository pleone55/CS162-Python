from statistics import mean, median, mode

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    """Setter Methods"""
    def set_name(self, name):
        if self._name == " " or self._name == None:
            print("Name cannot be blank")
        else:
            self._name = name
    
    def set_age(self, age):
        if self._age < 0:
            raise ValueError("Cannot have age under 0")
        else:
            self._age = age
    
    """Getter Methods"""
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age

def basic_stats(p_list):
    if len(p_list) <= 0:
        print("List is empty. Nothing to calculate")
    else:
        people_ages = []
        for item in p_list:
            people_ages.append(int(item.get_age()))
        if len(people_ages) == len(set(people_ages)):
            mode_ages = "No mode found"
        else:
            mode_ages = mode(people_ages)
        return (mean(people_ages), median(people_ages), mode_ages)

p1 = Person("Paul", 28)
p2 = Person("Alejandra", 26)
p3 = Person("Karla", 23)
p4 = Person("Josh", 25)
p5 = Person("Jerome", 25)
p6 = Person("Jon", 33)

print(basic_stats([p1, p2, p3, p4, p5, p6]))