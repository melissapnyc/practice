import random

answer = {1: "Yes", 2: "Maybe", 3: "No"}

response = "yes"
while response == "yes":
    question = raw_input("What would you like to know (that I can answer with yes or no?): ")

    x = random.randint(1, 3)
    l = (20 - len(answer[x]))/2
    s = ""
    for i in range(1, l+1):
        s += " "
        i += 1
    print "    -------------- "
    print "  /                \ "
    print " /       / \        \ "
    print "|       /   \        |"  
    print "|      /     \       |"
    print s, answer[x], s
    print "|    /         \     |"
    print " \    ---------     / "
    print "  \                / "
    print "    ------------- "        
        
    response = raw_input("Want to ask another question?: ")
    
