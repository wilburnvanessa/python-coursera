


def averages(grades):

    '''
    (list of list of number) -> list of float)

    Return a new list in which each item is the average of
    the grades in the inner list at the corresponding position
    of grades.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [70, 75, 80], [70, 80, 90, 100], [80, 100]


    '''

    averages = []

    for grades_list in grades:
        #calculate the averages of grades_list and append it
        # to averages.

        total = 0
        for mark in grades_list:
            total = total + mark
        averages.append(total / len(grades_list))

    return averages


    
    

##LiF
##LiCl
##LiBr
##NaF
##NaCl
##NaBr


def calculate_average(asn_gradess):


    total = 0

    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)



def count_matches(s1, s2):
    ''' (str, str) -> int

    Return the number of positions in s1 that contain the
    same character at the corresponding position of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>>> count_matches('head', 'hard')
    2
    '''

    num_matches = 0count_matches('ate', 'ape')

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches
    


def sum_items(list1, list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the items at the
    corresponding position of list 1 and list2.
    
    '''

    sum_list = []

    for i in range(len(list1)):
            sum_list.append(list1[i] + list2[i])

    return sum_list



    
