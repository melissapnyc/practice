for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print "CracklePop"
    elif x % 3 == 0:
        print "Crackle"
    elif x % 5 == 0:
        print "Pop"
    else:
        print x
