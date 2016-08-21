__author__ = 'srikanta'
'''
A Simple Async handler to execute a function and handle its callback with another function.
'''
from itertools import permutations
from random import randint


def async_handler(input_func, args, callback_function):
    '''
    Acts as simple async handling function.
    :param input_func: 
    :param args: 
    :param callback_function: 
    :return:
    '''
    result = input_func(args)
    callback_function(result)


def compute_permutations(input):
    return permutations(input)


def print_permutations(result):
    print [i for i in result]


for i in xrange(10):
    p_ip = str(randint(0, 10 ** 5))
    async_handler(compute_permutations, (p_ip), print_permutations)
