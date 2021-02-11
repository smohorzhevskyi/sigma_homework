from random import randint
from datetime import datetime


G1 = sorted([randint(0, 100) for i in range(1000)])
G2 = sorted([randint(0, 100) for i in range(10000)])
G3 = sorted([randint(0, 100) for i in range(100000)])
M1 = [randint(0, 100) for i in range(1000)]
M2 = [randint(0, 100) for i in range(10000)]
M3 = [randint(0, 100) for i in range(100000)]
W1 = sorted([randint(0, 100) for i in range(1000)], reverse=True)
W2 = sorted([randint(0, 100) for i in range(10000)], reverse=True)
W3 = sorted([randint(0, 100) for i in range(100000)], reverse=True)

"""СОРТУВАННЯ МЕТОДОМ ВИБОРУ"""


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums

before = datetime.now()
selection_sort(G1)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(G2)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(G3)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(M1)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(M2)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(M3)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(W1)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(W2)
after = datetime.now()
print(after - before)

before = datetime.now()
selection_sort(W3)
after = datetime.now()
print(after - before)
print("__")

"""СОРТУВАННЯ МЕТОДОМ ЗЛИТТЯ"""


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


before = datetime.now()
merge_sort(G1)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(G2)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(G3)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(M1)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(M2)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(M3)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(W1)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(W2)
after = datetime.now()
print(after - before)

before = datetime.now()
merge_sort(W3)
after = datetime.now()
print(after - before)
print("__")

"""СОРТУВАННЯ МЕТОДОМ ПІДРАХУНКУ"""


def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m
    for a in array1:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1
    return array1


before = datetime.now()
counting_sort(G1, max(G1))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(G2, max(G2))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(G3, max(G3))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(M1, max(M1))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(M2, max(M2))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(M3, max(M3))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(W1, max(W1))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(W2, max(W2))
after = datetime.now()
print(after - before)

before = datetime.now()
counting_sort(W3, max(W3))
after = datetime.now()
print(after - before)
print("__")