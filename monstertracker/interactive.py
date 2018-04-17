#!python2

"""
monster hp tracker beta.01

to do: 
incorperate dr to damage
create intarctive script to create monster till dead add monsters to list.
"""

# imports
import monstermain as mm
import funfuncfile as fff

# variables

# continueprogram = "y"
# q = "create new foe?"


def foecreate():

    q = "what is its name?"
    n = raw_input(q)

    q = "what level is it? ie how many hit die?"
    h1 = fff.numtest(q)

    q = "what hitdie shall be rolled?"
    h2 = fff.numtest(q)

    q = "what is its con score?"
    c = fff.numtest(q)

    q = "what is its damage reduction?"
    d = fff.numtest(q)

    q = "use max hitpoints"
    m = fff.yesnoquest(q)

    return[n,h1,h2,c,d,m]


def main():
    args = foecreate()
    mon1 = mm.foe(*args)
    print mon1.conbonus
    print mon1.maxhp
    print mon1.stillalive
    while mon1.stillalive == "yes":
        mon1.hpchange()
    

def keepopen():
    
    while True:
        j = fff.yesnoquest("are you done?")
        if j == "n":
            pass
        else:
            break


if __name__ == '__main__':
    main()
    keepopen()
