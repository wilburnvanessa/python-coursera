


def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

    print(increment_items(values, 2))
    print(values)


def muta():

    a = [1, 2, 3]
    b = [1, 2, 3]

    a[1] = 'A'

    print(a, b)

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''

    while playlist.count(song) >= 3:
        playlist.remove(song)
        

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total


def while_version(L):
    """ (list of number) -> number

    >>> while_version(L)
    9


    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
         i = i + 1

    return total


def sum_of_evens(first, last):
    ''' (int, int) -> int

    Return the sum of the even numbers from 524 through
    10508, inclusive. Use a while loop to accumulate
    the sum and print it. The first number of the list is the start
    number and the second number of the list is the last number. 

    >>> sum_of_evens(2, 10)
    2+4+6+8+10=30
    >>> sum_of_evens(524, 10508)
    ???
    '''
    
    i = first
    result = 0
    
    while i <= last:
        result = result + i
        i = i + 2

    return result
        
    
    

def compress_list(L):
    ''' (list of str) -> list of str

    Return a new list with adjacent pairs of string elements from
    Lconcatenated together, starting with indices 0 and 1,
    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    >>> compress_list(['a', 'b', 'c', 'd', 'e', 'f'])
    ['ab', 'cd', 'ef']
    >>> compress_list(['a', 'b', 'c', 'd', 'e'])
    IndexError
    '''
    
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list


def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result




def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result
