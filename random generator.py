'''
Part 1
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
'''
'''
Part 2
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

# Expanded solution : I implemented a code that can solve for both parts using the same logic,that is converting a longer range to a shorter range or vice vers. It just needs to know the range of numbers it is converting from and the range of numbers it needs to convert to, for example from [1,2,3] to [4,5]. The ranges can start and end at any non-negative number.


from random import randint

# both range_in and range_out need to be in the format of (a,b), 'a' as the lower boundary and 'b' as the upper boundary. If you want to convert an already randomly generated integer 'n' that is between the lower and upper boundaries of range_in, set input_int=n
def random(range_in : tuple, range_out: tuple, input_int=None) -> float:
    if input_int:
        # checks if 'input_int' is in range
        if input_int < range_in[0] or input_int > range_in[1]:
            return "Integer not in range"
    else:
        input_int = randint(range_in[0], range_in[1])
    '''
    I wrote down many examples using different ranges and connecting the dots and finally come up with a formula, so explaining the functionality of the formula is not an easy task (at list through commenting), but the main idea is to divide range_out into equal parts, and the number of these parts is same as the number of numbers in range_in so that each number in range_in corresponds to a number in range_out
    '''
    return ((input_int - range_in[0])*((range_out[1]-range_out[0])/(range_in[1]-range_in[0]))) + range_out[0]


### Test code: ###
from time import sleep

while True:
    print(random((1,5), (1,7)))
    sleep(1)
