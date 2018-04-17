
def yesnoquest(q):
    """
    askes a yes/no question with output being y/n
    :param raw input query: 
    """
    while True:
        a = raw_input(q) 
        if a == "y" or a == "n":
            break
        else:
            print """please reply with either "y" or "n" > """
    return a          

def numtest(q):
    """
    checks input for intager
    :param rawinput request text<string>:
    """
    while True:
        try:
            n = int(raw_input(q))
        except (ValueError, TypeError):
            print "Not a number! Try again"
        else:
            break
    return n


  
def main():
    test = numtest("this is a test")
    test2 = yesnoquest("yes or no")

    print test,test2

if __name__ == '__main__':
    main()