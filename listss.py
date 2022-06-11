
list_of_item = [1,1,1,2,3,3]
y = [x for x in list_of_item if list_of_item.count(x)>1]
final_list = list(dict.fromkeys(y))
print(final_list)