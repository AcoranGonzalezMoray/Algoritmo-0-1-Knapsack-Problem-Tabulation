from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

# Routine used in my_tests.py to read input-data from a string!
def from_data_to_items(input_data):
    lines = input_data.split('\n')

    first_line = lines[0].split()
    N          = int(first_line[0])
    capacity   = int(first_line[1])

    items = []
    for i in range(1, N + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i, int(parts[0]), int(parts[1])))

    return items, capacity
    
def total_weight(items, taken):
    weight = 0
    for item in items:
        if taken[item.index]== 1:
            weight += item.weight
    return weight
