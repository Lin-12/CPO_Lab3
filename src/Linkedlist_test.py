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
        a = l['from_list'](lst)

        def func(x):
            x = x +1
            return x

        self.assertEqual(l['to_list'](l['map'](a, func)), [2, 3, 4, 5, 6, 7])

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

    def test_Laziness(self):
        lst1 = []
        for e in Infinite_List(99):
           lst1.append(e)               # make a list,lst1=[0,1,2,...,98,99]
        L1 = List()
        List1 = L1['from_list'](lst1)

        # 1.test function test_head
        self.assertEqual(L1['head'](List1), 0)
        # 2.test function test_tail
        self.assertEqual(L1['tail'](List1), 99)
        # 3.test function test_length
        self.assertEqual(L1['length'](List1), 100)

        # 4.test function test_reduce
        lst2 = []
        for e in Infinite_List(9):
           lst2.append(e)               # make a list,lst2=[0,1,2,...,9]
        L2 = List()
        List2 = L2['from_list'](lst2)
        self.assertEqual(L2['reduce'](List2, lambda st, e: st + e, 0), 45)

        # 5.test function test_map
        lst3 = []
        for e in Infinite_List(5):
            lst3.append(e)           # make a list,lst3=[0,1,2,3,4,5]

        def func(x):
            x = x + 1
            return x
        L3 = List()
        a = L3['from_list'](lst3)
        self.assertEqual(L3['to_list'](L3['map'](a, func)), [1, 2, 3, 4, 5, 6])

        # 6.test function test_from_list_to_list_equality
        lst4 = []
        for e in Infinite_List(1000):
            lst4.append(e)
        L4 = List()
        self.assertEqual(L4['to_list'](L4['from_list'](lst4)), lst4)

        # 7.test function test_monoid_identity
        lst5 = []
        for e in Infinite_List(1000):
            lst5.append(e)
        L5 = List()
        l = L5['from_list'](lst5)
        self.assertEqual(L5['to_list'](L5['mconcat'](L5['empty'](), l)), L5['to_list'](l))

        # 8.test function test_mconcat
        lst6 = []
        for e in Infinite_List(1):
            lst6.append(e)              # make a list,lst6=[0,1]
        lst7 = []
        for e in Infinite_List(10):
            lst7.append(e)              # make a list,lst7=[0,1,2,....,9,10]
        L6 = List()
        a = L6['from_list'](lst6)
        b = L6['from_list'](lst7)
        c = L6['mconcat'](a, b)
        self.assertEqual(L6['head'](c), 0)
        self.assertEqual(L6['tail'](c), 10)
        self.assertEqual(L6['length'](c), 13)

        # 9.test function test_iter
        lst8 = []
        for e in Infinite_List(3):
            lst8.append(e)            # make a list,lst8=[0,1,2,3]
        L7 = List()
        list = L7['from_list'](lst8)
        tmp = []
        try:
            get_next = L7['iterator'](list)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(lst8, tmp)
        self.assertEqual(L7['to_list'](list), tmp)

if __name__ == '__main__':
    unittest.main()
