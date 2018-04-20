#yes no question
def yesnoquest(q):
    """
    askes a yes/no question with output being y/n
    :param raw input query: 
    """

    while True:
        q2 = "(y/n)"
        a = raw_input("{0} {1}> ".format(q,q2)) 
        if a == "y" or a == "n":
            break
        else:
            print """please reply with either "y" or "n" > """
    return a          

#Int valadator

def numtest(q):
    """
    checks input for intager
    :param rawinput request text<string>:
    """
    while True:
        try:
            n = int(raw_input("{0} > ".format(q)))
        except (ValueError, TypeError):
            print "Not a number! Try again"
        else:
            break
    return n


def keepopen():
    while True:
        j = yesnoquest("are you done?")
        if j == "n":
            pass
        else:
            break



  
def main():
    test = numtest("enter a number")
    test2 = yesnoquest("yes or no")

    print test,test2

if __name__ == '__main__':
    main()