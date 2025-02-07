# def add(n):
#     return n+n
# li=[1,2,3,4,5]

# #map = (func_name , argumants )
# y = map(add,li)
# print(list(y))

##____________________________________________________________________##
#by using map() calculate factorial of members of list

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f

# li=[1,2,4,5]
# fact=map(fact,li)

# print(list(fact))
##____________________________________________________________________##

#Wap to calculate square of each member of list using map()
# def square(num):
#     return num ** 2

# numbers = [1, 2, 3, 4, 5]

# squares = list(map(square, numbers))

# print("Original List:", numbers)
# print("Square of each member:", squares)


            # or
            
            
# li=[1,2,3,4,5]
# sq=map(lambda x : x**2,li) 
# print(list(sq))           

##____________________________________________________________________##

#Wap to calculate addition of 2 list using map()

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# def sum_list(list1,list2):
#     return list1+list2

# x=map(sum_list,list1,list2)

# print(list(x))



        # or
        
# li1=[2,4,7,9,4]
# li2=[3,6,8,2,7]
# res=map(lambda x,y:x+y,li1,li2)
# print(list(res))

##____________________________________________________________________##

# Write a  Python program to square and cube every number in a given tuple of integers using Lambda

# numbers = (1, 2, 3, 4, 5)
# square = tuple(map(lambda x: x**2, numbers))
# cube = tuple(map(lambda x: x**3, numbers))
# print("Square:", square)
# print("Cube:", cube)

##____________________________________________________________________##

# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# subjects=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# subjects.sort(key=lambda x : x[1])
# print(subjects)
##____________________________________________________________________##

# Write a  Python program to sort a list of dictionaries using Lambda on the basis of color
# models = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]

# models = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]


# models.sort(key=lambda x:['color'] )
# print(models)
##____________________________________________________________________##

#by using map() and lambda() calculate factorial of members of list
