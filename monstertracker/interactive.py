#!python2

"""
monster hp tracker beta.01

to do: create hd randomizer and max choice
incorperate dr to damage
create intarctive script to create monster till dead add monsters to list.
"""

# imports
import monstermain as mm

# variables
continueprogram = "y"
q = "create new foe?"


def foecreate():

    q = "what is its name?"
    n = raw_input(q)

    q = "how many hit die?"
    h1 = mm.numtest(q)

    q = "what hitdie shall be rolled?"
    h2 = mm.numtest(q)

    q = "what is its con score?"
    c = mm.numtest(q)

    q = "what is its damage reduction?"
    d = mm.numtest(q)

    return[n,h1,h2,c,d]


def main():
    args = foecreate()
    mon1 = mm.foe(*args)
    print mon1.conbonus
    print mon1.maxhp
    mon1.hpchange()

if __name__ == '__main__':
    main()

