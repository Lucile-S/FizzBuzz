for x in xrange(1, 200):
 
    fizz = not x % 3
    buzz = not x % 5
 
    if fizz and buzz :
        print "Titigrosminet"
    elif fizz:
        print "Titi"
    elif buzz:
        print "grosminet"
    else:
        print x
