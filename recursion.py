        #(1)factoriyal
# def fact(no):
#     if no==1:
#         return 1
#     else:
#         return no*fact(no-1)

# print(fact(5))      #5*4*3*2*1=120
# print(fact(7))      #7*6*5*4*3*2*1=5040

            #(2)calculate sum of list using recursion
# li=[1,2,5,4,7]
# li1=[1]

# def list_sum(list):
#     if len(list)==1:
#         return list[0]
#     else:
#         return list[0]+list_sum(list[1:])
    
# print(list_sum(li))
# print(list_sum(li1))            

        #(3)calculate product of list using recursion
# def product(list):
#     if len(list)==1:
#         return list[0]
#     else:
#         return list[0]*product(list[1: ])
    
# print(product([20,30,50]))        

        #(4) print your name 5 times using recursion
# def print_name(name,ntimes):
    
#     if ntimes==1:
#         return name
#     else:
#         return name + print_name(name,ntimes-1)
    
# print(print_name("yash\n",5))        

##__________________________________________________________________##
