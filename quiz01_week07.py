
def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah' , 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True
            
    return found


def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of     that fruit.

    REST OF DESCRIPTION MISSING HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate



##def quiz8(d):
##    
##    total = 0
##    for k in d:
##        total = total + k
##
##
##print(quiz8({1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}))
##
