# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число
first=int(input("first: "))
action=input("action: ")
second=int(input("second: "))
if action =="+":
    print(first+second)
elif action =="-":
    print(first-second)
elif action =="*":
    print(first*second)
elif action =="/":
    print(first/second)
