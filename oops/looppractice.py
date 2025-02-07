# generate fibbonacci series upto n (while loop)
# 0,1,1,2,3,5,8,13

# n=int(input("enter a number : "))
# a,b=0,1

# i=1
# while i<=n:
#     print(a,end=" ")
#     a,b=b,a+b
    
#     i+=1
##_______________________________________________________________________##

# generate fibbonacci series upto n (for loop)

# n=int(input("enter a number : "))
# a,b=0,1

# for  i in range (1,n+1):
#     print(a,end=" ")
#     a,b=b,a+b
    
##_______________________________________________________________________##
    #print armstrong number
    
# n=int(input("enter a number : "))
# num=n
# sum=0
# while n > 0:
#     digit=n%10
#     sum+=digit**3
#     n//=10
# print(sum)

# if num==sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")
    
##_______________________________________________________________________##
    
    #print prime number
# n=int(input("enter a number : "))

# i=2
# p=True
# while i<n:
#     if n%i==0:
#         p=False
#         break
    
#     i+=1
# if p==True:
#     print("it is prime number")
# else:
#     print("it is not prime number")
    
##_______________________________________________________________________##

# *
# **
# ***
# ****
# *****
# ******

# for i in range(7):
#     print("*"*i)


##_______________________________________________________________________##

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


