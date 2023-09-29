# Fibonacci Sequence

fibonacciSequence = [0,1]

while len(fibonacciSequence) < 11:
    lastNumber = fibonacciSequence[-2] + fibonacciSequence[-1]
    fibonacciSequence.append(lastNumber)

print(fibonacciSequence)







