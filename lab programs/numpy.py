import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

#Basic operations
print("Array a:",a)
print("Array b:",b)
print("Sum of the arrays a and b:",np.add(a,b))
print("Difference of the arrays a and b:",np.subtract(a,b))
print("product of the arrays a and b:",np.multiply(a,b))
print("division of the arrays a and b:",np.divide(a,b))
print("Square root of the arrays a:",np.sqrt(a))
print("Exponential of the arrays a:",np.exp(a))

#Aggregation operations
print("Minimum of array a:",np.min(a))
print("Maximum of array b:",np.max(b))
print("Mean of array a:",np.mean(a))
print("Standard deviation of array a:",np.std(b))
print("Sum of all elements in array a:",np.sum(a))

#reshaping arrays
c=np.array([[1,2],[3,4],[5,6]])
print("array c:",c)
print("Reshaped array c(2 rows,3 columns):",np.reshape(c,(2,3)))

#transposing arrays
d=np.array([[1,2,3],[4,5,6]])
print("array d:",d)
print("Trnsposed array d:",np.transpose(d))
