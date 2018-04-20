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


def turnloop(turnlist):
    """
    takes list returnes 1 in list iterates though
    """
    t = turnlist
    print "full list of players:"
    for t in t:
        print t
    
    # print turnlist[0],"first"
    # print turnlist[2],"third"
    
    done = "n"
    i = 0
    rc = 1
    while done == "n":
        print "round {0} current turn {1}".format(rc,turnlist[i])
        n = fff.yesnoquest("is {0} done?".format(turnlist[i]))
        if n == "y":
            i = i + 1        
            if i >= len(turnlist):
                i = 0
                rc = rc + 1
                done = fff.yesnoquest("is combat over?")
                pass
            else:
                pass
            continue
        else:
            print "{0} still needs to go".format(turnlist[i])
            continue

        


def main():
    print "this is a turn initative tracker"
    b = personlist()
    print "unordered list --",group
    print "ordered list --",b
    turnloop(b)
    
def debug():
    gr = []
    p = ["rogue",15]
    w = person(*p)
    gr.append(w)
    p = ["wizard",16]
    w = person(*p)
    gr.append(w)
    p = ["fighter",4]
    w = person(*p)
    gr.append(w)
    p = ["cleric",10]
    w = person(*p)
    gr.append(w)
    s = sorted(gr, key=lambda person: person.turn, reverse=True)
    print "unordered list --",gr
    print "ordered list --",s
    turnloop(s)


if __name__ == '__main__':
    # main()
    debug()
    fff.keepopen()
