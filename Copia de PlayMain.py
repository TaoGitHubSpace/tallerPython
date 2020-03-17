import random
import json

def success():
    rand=random.randrange(0,100)
    if rand>50:
        return True
    else:
        return False


class Soul(object):
    def __init__(self,name,hp,atk,powerL,powerH,defense,mana,recov):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.powerl=powerL
        self.powerh=powerH
        self.defense=defense
        self.mana=mana
        self.recov=recov
    
    def say_name(self):
        print(f"Hi, my name is to {self.name}")

    def task(self,mission):
        print(f'My mission is to {mission}')
    
    def attack(self, obj):
        Hist=[]
        if self.hp<=0:
            print(f'{self.name} is dead')
            Hist.append(f'{self.name} is dead')
            print(Hist)
        else:
            if self.mana<=0:
                print(f"{self.name} Your mana is finish, wait for the next turn")
                Hist.append(f"{self.name} Your mana is finish, wait for the next turn")
                self.mana += self.recov
                self.recov = 0
                #print(f'{self.name} new mana level is: {self.mana}')
                #print(f'{self.name} new recov mana is: {self.recov}')
            else:
                while True:
                    t=input(f'{self.name} choose an attack power\nA:{self.powerl}\nB:{self.powerh}\n').upper()
                    if t=="A":
                        print(f'{self.name} attacked with {self.powerl} to {obj.name}')
                        Hist.append(f'{self.name} attacked with {self.powerl} to {obj.name}')
                        break
                    elif t=="B":
                        print(f'{self.name} attacked with {self.powerh} to {obj.name}')
                        Hist.append(f'{self.name} attacked with {self.powerh} to {obj.name}')
                        break
                    else:("Try again")

                self.mana -= self.atk
                self.recov += self.atk
               #print(f'{self.name} new mana level is: {self.mana}')
               #print(f'{self.name} new recov mana is: {self.recov}')
                if success():
                    if obj.hp<=0:
                        print(f'{obj.name} is dead')
                        Hist.append(f'{obj.name} is dead')
                        print(Hist)
                    else:
                        print(f'{obj.name} has been hit by {self.name}')
                        Hist.append(f'{obj.name} has been hit by {self.name}')
                        if self.atk > obj.defense:
                            obj.hp -= self.atk
                            obj.hp += obj.defense
                            print(f'{obj.name} HP is now {obj.hp}')
                            Hist.append(f'{obj.name} HP is now {obj.hp}')
                            if obj.hp<=0:
                                print(f'{obj.name} is dead')
                                Hist.append(f'{obj.name} is dead')
                                print(Hist)
                        else:
                            print(f'The {obj.name} defense is stronger than the {self.name} attack')
                            Hist.append(f'The {obj.name} defense is stronger than the {self.name} attack')
                            if obj.hp<=0:
                                print(f'{obj.name} is dead')
                                Hist.append(f'{obj.name} is dead')
                                print(Hist)
                else:
                    print(f'{self.name} miss attack to {obj.name}')
                    Hist.append(f'{self.name} miss attack to {obj.name}')

class Human(Soul):
    def mission(self):
        self.task("Get the treasure")

class Monster(Soul):
    def mission(self):
        self.task("Defend the treasure")

class Warrior(Human):
    def intro(self):
        print(f'I\'m {self.name} i have \nHP: {self.hp}\nAttack: {self.atk}\nPowers: {self.powerl}, {self.powerh}\nDefense: {self.defense}\nMana: {self.mana}')

class Mage(Human):
    def intro(self):
        print(f'I\'m {self.name} i have \nHP: {self.hp}\nAttack: {self.atk}\nPowers: {self.powerl}, {self.powerh}\nDefense: {self.defense}\nMana: {self.mana}')

class Elf(Human,Monster):
    def intro(self):
        print(f'I\'m {self.name} i have \nHP: {self.hp}\nAttack: {self.atk}\nPowers: {self.powerl}, {self.powerh}\nDefense: {self.defense}\nMana: {self.mana}')

class Centaur(Monster,Human):
    def intro(self):
        print(f'I\'m {self.name} i have \nHP: {self.hp}\nAttack: {self.atk}\nPowers: {self.powerl}, {self.powerh}\nDefense: {self.defense}\nMana: {self.mana}')

class Skeleton(Monster):
    def intro(self):
        print(f'I\'m {self.name} i have \nHP: {self.hp}\nAttack: {self.atk}\nPowers: {self.powerl}, {self.powerh}\nDefense: {self.defense}\nMana: {self.mana}')

class Slime(Monster):
    def intro(self):
        print(f'I\'m {self.name} i have \nHP: {self.hp}\nAttack: {self.atk}\nPowers: {self.powerl}, {self.powerh}\nDefense: {self.defense}\nMana: {self.mana}')



