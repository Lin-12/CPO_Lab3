## Computer Process Organization
### Lab3

#### Title:
  Computational Process Organization Lab3,variant 1

#### List of group members:
  - Name:Huang Yanlin,  student number:192050222 
  - Name:Lin ningning,  student number:192050192

#### Laboratory work number:
   Lab3 variant 1
#### Description:
   variant 1: In this variant, you should implement a lazy library for a single-linked list. For that, you should use closures. Usage of generators (yield statement) or async (async, await statements) is not allowed.

#### Synopsis:  
 implement the following API:
 
* head(List) – return a list first element. If the list is empty – raise an exception. 
* tail(List) – return tail of the list.
* length(List).
* map(List, Function) and reduce(List, Function, InitialState).
* mempty().
* mconcat(List1, List2) – should not force list evaluation.
* from_list(pythonList) and to_list(List).
* it should be an iterator.
* Complex test – factorial
   - To proof correctness, use unit tests, properties-based tests
   - To proof laziness,demonstrate it for all suitable implemented functions on an infinite list (e.g. natural numbers sequence) and a 

#### contribution
* contribution summary for each group member (should be checkable by git log and git blame);
   - Linkedlist:Huang Yanlin
   - Linkedlist_test:Lin ningning

#### Explanation：  
  we create a single-linked list and use closures.And we not use  generators (yield statement) or async (async, await statements).
  
#### Work demonstration 
* (how to use developed software, how to test it), should be repeatable by an instructor by given command-line examples:  
  - We write Linkedlist file and test file on Pycharm.
  - Use terminal to test the code. like 'python Linkedlist.py -v'and 'python Linkedlist_test.py -v'.

#### Conclusion:  
  We create a single-linked list and use closures.It's easy to see the test result.
  
 
