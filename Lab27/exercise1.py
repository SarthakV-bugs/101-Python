
class Animal:
    phylum = ''
    __limbs = 4
    __voice = "A general animal sound"

    def __init__(self,phylum):
        self.phylum = phylum

    @staticmethod
    def kingdom():
     return "Animalia"

    def getPhylum(self):
        return self.phylum

    @property   #gets the value
    def legs(self):
        return self.__limbs

    @legs.setter #sets the value
    def legs(self,val):
        self.__limbs = val

    @property
    def sound(self):
        return self.__voice

    @sound.setter
    def sound(self, voice):
        self.__voice = voice


    @classmethod
    def description(cls):
        return cls.__name__


human = Animal('Mammal')
print(f'phylum of human:{human.phylum}')
dog = Animal('Mammal')
print(dog.phylum)
pigeon=Animal('Aves')
print(pigeon.phylum)

print(Animal.kingdom())
print(Animal.description())
print(dog.getPhylum())
print(pigeon.getPhylum())

print(dog.legs)
print(pigeon.legs)
print(human.sound)

print('After setting the values:')

human.sound = "speech"
print(human.sound)
dog.sound = "bark"
print(dog.sound)
pigeon.sound = "chirp"
print(pigeon.sound)


human.legs = 2
print(human.legs)
dog.legs = 4
print(dog.legs)
pigeon.legs = 2
print(pigeon.legs)

