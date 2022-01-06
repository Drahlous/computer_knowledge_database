
# Arrays & Lists
my_int_array = [i+1 for i in range(0,9)]

print("\n---Full Array---")
print("my_int_array[:]")
print(my_int_array[:])

print("\n---First Item---")
print("my_int_array[0]")
print(my_int_array[0])

print("\n---Last item---")
print("my_int_array[-1]")
print(my_int_array[-1])

print("\n---First two---")
print("my_int_array[:2]")
print(my_int_array[:2])

print("\n---Last two---")
print("my_int_array[-2:]")
print(my_int_array[-2:])

print("\n--Sliding Window---")
print("[print(my_int_array[x:x+2]) for x, _val in enumerate(my_int_array[:-1])]")
width = 2
[print(my_int_array[x:x+width]) for x, _val in enumerate(my_int_array[:-width])]


# MultiDimensional Arrays
print("\n===Multidimensional Arrays===")
my_int_matrix = [
        [0,1,2],
        [3,4,5],
        [6,7,8]]

print("\n---Full Matrix---")
print("my_int_matrix")
print(my_int_matrix)

print("\n---Full Matrix (row-wise)---")
print("[print(row) for row in my_int_matrix[:]]")
[print(row) for row in my_int_matrix[:]]

print("\n---First Row---")
print("my_int_matrix[0]")
print(my_int_matrix[0])

print("\n---Flatten Matrix---")
print("[col for row in my_int_matrix for col in row]")
print([col for row in my_int_matrix for col in row])

print("\n---Build matrix from list---")
num_rows = 3
num_columns = 3
print("[[x for x in range(offset,offset + num_columns)] for offset in range(0, num_rows*num_columns, num_columns)])")
print([[x for x in range(offset,offset + num_columns)] for offset in range(0, num_rows*num_columns, num_columns)])

print("\n---2x2 Window---")
top = 0
left = 0
height = 2
width = 2
print("[[x for x in row[left : left+width]] for row in my_int_matrix[top:left+height]]")
print([[x for x in row[left : left+width]] for row in my_int_matrix[top:left+height]])

print("\n---2x2 Sliding Right---")
print("[[[x for x in row[left : left+width]] for row in my_int_matrix[top:top+height]] for left in range(len(my_int_matrix[0]) - width + 1)]")
print([[[x for x in row[left : left+width]] for row in my_int_matrix[top:top+height]] for left in range(len(my_int_matrix[0]) - width + 1)])

print("\n---2x2 Sliding Down---")
print("[[[x for x in row[left : left+width]] for row in my_int_matrix[top:top+height]] for top in range(len(my_int_matrix[0]) - height + 1)]")
print([[[x for x in row[left : left+width]] for row in my_int_matrix[top:top+height]] for top in range(len(my_int_matrix) - height + 1)])


combs = []
for x in [1,2,3]:
    for y in ["a","b","c"]:
        combs.append((x,y))
print(combs)

combs = [(x,y) for x in [1,2,3] for y in ["a","b","c"]]
print(combs)

