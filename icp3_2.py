import numpy as np
a = np.random.randint(1,20,15)
print(a)

b = a.reshape((3,5))
print(b)

c=np.where(b == np.amax(b, axis=1,keepdims=True),0,b)
print(c)