# Вывести первые N цисел кратные M и больше K

n = int(input("enter N: "))
m = int(input("enter M: "))
k = int(input("enter K: "))
i = 0
while n > i:
    if (k + 1) % m == 0:
        print(k + 1)
        i = i + 1
        k = k + 1
    else:
        k = k + 1
        continue
