import numpy as  np
list1 = [25, 56, 12, 85, 34, 75]
list2 = [42, 3, 86, 32, 856, 46]
arr1=np.array(list1, )
arr2=np.array(list2, dtype=int)
narr=np.array(np.random.rand(6))
print(arr1)
print(arr2)
print(narr)
#narr1=np.array(list1, dtype=complex)
narr1=arr1.astype(complex)
narr2=arr2.astype(complex)
print(narr1)
narr1_mat=arr1.reshape(2,3)
narr2_mat=arr2.reshape(2,3)
print(narr1)
print(narr2)
print((narr1+narr2)*(narr1-narr2)/narr1-narr2)