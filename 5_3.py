#Вывести четные числа от 2 до N по 5 в строку
n=int(input("enter N: "))
list_of_numbers=[i for i in range(2,n,2)]
while len(list_of_numbers)>0:
    if len(list_of_numbers)>5:
        for j in range(5):
            print(list_of_numbers[j],end=" ")
        print("")
        del list_of_numbers[0:5]

    else:
        print(list_of_numbers[0],end=" ")
        del list_of_numbers[0]


