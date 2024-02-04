#Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
n=int(input("enter n:"))
list_of_names=[input("name: ") for i in range(3)]
list_of_emails=[input("email: ")for i in range(n)]
dictionary={i:{"name":list_of_names[i],"email":list_of_emails[i]} for i in range(n)}
print(dictionary)




