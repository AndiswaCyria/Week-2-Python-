#An empty list 
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

del my_list[7]

my_list.sort()
print("Sorted list:", my_list)

index_30 = my_list.index(30)

print("Index of 30:", index_30)

