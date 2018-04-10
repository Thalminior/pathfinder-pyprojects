#!python2

"""
monster hp tracker beta.01

to do: line 27
"""

# imports
import random
# variables


class foe:
    """
    creates monster with (HD LVL DR CON)
    """

    def __init__(self,totalhd,hitdie,constitution,damage_reduction=0):

        # inhearant
        self.dr = damage_reduction
        self.conscore = constitution
        self.hd = hitdie
        self.lvl = totalhd


        # created
        self.conbonus = int((self.conscore-10)/2)
        self.hp = ((self.hd + self.conbonus) * self.lvl)
# create hd randomizer and max choice

        self.maxhp = self.hp





if __name__ == '__main__':
    mon1 = foe(5,8,19,0)
    print mon1.conbonus
    print mon1.maxhp