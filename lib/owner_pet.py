class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        if value not in self.PET_TYPES:
            raise Exception(f"{value} is not a valid pet type.")
        self._pet_type = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Owner):
            raise Exception(f"{value} is not an Owner instance.")
        self._owner = value


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} is not a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        # def sort_pets_by_name(self): # test is different from instructions in Canvas
        return sorted(self.pets(), key=lambda pet: pet.name)


# anthony = Owner(name="Anthony")
# rex = Pet(name="Rex", pet_type="dog", owner=anthony)
# whiskers = Pet(name="Whiskers", pet_type="cat", owner=anthony)

# print(anthony.get_sorted_pets())
# import ipdb

# ipdb.set_trace()
