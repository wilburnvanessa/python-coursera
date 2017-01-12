def find_repeats(s1, s2):
    '''(str, str) -> int

    Return the index of the second occurrence of s2 in s1.
    If s2 does not occur twice in s1, the expression should produce -1.
    Unlike str.count, you should allow overlapping occurrences of s2.
    
    >>> find_repeats('banana', 'ana')
    3
    >>> find_repeats('apple', 'p')
    2
    >>> find_repeats('peter', 'lass')
    -1
    '''

    return s1.find(s2, (s1.find(s2) +1))
    
    

##def common_chars(s1, s2):
##    '''(str, str) -> str
##
##    Return a new string containing all characters from s1 that
##    appear at leastonce in s2. The characters in the result
##    will appear in the same order asthey appear in s1.
##
##    >>> common_chars('abc', 'ad')
##    'a'
##    >>> common_chars('a', 'a')
##    'a' 
##    >>> common_chars('abb', 'ab')
##    'abb' 
##    >>> common_chars('abracadabra', 'ra')
##    'araaara'
##    '''
##
##    res = ''
##
##    for ch in s1:
##        if ch in s2:
##            res = res + ch
##        
##    return res
