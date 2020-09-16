import json

class NeighborhoodPets:
    def __init__(self):
        self._name = None
        self._species = None
        self._owners_name = None
        self._pets_list = []
    
    def add_pet(self, name, species, owners_name):
        pet_list = []
        
        if self._name == name:
            return
        else:
            self._name = name
            self._species = species
            self._owners_name = owners_name
            pet_list.append(name)
            pet_list.append(species)
            pet_list.append(owners_name)
        
        self._pets_list.append(pet_list)
    
    def get_pets_list(self):
        return self._pets_list

    def delete_pet(self, name):
        for pet in self._pets_list:
            if name == pet[0]:
                self._pets_list.remove(pet)
    
    def get_owner(self, name):
        for owner in self._pets_list:
            if name == owner[0]:
                return owner[2]
    
    def save_as_json(self, filename):
        with open(filename, 'w') as wf:
            json.dump(self._pets_list, wf)
    
    def read_json(self, filename):
        try:
            with open(filename, 'r') as rf:
                self._pets_list = json.load(rf)
        except FileNotFoundError:
            print("file not found")
    
    def get_all_species(self):
        species_list = []
        
        for pet in self._pets_list:
            species_list.append(pet[1])
        species_set = set(species_list)
        
        return species_set

def main():
    np = NeighborhoodPets()
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "bunny", "Matt")
    np.add_pet("Spot", "zebra", "Farrokh")
    print(np.get_pets_list())
    np.save_as_json("pets.json")
    np.delete_pet("Tiny")
    np.delete_pet("Timmy") # doesn't matter if pet name exists or not
    print("Now pet list has ", np.get_pets_list())
    mem_set = np.get_all_species()
    print("Species in memory are: ", mem_set)
    spot_owner = np.get_owner("Spot")
    fluffy_owner = np.get_owner("Fluffy")
    tiny_owner = np.get_owner("Tiny")
    npH = NeighborhoodPets()
    npH.add_pet('Fang', 'dog', 'Hagrid')
    npH.add_pet('Fawkes', 'phoenix', 'Dumbledore')
    npH.add_pet('Buckbeak', 'hippogriff', 'Sirius')
    npH.save_as_json('other_pets.json')
    np.read_json("other_pets.json")
    species_set = np.get_all_species()
    fang_owner = np.get_owner("Fang")
    print(species_set)
    print(spot_owner)
    print(fluffy_owner)
    print(tiny_owner)
    print(fang_owner)
    print(np.get_pets_list())

if __name__=="__main()__": main()
main()