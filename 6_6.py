# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
a=[1,2,3,4,5,6,7,8,9]
a=list(filter(lambda x: x%2==0,a))+list(filter(lambda x: x%2,a))
print(a)