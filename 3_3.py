name = input('name:')
city = input('city:')
age = input('age:')
print(f'My name is {name}. I live in {city}. I\'m {age}')
print('My name is {name}. I live in {city}. I\'m {age}'.format(name=name, city=city, age=age))
print('My name is %(name)s. I live in %(city)s. I\'m %(age)s'%{"name":name, "city":city,"age":age})

