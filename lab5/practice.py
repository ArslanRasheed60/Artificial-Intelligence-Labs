import  numpy as np
import pandas as pd
a = np.array([1,2,4])
# print(a)
a = np.zeros((3,3))
# print(a)
a = np.ones((2,2))
# print(a)
a = np.eye(3)
# print(a)
a = np.full((4,4),3)
# print(a)
a = np.random.random((3,4))
# print(a)
a = np.arange(5,25,3)
# print(a)
a = np.linspace(0,2,7)
a = np.empty((3,2))
# print(a)

# Attributes of array object
a=np.array([[1,2,3],[5,1,2]])#
# print(type(a))#
# print(type(a.shape))#
# print(type(a.ndim))
# print(type(a.size))


#Array slicing
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[:2,1:3]     #shallow copy   -> reference based
# print(a[0,1], a[0][1])  #same result

a = np.arange(5)**3
b = a[::-1]
# print(a[a>4])
# print(a, b)

#operators
x=np.array([[1,2],
            [3,4]],dtype=np.float64)
y=np.array([[5,6],
            [7,8]],dtype=np.float64)
# print(x+y)
# print(np.add(x,y))
# print(np.sqrt(x))
# print(x @ y)
# print(x.flatten())
# print(x.sum(axis=0))
# print(x.cumsum(axis=1))
# print(x.min())
# print(x.max())
# print(np.exp(x))
# print(x.T)


s = pd.Series([1,2,4], index=['A','B','C'])
# print(s)
data = {'a': [1,2,4],'b': [7,8,9]}
s = pd.DataFrame([[1,2],[9,5]], index=['a','b'], columns=['x','y'])
y = pd.DataFrame(data)
print(s)
# print(s.loc['b'])
# print(s.iloc[0])

print(s.sort_values(by='x',ascending=False))
minn = s.min()
print(s.count(), s.sum(), s.index, s.shape, minn[0])

f = lambda x: x*2 + x*4
print(s.apply(f))

