listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

#Index() Method which finds the index of an element in the list
listOne.index('b')#1
listTwo.index('g')#2

#Append() Methhod which adds an element to the end of the list

currencies = ['Dollar', 'Euro', 'Pound']
currencies.append('Yen')
currencies.append('UGX')

#Extend() This methods adds an iterable(String, tupple,list) to the end of the list..

listOne.extend(listTwo)
print(listOne)


#Insert() This method inserts an element at a specifieced index or numrrical position.
fruits = ['Appales','Grapes','Tomatoes']
fruits.insert(2,'Oranges')


#Remove() This method removes an element from the list

# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.remove(9)

#Count() This methods returns the number an element appears in the list
# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]

print(numbers.count(2))

#Pop() This methods removes an element from the list at a specified position.
list_num = [2,4,6,8,0,12,4,67,50]
list_num.pop(0)

#The reverse() method reverses the elements of the list.
list_numx = [2,4,6,8,0,12,4,67,50]
#print(list_numx)
list_numx.reverse()
#print(list_numx)

#The sort() method sorts the elements of a given list in a specific ascending or descending order.

list_num_sort = [2,4,6,8,0,12,4,67,50]
print(list_num_sort)
list_num_sort.sort(reverse=True) #Sorts it to the decendeing order
print(list_num_sort)


#The copy() method returns a shallow copy of the list.

x = ['Chelsea','Arsenal','Man u','Liverpool']
y = x.copy()

print('The Copied List : ', y)

#The clear() method removes all items from the list.

xx = ['Chelsea','Arsenal','Man u','Liverpool']
yx = xx.clear()

print('The Copied List : ', yx)
