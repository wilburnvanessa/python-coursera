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

def is_valid_sequence(pot_sequence):
    '''(str) -> bool

    Return True if and only if the DNA sequence
    is valid (that is, it contains no characters other
    than 'A', 'T', 'C' and 'G'). 

    >>> is_valid_sequence('TCGGC')
    True
    >>> is_valid_sequence('ATCZQF')
    False
    >>> is_valid_sequence('ATCGgc')
    False
    '''

    valid = True
    
    for char in pot_sequence:
        if char != 'A' and char != 'C' and char != 'G' and char != 'T':
            valid = False
        
    return valid
        
    
##    thought experiments: 
##    return ('Q' or 'W' or 'E' or 'R' or 'Y' or 'U' or 'I' or 'O' or 'P' or 'S' or 'D' or 'H' or 'J' or 'K' or'L' or 'Z' or 'X' or 'V' or 'B' or 'N' or 'M') in pot_sequence
##      

##    if ('Q' or 'W' or 'E' or 'R' or 'Y' or 'U' or 'I' or 'O' or 'P' or 'S' or 'D' or 'H' or 'J' or 'K' or'L' or 'Z' or 'X' or 'V' or 'B' or 'N' or 'M') in pot_sequence:
##        pot_sequence = False
        
##    else:
##         pot_sequence = True

##    return ('A' or 'T' or 'C' or 'G') in pot_sequence

    
##    for char in pot_sequence:
##        if char ='ATCG'
##
##    return


def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str

    Return the DNA sequence obtained
    by inserting the second DNA sequence into the first DNA
    sequence at the given index. The first two parameters are
    DNA sequences and the
    third parameter is an index. (You can assume that the
    index is valid.) When coming up with more examples, think about
    where the second DNA sequence might be inserted: what are the extremes?

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('TCC', 'GGGG' , 0)
    'GGGGTCC'
    >>> insert_sequence('TCC', 'GGGG', 6)
    'TCCGGGG'
    '''

    return dna1[:index] + dna2 + dna1[index:]
    
## s[:5] + 'ed' + s[5:]
## learn + ed to program

def get_complement(nuc):
    '''(str) -> str

    The first parameter is a nucleotide ('A', 'T', 'C' or 'G').
    Return the nucleotide's complement. We have intentionally
    not given you any examples for this function. The
    Problem Domain section explains what a nucleotide is
    and what a complement is.

    >>> get_complement()
    
    '''


def get_complementary_sequence(seq):
    '''(str) -> str

    The parameter is a DNA sequence. Return the
    DNA sequence that is complementary to the
    given DNA sequence. For example, if you call this
    function with 'AT' as the argument, it should return 'TA'.

    >>> get_complementary_sequence()
    '''
