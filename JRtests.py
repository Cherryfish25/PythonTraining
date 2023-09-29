

import numpy

from scipy import stats

import matplotlib.pyplot as plt

#Create the data set

#userInputs = input("Input your data, separated by commas: ")
#dataSet = userInputs.split(",")
dataSet = numpy.random.normal(10, 1, 100)
dataSet = [int(x) for x in dataSet]
print(dataSet)

#Determine our values

setMean = numpy.mean(dataSet)
setMedian = numpy.median(dataSet)
standDev = numpy.std(dataSet)
setVar = numpy.var(dataSet)
mostUsed = stats.mode(dataSet)

#Start printing

print("The mean is " + str(setMean))
print("The median is " + str(int(setMedian)))
print("the standard deviation is " + str(standDev))
print("The variance is " + str(setVar))
print("The most used number is :" + str(mostUsed))

#Graph the results

plt.hist(dataSet, 40)
plt.show()


