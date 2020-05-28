import unittest

from hypothesis import given
import hypothesis.strategies as st
from Linkedlist import *


class TestLinklist(unittest.TestCase):
    def test_len(self):
        lst = [1, 2, 3, 4, 5, 6]
        l = List()
        self.assertEqual(l['length'](l['from_list'](lst)), 6)

    def test_map(self):
        lst = [1, 2, 3, 4, 5, 6]
        l = List()
        h = l['from_list'](lst)

        def func(a):
            a = a +1
            return a

        self.assertEqual(l['to_list'](l['map'](h, func)), [2, 3, 4, 5, 6, 7])

    def test_reduce(self):
        lst = [1, 2, 3, 4, 5, 6]
        l = List()
        s = l['from_list'](lst)
        self.assertEqual(l['reduce'](s, lambda st, e: st + e, 0), 21)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        l = List()
        self.assertEqual(l['to_list'](l['from_list'](a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        l = List()
        a = l['from_list'](lst)
        self.assertEqual(l['to_list'](l['mconcat'](a, l['empty']())), l['to_list'](a))
        self.assertEqual(l['to_list'](l['mconcat'](l['empty'](), a)), l['to_list'](a))

    def test_head(self):
        lst = ['a', 'b', 'c', 'd']
        l = List()
        root = l['from_list'](lst)
        self.assertEqual(l['head'](root), 'a')
        root = root.next
        self.assertEqual(l['head'](root), 'b')

    def test_tail(self):
        lst = ['a', 'b', 'c', 'd']
        l = List()
        self.assertEqual(l['tail'](l['from_list'](lst)), 'd')

    def test_mconcat(self):
        l1 = ['a']
        l2 = ['b']
        lst = List()
        h1 = lst['from_list'](l1)
        h2 = lst['from_list'](l2)
        c = lst['mconcat'](h1, h2)
        self.assertEqual(lst['to_list'](c), ['a', 'b'])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]

        for e in test_data:
            l = List()
            l2 = l['from_list'](e)
            self.assertEqual(l['to_list'](l2), e)

    def test_to_list(self):
        l = List()
        self.assertEqual(l['to_list'](Node('a')), ['a'])
        self.assertEqual(l['to_list'](Node('a', Node('b'))), ['a', 'b'])

    def test_iter(self):
        x = [1, 2, 3]
        l = List()
        l1 = l['from_list'](x)
        tmp = []
        try:
            get_next = l['iterator'](l1)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(l['to_list'](l1), tmp)



if __name__ == '__main__':
    unittest.main()
