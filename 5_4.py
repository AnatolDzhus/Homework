# Пользователь вводит химическую формулу (элементы однобуквенныe и формула без скобок)
# Подсчитать количество атомов
# input: C2H5OH
# output: {"C": 2, "H": 6, "O": 1}
formula="c2h5ohpf"
new_formula=[]
new_formula=[i for i in len(formula) if (formula[i].isnumeric())]
#     print(i)
print(formula)
print(new_formula)
