from inspect import isfunction

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Return the length of lst
def length(lst):
    if lst is None:
        return 0
    else:
        lst = lst()
        return 1 + length(lst.next)

# Utilize the f to map the LinkList.
def map(lst, f):
    if lst is None:
        return None
    else:
        lst = lst()
        tmp = f(lst.value)
        lst = lst.next
        return con(tmp, map(lst, f))


#  process structure elements to build a return value by specific functions
def reduce(lst, f, initial_state):
    state = initial_state
    if lst is not None:
        lst = lst()
        state = f(state, lst.value)
        lst = lst.next
        return reduce(lst, f, state)
    else:
        return state


# Return a empty list.
def empty():
    return None


# Connect two linked lists
def concat(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    tmp = reverse(l1)
    res = l2
    while tmp is not None:
        res = con(tmp.value, res)
        tmp = tmp.next
    return res


# return the first element
def head(lst):
    assert lst is not None
    lst = lst()
    assert type(lst) is Node
    return lst.value


# return the last element
def tail_e(lst):
    assert lst is not None
    lst = lst()
    assert type(lst) is Node
    if lst.next is not None:
        lst = lst.next
        return tail_e(lst)
    return lst.value


# Reverse the linkedlist
def reverse(lst, e=None):
    def tail(lst):
        lst = lst()
        assert type(lst) is Node
        return lst.next

    if lst is None:
        return e
    return reverse(tail(lst), Node(head(lst), e))


# Make a list to be LinkList
def from_list(lst):
    res = None
    if len(lst) == 0:
        return None
    for e in reversed(lst):
        res = con(e, res)
    return res


# make LinkList be a list
def to_list(lst):
    res = []
    if lst:
        lst = lst()
    while lst is not None:
        res.append(lst.value)
        if lst.next is not None:
            lst = lst.next()
        else:
            lst = None
    return res


def con(head_, tail_):
    def A():
        return Node(head_, tail_)

    return A
# Infinitely generate element
def from_generator(lst):
    e = next(lst)
    return e

# Iterative structure.
def iterator(lst):
    cur = lst
    while isfunction(cur):
        cur = cur()

    def A():
        nonlocal cur
        if cur is None:
            raise StopIteration
        tmp = cur.value
        if cur.next:
            cur = cur.next()
        else:
            cur = cur.next
        return tmp

    return A

# Make a infinite list ,this list's elem can be created by elem +=1
def infinite_list(Limit):
    elem = 0
    lst = None
    while elem <= Limit:
        lst = con(elem, lst)
        elem += 1
    return lst

# Return no instantiated hofstadter_seq.
def hofstadter_seq(idx):
    n = 0
    res1 = None
    res2 = None
    while n < idx:
        if n == 0:
            res1 = con(0, res1)
            res2 = con(1, res2)
        else:
            tmp_res1 = res2()
            for _ in range(n - res1().value - 1):
                tmp_res1 = tmp_res1.next()
            tmp_value1 = n - tmp_res1.value
            tmp_res2 = res1()
            for _ in range(n - res2().value - 1):
                tmp_res2 = tmp_res2.next()
            tmp_value2 = n - tmp_res2.value
            res1 = con(tmp_value1, res1)
            res2 = con(tmp_value2, res2)
        n += 1
    return res1, res2



