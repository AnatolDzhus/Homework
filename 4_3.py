first_value = input("enter first value:")
second_value = input("enter second value:")
n=int(input("enter n:"))
internal_dict = {"name":first_value, "email":second_value}
keys_for_external_dict=[i for i in range(n)]
total_dict={keys_for_external_dict[i]:internal_dict for i in range(len(keys_for_external_dict))}
print(total_dict)
