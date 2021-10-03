# Find odd number of the list and create new list of odd numbers
list1 = [1,2,4,5,6,56,32,424,32,15,71,57]
odd_num_list = []
for num in list1:
    if num%2 != 0:
        odd_num_list.append(num)
print(odd_num_list)
