#1
lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for item in lst:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

#3
lst = [10, 20, 30, 40, 20]
unique_lst = list(set(lst))
unique_lst.sort()

print("Second Largest:", unique_lst[-2])

#4
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8]]

for inner_list in nested_list:
    print("Sum:", sum(inner_list))

#5
import copy

lst1 = [[1, 2], [3, 4]]
shallow = copy.copy(lst1)

shallow[0][0] = 99

print("Original:", lst1)
print("Shallow:", shallow)

  #deep copy
deep = copy.deepcopy(lst1)

deep[0][0] = 10

print("Original:", lst1)
print("Deep:", deep)

