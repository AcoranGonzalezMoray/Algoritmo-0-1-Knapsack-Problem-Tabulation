from collections import namedtuple
from solve       import *
from ks_utils    import *
from my_tests    import *

Item = namedtuple("Item", ['index', 'value', 'weight'])

# Check my tests
tests = TestKSP()
# tests.test_from_data_to_item()
# tests.test_1() 
# ..                        	# Add more tests as you consider convenient
    
first_line = input().split() 	# N, Capacity
N          = int(first_line[0])
capacity   = int(first_line[1])

items = []
for i in range(1, N+1):
    parts = input().split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

value, taken = solve_tabulation(items, capacity)
print(value, taken)
