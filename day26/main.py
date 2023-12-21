# number = range(1,5)
# new_list = [num+2 for num in number]
# print(new_list)

names = ["Dikshan","Kushal","Sakar","Raj","Satya","Anish","Ram"]
new_list = [name.upper() for name in names if len(name) > 4]
print(new_list)