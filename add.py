# I'd like you to write a function that accepts two lists-of-lists 
# of numbers and returns one list-of-lists with each of the 
# corresponding numbers in the two given lists-of-lists added together.

def add(*matricies):
    """ Calculates elementwise sum of two or more 2D matricies.

        *matrix: tuple of matricies

        returns: list of lists (a matrix)
    """
    mat_shape = {
        tuple(len(x) for x in matrix) 
        for matrix in matricies
        }

    if len(mat_shape) > 1:
        raise ValueError('Given matricies are not the same size')

    element_sum = [
        [sum(m) for m in zip(*n)]  
        for n in zip(*matricies)
    ]
    return element_sum
