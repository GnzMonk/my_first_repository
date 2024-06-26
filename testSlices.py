my_list = [1, 2, 4, 5, 8, 9]

print(list(reversed(my_list)))
print(my_list)

dict1 = {'a': 1, 'b': 2} # Объединение двух словарей 
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}
print(dict3)        	# {'a': 1, 'c': 3, 'b': 2, 'd': 4}