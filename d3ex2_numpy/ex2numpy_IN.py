
import numpy as np

#a) Create a null vector of size 10 but the fifth value which is 1
a = np.zeros(10)
a[4] = 1
print(a)

#b) Create a vector with values ranging from 10 to 49
b = np.arange(10, 50)
print(b)


#c) Reverse a vector (first element becomes last)
c = np.arange(10)
np.flip(c)
print(c)
print(np.flip(c))


#d) Create a 3x3 matrix with values ranging from 0 to 8
d = np.arange(9).reshape(3,3)
print(d)

#e) Find indices of non-zero elements from [1,2,0,0,4,0]
e = np.array([1, 2, 0, 0, 4, 0])
e1 = e > 0
print(e[e1])

#f) Create a random vector of size 30 and find the mean value
f = np.arange(30)
print(f)
print(np.median(f))


#g) Create a 2d array with 1 on the border and 0 inside
#This is cheating:
#g = np.array([[1,1,1], [1,0,1], [1,1,1]])
#print(g)

g1 = np.ones((5,5))
#g1[0,:] = 0 - note to myself: makes the first row all zeros but the other rows will have the original value
ifancy = [1,2,3] #colums
islice = slice(1,4,1) #rows
g1[islice, :][:, ifancy] = 0
print(g1)


#h) Create a 8x8 matrix and fill it with a checkboard pattern
h = np.ones((8,8))
ifancy = [1,3,5,7] #colums
islice = slice(0,8,2) #rows
h[islice, :][:, ifancy] = 0
ifancy2 = [0,2,4,6]
islice2 = slice(1,8,2)
h[islice2, :][:,ifancy2] = 0
print(h)


#i) Create a checkerboard 8x8 matrix using the tile function
i = np.array([[1,0], [0,1]])
i1 = np.tile(i, (4,4))
print(i1)


#j) Given a 1d array, negate all elements which are between 3 and 8, in place
j = np.arange(11)
j[(j>3) & (j<8)] *= -1
print(j)


#k) Create a random vector of size 10 and sort it
k = np.array(np.random.rand((10)))
k_sorted = np.sort(k)
print(k_sorted)



#l) Consider two random array A and B, check if they are equal
l1 = np.random.randint(0,2,5)
l2 = np.random.randint(0,2,5)
equal = np.array_equal(l1, l2)
print(equal)
#they are not equal


#m) How to convert an integer (32 bits) array into a float (32 bits) in place?
m = np.arange(10, dtype=np.int32)
print(m.dtype)
m1= m.astype('float32')
print(m1.dtype)



#n) How to get the diagonal of a dot product?
n1 = np.arange(9).reshape(3,3)
n2 = n1 + 1
n3 = np.dot(n1,n2)
diagonal = np.diag(n3)
print(diagonal)





