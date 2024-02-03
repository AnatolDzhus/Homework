# number of each letter in text
# list_of_letters = list(input("enter text:"))
# number_of_letters = [list_of_letters.count(i) for i in list_of_letters]
# dictionary = {list_of_letters[i]: number_of_letters[i] for i in range(len(list_of_letters))}
# print(dictionary)
list_of_letters = list(input("enter text:"))
dictionary = {i: list_of_letters.count(i) for i in list_of_letters}
print(dictionary)
