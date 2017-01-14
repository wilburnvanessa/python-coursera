def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)
    

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    >>> is_longer('ATCG', 'TCGA')
    False
    """

    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)

    
def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

##    return dna1.find(dna2) != -1

    return dna1.find(dna2) >= 0

##def is_valid_sequence(pot_sequence)
    '''(str) -> bool

    Return True if and only if the DNA sequence
    is valid (that is, it contains no characters other
    than 'A', 'T', 'C' and 'G'). 

    >>> contains_sequence('ATCGGC')
    True
    >>> contains_sequence('ATCZQF')
    False
    >>> contains_sequence('ATCGgc')
    False
    '''

    
##    for char in pot_sequence:
##        if char ='ATCG'
##
##    return


##def insert_sequence
    '''(str, str, int) -> str

    Return

    >>>is_valid_sequence()
    
    '''
