#!
# -*- coding: utf-8 -*-

""" Testing own functions zip(), xrange() and """

from main import own_zip, own_xrange, reverse_items


class Test:
    """
    Test of own function zip(), xrange()
    and reverse_item().
    """

    # Test own_zip()
    def test_empty(self):
        assert own_zip() == []

    def test_one_seq(self):
        a = [1, 2, 3]
        assert own_zip(a) == [(1,), (2,), (3,)]

    def test_two_seq(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        assert own_zip(a, b) == [(1, 4), (2, 5), (3, 6)]

    def test_various_seq(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = [7, 8, 9, 10]
        d = [i for i in range(15)]
        result = [(1, 4, 7, 0), (2, 5, 8, 1), (3, 6, 9, 2)]
        assert own_zip(a, b, c, d) == result

    def test_str(self):
        assert own_zip('a') == [('a',)]

    # Test own_xrange()
    def test_one(self):
        assert list(own_xrange(3)) == [0, 1, 2]

    def test_two(self):
        assert list(own_xrange(0, 3)) == [0, 1, 2]

    def test_three(self):
        assert list(own_xrange(3, 0, -1)) == [3, 2, 1]

    # Test reverse_items()
    def test_change(self):
        d = {'key': 'value'}
        assert reverse_items(d) == {'value': 'key'}


if __name__ == '__main__':
    pass
