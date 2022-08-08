#lists
names=["gagan","kittu","nandu","vijaya"]
#changing the name in given list
names[0]="kittu"
print(names) #by using index values we can print the names sepirately
print(names[2])#we can also select the range of values
print(names[0:3])
#note:these just create a new list but don't change the orginal list
#TYPES OF LISTS
# we can add the data into the list
numbers = [1,2,3,4,5,"gagan"]
numbers.append(9) # these function will add the data into the list
# which we have already given
print(numbers)
numbers.insert(0,-1)# these function will insert data in the list
# where we want to be inserted
print(numbers)
numbers.remove(5)# these function will remove the data into the list
print(numbers)
numbers.clear()
print(numbers)
print(1 in numbers)
#lists
lists = ["abcd",786,2.23,"jhon",70.2]
print(lists[0])
print(lists+numbers)
#lists
numbers=[1,2,3,4,5]
lists = ["abcd",786,2.23,"jhon",70.2]
print(lists[0])
print(lists+numbers)
print("list = "+str(lists*2))

import numpy

list1 = [1, 2, 3]
list2 = [3, 2, 4]

# using numpy.prod() to get the multiplications
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print(result1)
print(result2)


