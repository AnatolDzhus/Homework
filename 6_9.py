# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
data = {"id1": {"name": "name1", "surname": "surname1", "number": 1, "mail": "mail1"},
        "id2": {"name": "name2", "surname": "surname2", "number": 2, "mail": "mail2"},
        "id3": {"name": "name3", "surname": "surname3", "number": 3, "mail": ""},
        "id4": {"name": "name4", "surname": "surname4", "number": 4}}
a = list(filter(lambda x: "mail" not in x or not x["mail"], data.values()))
name = [i["name"] for i in a]
print(name)
