#!python2

"""
monster hp tracker beta.01

to do: create hd randomizer and max choice
incorperate dr to damage
create intarctive script to create monster till dead
"""

# imports
import random
# variables


# functions



def numtest(q):
    """
    checks input for intager
    :param console num request text<string>:
    """
    q = q
    while True:
        try:
            n = int(raw_input(q))
        except (ValueError, TypeError):
            print "Not a number! Try again"
        else:
            break
    return n 

# classes
class foe:
    """
    creates monster with (name HD LVL DR CON)
    """

    def __init__(self,name,totalhd,hitdie,constitution,damage_reduction=0):

        # inhearant
        self.name = name
        self.dr = damage_reduction
        self.conscore = constitution
        self.hd = hitdie
        self.lvl = totalhd
        self.sillalive = "yes"


        # created
        self.conbonus = int((self.conscore-10)/2)
        self.hp = ((self.hd + self.conbonus) * self.lvl)
# create hd randomizer and max choice

        self.maxhp = self.hp

    def hpchange(self):
        """
        deals damage and healing to foe
        """
        
        messege = "enter ammount of damage/healing > "
        hitvalue = numtest(messege)
        self.hp = self.hp - hitvalue

        remainmsg = "{0} has {1} hp remaining".format(self.name,self.hp)

        if self.hp <= (0 - self.conscore):
            print "{0} is dead".format(self.name)
            self.stillalive = "no"
        else:
            if self.hp >= self.maxhp:
                self.hp = self.maxhp
                print remainmsg
            else:
                print remainmsg





if __name__ == '__main__':
    mon1 = foe("spider",5,8,19)
    print mon1.conbonus
    print mon1.maxhp
    mon1.hpchange()