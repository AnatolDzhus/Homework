# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
a={"Country1":["City1","City11","City111"],"Country2":["City2","City22","City222"]}
city=input("City: ")
country=[key for key,value in a.items() if city in value]
print(country)
