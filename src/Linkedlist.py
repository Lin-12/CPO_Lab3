class Node(object):
    def __init__(self, value, next=None):
        """node constructor"""
        self.value = value
        self.next = next


def List(root1=None):
    root = root1

    # return the length of list
    def length(lst):
        res = 0
        while lst is not None:
            res = res + 1
            lst = lst.next
        return res

    # Utilize the f to map the LinkList
    def map(lst, f):
        curNode = lst
        while curNode is not None:
            curNode.value = f(curNode.value)
            curNode = curNode.next
        return lst

    # process structure elements to build a return value by specific functions
    def reduce(lst, f, initial_state):
        state = initial_state
        curNode = lst
        while curNode is not None:
            state = f(state, curNode.value)
            curNode = curNode.next
        return state

    # Make it empty and return None
    def empty():
        return None

    # return the first element
    def head(lst):
        if lst is None: raise Exception
        a = lst.value
        return a

    def head_node(node):
        assert type(node) is Node
        return node.value

    # return the last element
    def tail(lst):
        while lst.next is not None:
            lst = lst.next
        return lst.value

    def tail_node(node):
        assert type(node) is Node
        cur = node.next
        return cur

    def reverse(a, next_=None):
        if a is None:
            return next_
        return reverse(tail_node(a), Node(head_node(a), next_))

    # Make a list to be LinkList
    def from_list(lst):
        if len(lst) == 0:
            root = None
            return root
        root = None
        for elem in reversed(lst):
            root = Node(elem, root)
        return root

    # make LinkList be a list
    def to_list(root):
        res = []
        curNode = root
        while curNode is not None:
            res.append(curNode.value)
            curNode = curNode.next
        return res

    def con(l1, l2):
        return Node(l1, l2)

    # Connect two linked lists
    def mconcat(l1, l2):
        if l1 is None:
            return l2
        a = reverse(l1)
        b = l2
        while a is not None:
            b = con(a.value, b)
            a = a.next
        return b

    def iterator(lst):
        curNode = lst

        def A():
            nonlocal curNode
            if curNode is None: raise StopIteration
            elem = curNode.value
            curNode = curNode.next
            return elem

        return A

    return {
        'Node': Node,
        'length': length,
        'map': map,
        'reduce': reduce,
        'empty': empty,
        'head': head,
        'head_node': head_node,
        'tail_node': tail_node,
        'tail': tail,
        'reverse': reverse,
        'to_list': to_list,
        'from_list': from_list,
        'con': con,
        'mconcat': mconcat,
        'iterator': iterator,

    }
# Make a infinite list ,this list's elem can be created by def __next__
class Infinite_List(object):

    def __init__(self, Limit):
        self.Limit = Limit
        self.elem = -1
        self.len = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.elem < self.Limit:
            self.elem += 1
            self.len += 1
            return self.elem
        raise StopIteration()

