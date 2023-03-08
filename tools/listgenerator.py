def listgenerator(row: int, col:int, rangelow=0, rangehigh=10, randtype='int'):
    """
    Generates a matrix with each element generated randomly between high range and low range.

    :row: - number of rows in the matrix\n
    :col: - number of columns in the matrix\n
    :rangelow: - the least possible number that can be generated\n
    :rangehigh: - the most possible number that can be generated\n
    :randtype: - the type of generated numbers. It is set to integer by default, but it can be set to float as well.
    """

    from random import randint, random
    if randtype == 'int':
        return [[randint(rangelow, rangehigh) for j in range(col)] for i in range(row)]
    elif randtype == 'float':
        """
        random() generated float numbers ranging between 0 to 1.
        In order to generate float numbers ranging between two arbitrary
        boundries, the following equation is used:
        number = (low range) + ((high range - low range)* random())
        """
        return [[(rangelow + ((rangehigh-rangelow)*random())) for j in range(col)] for i in range(row)]
    else:
        raise Exception(f"Type \"{randtype}\" not supported")