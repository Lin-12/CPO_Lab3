import unittest
from hypothesis import given
import hypothesis.strategies as st
from Linkedlist import *

class TestLinkedlist(unittest.TestCase):
    # test function of length
    @given(st.lists(st.integers()))
    def test_length(self, l):
        lst = from_list(l)
        self.assertEqual(length(lst), len(l))
        self.assertEqual(length(None), 0)
        self.assertEqual(length(con(1, None)), 1)
        self.assertEqual(length(con(1, con(2, con(3, con(4, None))))), 4)

    # test function of map
    def test_map(self):
        self.assertEqual(map(None, str), None)
        self.assertEqual(to_list(map(con(1, con(2, con(3, con(4, None)))), str)),
                         to_list(con('1', con('2', con('3', con('4', None))))))
        self.assertEqual(to_list(map(con(1, con(2, con(3, con(4, None)))), lambda x: x * x)),
                         to_list(con(1, con(4, con(9, con(16, None))))))

    # test function of reduce
    def test_reduce(self):
        self.assertEqual(reduce(None, lambda st, e: st + e, 0), 0)
        self.assertEqual(reduce(con(1, con(2, con(3, con(4, None)))), lambda st, _: st + 1, 0), 4)
        self.assertEqual(reduce(con(1, con(2, con(3, con(4,None)))), lambda st, e: st + e, 0), 10)

    # test function of empty
    def test_empty(self):
        self.assertEqual(empty(), None)

    # test function of concat
    def test_concat(self):
        self.assertEqual(concat(None, None), None)
        self.assertEqual(to_list(concat(con(1, None), None)), to_list(con(1, None)))
        self.assertEqual(to_list(concat(None, con('1', None))), to_list(con('1', None)))
        self.assertEqual(to_list(concat(con('1', None), con('2', con('3', None)))), to_list(con('1', con('2', con('3', None)))))

    # test function of head
    def test_head(self):
        self.assertRaises(AssertionError, lambda: head(None))
        self.assertEqual(head(con(1, None)), 1)
        self.assertEqual(head(con('a', None)), 'a')
        self.assertEqual(head(con(1, con(2, con(3, con(4,None))))), 1)

    # test function of tail_e
    def test_tail(self):
        self.assertRaises(AssertionError, lambda: tail_e(None))
        self.assertEqual(tail_e(con('a', None)), 'a')
        self.assertEqual(tail_e(con('a', con('b', con('c', None)))), 'c')
        self.assertEqual(tail_e(con(1, None)), 1)
        self.assertEqual(tail_e(con(1, con(2, con(3, con(4, None))))), 4)

    # test function of from_list
    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]

        for e in test_data:
            l = from_list(e)
            self.assertEqual(to_list(l), e)

    # test function of to_list
    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(con('a', None)), ['a'])
        self.assertEqual(to_list(con('a', con('b', None))), ['a', 'b'])

    @given(st.lists(st.integers()))
    def test_from_list_to_list(self, l):
        self.assertEqual(to_list(from_list(l)), l)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, l):
        self.assertEqual(to_list(concat(empty(), from_list(l))),
                         to_list(from_list(l)))
        self.assertEqual(to_list(concat(from_list(l), empty())),
                         to_list(from_list(l)))
        self.assertEqual(to_list(concat(from_list(l), empty())),
                         to_list(concat(empty(), from_list(l))))

    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_monoid_associativity(self, l1, l2, l3):
        a = from_list(l1)
        b = from_list(l2)
        c = from_list(l3)
        self.assertEqual(to_list(concat(a, concat(b, c))), to_list(concat(concat(a, b), c)))

    def test_iter(self):
        x = [1, 2, 3]
        lst = from_list(x)
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

    @given(st.integers())
    def test_infinite_list(self, Limit):
        l1 = []
        for e in infinite_list(10):
            l1.append(e)
        lst1 = from_list(l1)
        self.assertEqual(head(lst1), 0)
        self.assertEqual(tail_e(lst1), 10)
        self.assertEqual(length(lst1), 11)
        if Limit < 100:
            lst = list(range(Limit, -1, -1))
            self.assertEqual(to_list(infinite_list(Limit)), lst)

    def test_infinite_list(self):
        def tmp_natural_seq(i):
            while True:
                yield i
                i += 1
        lst = []
        l1 = tmp_natural_seq(0)
        cur = from_generator(l1, 3)
        i = iterator(cur)
        while True:
            x = i()
            if len(lst) > 3: break
            lst.append(x)
        l = list(reversed(lst))
        self.assertEqual(l, [0, 1, 2, 3])

    @given(st.integers())
    def test_hofstadter_seq(self, idx):
        def tmp_hofstadter_seq(m):
            list1 = []
            list2 = []
            for i in range(m):
                if i == 0:
                    list1.append(0)
                    list2.append(1)
                else:
                    list1.append(i - list2[list1[i - 1]])
                    list2.append(i - list1[list2[i - 1]])
            return list1, list2
        if idx < 100:
            res1, res2 = hofstadter_seq(idx)
            res1 = to_list(res1)
            res2 = to_list(res2)
            list1, list2 = tmp_hofstadter_seq(idx)
            list1 = list(reversed(list1))
            list2 = list(reversed(list2))
            self.assertEqual(res1, list1)
            self.assertEqual(res2, list2)

if __name__ == '__main__':
    unittest.main()
