def firstDuplicate(a):
    #Check input
    assert type(a) is list and len(a) is not 0

    #Define Set, Counter, N
    full_set = set()
    counter = 0
    n = len(a)

    #Check for Duplicates
    for i in a:
        counter +=1
        if i in full_set:
            print("the first duplicate is {}...".format(i))
            return i
        elif i not in full_set:
            full_set.add(i)
            if counter<n:
                pass
            elif counter==n:
                print("there are no duplicates in the array...")
                return -1
            else:
                return "counter error"
        else:
            return "unknown error occured"
