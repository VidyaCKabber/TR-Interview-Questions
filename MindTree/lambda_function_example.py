# Find even number of the using lambda function
list1 = [1,2,4,5,6,56,32,424,32,15,71,57]
even_num_list = list(filter(lambda x : x%2 == 0 , list1))
print(even_num_list)
