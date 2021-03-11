input_str = "abc de"
input_str1= "LuCiDPrograMMiNG"

vowels = "aeiou"
count = 0

def iterative_count_consonants(str):
    count = 0
    for item in str :
        if item.lower() not in vowels and item.isalpha():
            count = count + 1
    return count

#print(iterative_count_consonants(input_str1))


def recursive_count_consonants(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


print(recursive_count_consonants(input_str1))

