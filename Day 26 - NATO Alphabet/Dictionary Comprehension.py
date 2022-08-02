#Example 1
square_dict = {number:number*number for number in range(1, 11)}

print(square_dict)

#Example 2
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76

new_price = {item:value*dollar_to_pound for item, value in old_price.items()}

print(new_price)

#Single Conditional
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {item: value for item, value in original_dict.items() if value % 2 == 0}

print(even_dict)

#Multiple Conditionals
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {item: value for item, value in original_dict.items() if value % 2 != 0 if value < 40}

print(new_dict)