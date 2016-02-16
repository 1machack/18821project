from itertools import *


def run(n,pi):
    x = analyze(generate_data(n,pi))
    print x
    return x

def analyze_tree(data):
    allDegrees = {}
    for i in data:
        for j in i:
            origPerm = j[0]
            addPerms = j[1]
            parentDegrees = []

            origTuple = tuple(origPerm)
            
            if len(origPerm)>0:
                maxIndex = 0
                maxValue = 0
                for k in range(len(origPerm)):
                    if origPerm[k]>maxValue:
                        maxValue = origPerm[k]
                        maxIndex = k

                prevPerm = origPerm[:maxIndex] + origPerm[maxIndex+1:]
                prefixTuple = tuple(prevPerm)
                print prefixTuple
                parentDegrees = allDegrees[prefixTuple]
                print parentDegrees
                
            allDegrees[origTuple] = list(parentDegrees) + [len(addPerms)]

    return allDegrees
            

def generate_data_tree(n,pi):
    data = [[    [[],[[1]]]   ]] # [[    [None,[[1]]]   ]]
    for i in range(n-1):
        print i
        newlevel = []
        
        prevlevel = []

        for y in data[-1]:
            prevlevel = prevlevel + y[1]


        for x in prevlevel:

            newset = []
            for j in range(i+2):
                k=x[:j] + [i+2] + x[j:]
                if check_avoid(k,pi):
                    newset.append(k)

            newlevel.append([x, newset])
        

        data.append(newlevel)
    return data

def generate_data(n,pi):
    data = [[[1]]]
    for i in range(n-1):
        print i
        possibleset = []
        for x in data[-1]:
            for j in range(i+2):
                possibleset.append(x[:j] + [i+2] + x[j:])
                
        newset = []
        for k in possibleset:
            if check_avoid(k,pi):
                newset.append(k)
        data.append(newset)
    return data

def analyze(data):
    x = []
    for i in range(len(data)):
        x.append(len(data[i]))
    return x

def check_avoid(subseq, pi):
    if len(subseq) < len(pi):
        return True

    choices = generate_choices(subseq, len(pi))
    for i in choices:
        if check_order(list(i), pi):
            return False
    return True

def check_order(seq, pi):
    n = len(seq)
    m = max(seq) + 1
    newseq = [0]*n
    for i in range(n):
        minindex = seq.index(min(seq))
        newseq[minindex] = i+1
        seq[minindex] = m
    if newseq == pi:
        return True
    return False


def generate_choices(subseq, n):
    return list(combinations( subseq, n ))
