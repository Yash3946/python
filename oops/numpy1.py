# create string array using numpy

# import numpy as np
# arr=np.array(["mini","miki","kush","rono","jalu","pappu"])
# print(arr[0])
# print(arr[1:3])
# print(arr[:3])
# print(arr[-1])

##_______________________________________________________________________##

# create string array using numpy
# import numpy as np
# arr=np.array(["mini","miki","kush","rono","jalu","pappu"])
# print(arr[: :-1])

##_______________________________________________________________________##
    #data type find
# import numpy as np
# arr1=np.araay([1,2,3,4,5,6,56])
# print(arr1.dtype)

##_______________________________________________________________________##
    # copy and view
# import numpy as np
# arr=np.array(["mini","miki","kush","rono","jalu","pappu"])
# arr1=np.araay([1,2,3,4,5])

# x=arr1.copy()
# print(x)
# arr1[0]=100
# print(arr1)

##_______________________________________________________________________##

    #array shape

# import numpy as np
# x=np.array([[1,2,3,4],[2,3,5,6],[7,5,4,3]])
# print(x.shape)
##_______________________________________________________________________##

    #array reshape
# import numpy as np
# arr=np.array([1,3,4,6,7,8,9,7,6,5,3,1])
# newarr=arr.reshape(3,4)     #1d array to 2d array
# print(newarr)

# newarr1=arr.reshape(2,3,2)
# print(newarr1)
##_______________________________________________________________________##
# import numpy as np
# arr=np.array(["abc","def","hij"])
# for i in arr:
#     print(i,end=" ")
# arr1=np.array([["abc","def","hij"],['a','b','c']])
# for i in arr1:
#     for j in i:
#         print(j)

##_______________________________________________________________________##

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# splitarray=np.array_split(arr,4)
# print(splitarray)

# arr1=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# newarr=np.array_split(arr1,3)
# print(newarr)

##_______________________________________________________________________##
    #seraching in array
# import numpy as np
# arr=np.array([1,2,3,4,5,6,3,7,4,6,3])
# x=np.where(arr==3)
# print(x)

# y=np.where(arr%2==0)
# print(y)

# z=np.where(arr%2==0)
# print(y)

##_______________________________________________________________________##

# #-sorting in array

# arr=np.array([1,3,4,2,5])
# print(np.sort(arr))

# arr1=np.array([12,3,4,1,2])
# print(np.sort(arr1))

# arr2=np.array(["abc","mini","ishi","hiii"])
# print(np.sort(arr2))


# arr3=np.array([[1,3,2],[7,3,0]])
# print(np.sort(arr3))

##_______________________________________________________________________##

# create an array of boolean values and sort it

# import numpy as np
# bool_array = np.array([True, False, True, False, True, False, True])
# sorted_array = np.sort(bool_array)
# print(sorted_array)

##_______________________________________________________________________##

#-create an array and store its even values in a list


# import numpy as np

# arr12=np.array([12,3,4,1,2])
# li=[]

# for i in arr12:
#   if i %2==0:
#     li.append(i)

# print(li)
##_______________________________________________________________________##
