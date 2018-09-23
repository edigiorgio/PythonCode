import random


class character:

    def __init__(self):
        self.__s = s
        self.__d = d
        self.__v = v
        self.__i = i
        
    def set_strength(self, s):
        self.__s = s
    def set_dexterity(self, d):
        self.__d = d
    def set_vitality(self, v):
        self.__v = v
    def set_intelligence(self, i):
        self.__i = i

    def get_strength(self):
        return self.__s

    def get_dexterity(self):
        return self.__d

    def get_vitality(self):
        return self.__v

    def get_intelligence(self):
        return self.__i


def main():
    warrior = character()
    print(warrior.get_dexterity())

main()
