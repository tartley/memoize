#!/usr/bin/env python2.7

from string import ascii_letters
from unittest import TestCase, main

from memoize import memoize


class MemoizeTest(TestCase):

    def test_returns_correct_value(self):

        @memoize
        def mul(a, b):
            return a * b

        self.assertEqual(mul(7, 13), 91)


    def test_uses_cached_results(self):
        calls = []

        @memoize
        def counter():
            calls.append(1)
            return 12345

        self.assertEqual(counter(), 12345)
        self.assertEqual(counter(), 12345)
        self.assertEqual(len(calls), 1)


    def test_handles_kwargs(self):

        @memoize
        def distance2(x=0, y=0):
            return x*x + y*y

        self.assertEqual(distance2(x=3, y=4), 25)
        self.assertEqual(distance2(x=1, y=1), 2)


    def test_not_dependant_on_order_of_kwargs(self):
        calls = []

        @memoize
        def counter(**kwargs):
            calls.append(1)
        
        # TODO, change this to use simple iteration over all perms, and assert
        # the # expected total number of calls at the end, not inside the loops
        for index, first in enumerate(ascii_letters):
            for second in ascii_letters[index:]:
                forward = {first:0, second:0}
                reverse = {second:0, first:0}

                del calls[:]
                counter(**forward)
                counter(**reverse)
                self.assertEqual(len(calls), 1,
                    '%d for %s,%s' % (len(calls), first, second))


    def test_raises_on_mutable_args(self):
        @memoize
        def whatever(_):
            pass

        for mutable in [[], {}, set(), (1, 2, {})]:
            with self.assertRaises(TypeError):
                whatever({})



if __name__ == '__main__':
    main()

