test_list = ['gfg', 'is', 'best', 'for', 'geeksc']

# printing original list
print("The original list is : " + str(test_list))

# String with most unique characters
# using max() + dictionary comprehension
temp = {idx: len(set(idx)) for idx in test_list}
print(temp)
res = max(temp, key=temp.get)

# printing result
print("The string with most unique characters is : " + str(res))










