#!python2
"""
to do:
create class people
create interactive creator
create3 disply of peoiple
clear up questions

"""
#  variables

group = []

# imports
import funfuncfile as fff

class person:
    def __init__(self,who,what_rolled):
        self.pname = who
        self.turn = what_rolled

    def __repr__(self):
        return repr((self.pname,self.turn))


def active():
    """
    interactive script for creating person class
    """
    q = "enter Name/Nickname > "
    w = raw_input(q)
    q = "what initiative was rolled?"
    r = fff.numtest(q)
    return [w,r]    

def personlist():
    while True:
        praw = active()
        who = person(*praw)
        group.append(who)
        q = "add another?"
        keep = fff.yesnoquest(q)
        if keep == "y":
            continue
        else:
            s = sorted(group, key=lambda person: person.turn, reverse=True)
            break
    return s


# def turnloop(turnlist):
#     """
#     takes list returnes 1 in list iterates though
#     """
#     t = turnlist
#     for i in t



def main():
    done = "no"
    b = personlist()
    print group
    print b
    while done == "n":
        done == fff.yesnoquest("done?")

if __name__ == '__main__':
    main()

