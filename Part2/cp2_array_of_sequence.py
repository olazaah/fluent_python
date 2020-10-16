# Container sequence such as list, tuple and collection.deque can hold items of differnt types

# Flat sequence as str, bytes, bytearray, memoryview and array.array hold items of one type

# Mutable sequence list, bytearray, array.array, collections.deque and memory view

# Immutable sequence

# tuple, str, and bytes

# Cartesian product using list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# Generator expressions

for tshirt in (f'{color} {size}' for color in colors for size in sizes):
    print(tshirt)


from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.156254, 77.2398327))
delhi = City._make(delhi_data)
print(delhi)
print(delhi.coordinates.lat)
print(delhi._asdict())

# tic tact toe

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)

wierd_board = [['_'] * 3] * 3
wierd_board[1][2] = 'X'
print(wierd_board)

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(fruits)
fruits.sort()
print(fruits)


# Bisect finds insertion points for items in a sorted sequence

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '    |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->   ', '   '.join('%2d' % n for n in HAYSTACK))
    demo(bisect.bisect_left)

# Given test score, grade returns the letter of the grade

def grade(score, breakpoint=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoint, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


# Inserting with bisect.insort

# insort keeps sorted sequence always sorted

import random

SIZE = 7
random.seed(1729)
my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)

from array import array

# floats = array('d', (random.random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()
# floats2 = array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**7)
# fp.close()
# print(floats2[-1])
# print(floats == floats2)


# MEMORY VIEW used for creating objects of large datasets and having access to the data without necessarily copying the details out of memory

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
print(memv_oct[5])
print(numbers)

# working with deque
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

"""
    SORTING ALGORITHMS
    Bubble Sort
    Insertion Sort
    Merge Sort
    python's list.sort() and sorted(list) use timsort (an adaptive sorting algorithm that switches from
    insertion sort to merge sort strategies)
"""


