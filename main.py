#!
# -*- coding: utf-8 -*-

""" Own implementation of xrange, zip and """


def own_xrange(*args):
    """
    Own realization of xrange() function.
    :return: iterator of sequence from begin to end.
    """

    result = []
    if len(args) == 1:
        begin = 0
        end = args[0]
        step = 1
    elif len(args) == 2:
        begin = args[0]
        end = args[1]
        step = 1
    elif len(args) == 3:
        begin = args[0]
        end = args[1]
        step = args[2]
    else:
        raise TypeError('own_xrange() except 1 or 3 arguments')

    try:
        begin = int(begin)
        end = int(end)
        step = int(step)
    except ValueError:
        raise ValueError('need integer arguments')

    if step == 0:
        raise ValueError('step not be zero')
    elif step < 0:
        begin, end = end, begin
        num = end
    else:
        num = begin
    count = begin
    while count < end:
        result.append(num)
        num += step
        count += 1
    return iter(result)


def own_zip(*progr):
    """
    Own realization of zip() function.

    :param progr: one or more sequence -> [1, 2], [3, 4]
    :return: list with nested tuple -> [(1,3), (2,4)]
    """

    try:
        min_len = min(len(prg) for prg in progr)
        result = [tuple(prg[i] for prg in progr) for i in range(min_len)]
    except ValueError:
        result = []
    return result


def reverse_items(dictionary):
    """
    Swaps key and value in dictionary.
    :param dictionary: dict {key: value}
    :return: new dict {value: key}
    """

    try:
        result = {value: key for key, value in dictionary.items()}
    except TypeError:
        raise TypeError('key must be unchangeable type')
    return result


if __name__ == '__main__':

    print own_xrange(3)
    print own_zip([2, 3], [4, 5])
    print reverse_items({1: '1'})
