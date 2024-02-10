# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def decimal_to_binar(dec):
    numbers = []
    def dec_to_bin(dec):
        if dec//2 >0:
            a=dec//2
            b=dec%2
            numbers.append(b)
            return dec_to_bin(a)
        elif dec==1:
            numbers.append(1)
        elif dec==0:
            numbers.append(0)
        numbers.reverse()
        for i in numbers:
            print(i,end="")
        print()
    dec_to_bin(dec)
def binar_to_decimal(_bin):
    list_of_numbers=[]
    while _bin//10>0:
        b = _bin % 10
        _bin=_bin//10
        list_of_numbers.append(b)
    list_of_numbers.append(_bin)
    sum=0
    list_of_numbers.reverse()
    for i in range(len(list_of_numbers)):
        sum=sum+list_of_numbers[i]*pow(2,len(list_of_numbers)-i-1)
    print(sum)
decimal_to_binar(17)
binar_to_decimal(10001)
