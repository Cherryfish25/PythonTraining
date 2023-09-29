MyList = [1, 2, 3, 4, 5, 6, 9, 10, 15, 100, 90, 80]

even = []
NotEven = []
outlier = []

for item in MyList:
    if item%2 == 0:
        even.append(item)
    else:
        NotEven.append(item)
print("Even numbers " , even)
print("Odd numbers" , NotEven)
print("outliers" , outlier)

    #Out:
    #Even numbers [2, 4, 6, 10, 90, 80]
    #Odd numbers [1, 3, 5, 9, 15]
    #outliers [100]

num_sum = 0

for item in MyList:
    num_sum += item

print("Sum of the elements in the list" , num_sum)

#Out:
#Sum of the elements in the list 330

# step 1: find the even numbers
even = []

for item in MyList:
    if item%2 == 0:
        even.append(item)
# step 2: add all items in even list
sum_num = 0

for item in even:
    sum_num +=item
print("The sum of even numbers" , sum_num)

# Out:
#The sum of even numbers 260

count = 0

for item in range(len(MyList)):
        if MyList[item]%2==0:
           count +=1
print('The count of even numbers in the list', count)

#Out:
#The count of even numbers in the list 8

initial_val = 0
cumsum = []
for item in MyList:
    initial_val += item
    cumsum.append(initial_val)

print('The cummulative sum of the list', cumsum)

#Out:
#The cummulative sum of the list [1, 2, 3, 4, 5, 6, 9, 10, 15, 80, 90, 100]



