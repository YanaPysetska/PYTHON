# Sort the integers in sequence. But the position of zeros should not be changed.
# Input: List of integers (int).
# Output: List or another Iterable (tuple, generator, iterator) of integers (int).

def except_zero(items: list[int]):
    zero=[]
    for i, name in enumerate(items):
        if name==0:
            zero.append(i)
    my_sorted_values=sorted([i for i in items if i != 0])
    for i in zero:
        my_sorted_values.insert(i, 0)
    return my_sorted_values

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
