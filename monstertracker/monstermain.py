#!python2

"""
monster hp tracker beta.01

to do: 
incorperate dr to damage
create intarctive script to create monster till dead
"""

# imports
import random
import funfuncfile as fff
# variables


# classes
class foe:
    """
    creates monster with (name HD LVL DR CON)
    """

    def __init__(self,name,totalhd,hitdie,constitution,damage_reduction=0,rmhq="no"):

        # inhearant
        self.name = name
        self.dr = damage_reduction
        self.conscore = constitution
        self.hd = hitdie
        self.lvl = totalhd
        self.stillalive = "yes"

        # created
        self.conbonus = int((self.conscore-10)/2)

        if rmhq == "y":
            self.hp = ((self.hd + self.conbonus) * self.lvl)
        else:
            self.hp = ((random.randint(1,self.hd) + self.conbonus) * self.lvl)
      
        self.maxhp = self.hp

    def hpchange(self):
        """
        deals damage and healing to foe
        """
        
        messege = "enter ammount of damage/healing"
        hitvalue = fff.numtest(messege)
        
        if hitvalue <= 0:
            pass
        else:
            drq = "apply dr?"
            applydrq = fff.yesnoquest(drq)
            if applydrq == "y":
                hitvalue = hitvalue - self.dr
            else:
                pass
        self.hp = self.hp - hitvalue

        if self.hp <= (0 - self.conscore):
            print "{0} is dead".format(self.name)
            self.stillalive = "no"
        else:
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            else:
                pass
        self.remainmsg = "{0} has {1}/{2} hp remaining".format(self.name,self.hp,self.maxhp)
        print self.remainmsg




if __name__ == '__main__':
    mon1 = foe("spider",5,8,20,5,"y")
    print "con bonus :",mon1.conbonus
    print "max hp :",mon1.maxhp
    while mon1.stillalive == "yes":
        mon1.hpchange()
