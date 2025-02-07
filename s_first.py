# (2)find
# (3)concatenation
# (4)length  
# (5)str place    
# (6)str slice
# (7)upper      
# (8)lower     
# (9)capitalize   
# (10)strip  (remove space)     
# (11)replce  
# (12)endswith
# (13)count    
# (14)thrice

        # (1)
# a=12 
# age=23
# print(age)


        # (2)
# print("my name is yash \n i am in royal \n i live in ahmedabad")


         # (3)concatenation
# a=("my name is yash \n")
# b=(" my age is 21")
# print(a+ b)

        # (4)length
# a=("i am learning coding")
# print(len(a))

        # (5)str place
# str="patel yash"
# print(str[2])

        # (6)str slice
# str="education is the key of sucess"
# print(str[4:15])
# print(str[-14:-1])

        
# str="royal technosoft"
# print(str[0:10:3])

        #(7)upper
# str="royal technosoft"
# print(str.upper())

        #(8)lower
# str="royal technosoft"
# print(str.lower())

        #(9)capitalize
# str="royal technosoft"
# print(str.capitalize())


        #(10)strip     (remove space)
# str="       royal technosoft"
# print(str.strip())

        #(11)replce
# str="python programing"
# print(str.replace("python","java"))

        #(12)endswith
# str="python programing"
# print(str.endswith("g"))

        #(12)find
# str="python programing"
# print(str.find("th"))

        #(13)count
# str="python programing"
# print(str.count("p"))


# lang="python is my fav language"
# print(lang[24])
# print(len(lang))

# print("my name is yash \n i am in royal \n i live in ahmedabad \n i am from himaatnagar")


        #(14)thrice
# print("my name is yash \n "*3)


        #replace
# a="python is the way for data science"
# a=a.replace("e","@")
# a=a.replace("y","s")
# print(a)

        #concetination
# a=("my name is yash")
# b=(" my age is 21")
# print(a+ b)


# print(True==3)

# a="10.56"
# b="25.55"
# c=float(a)
# d=float(b)
# print(c+d)

        #with input type casting
        
# a=int(input("enter your value"))
# b=int(input("enter your value"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)



# a=int(input("enter your length"))

# print("area of square:",a*a)  
# print("area of parameter:", 4*a)


# a=int(input("enter your value"))
# b=int(input("enter your value"))
# c=int(input("enter your value"))

# d=a+b+c
# print(d)
# print("average:",d/3)


        #simple interest(s.i)

# p=float(input("enter your principal value"))
# r=float(input("enter  rate"))
# t=int(input("enter your time"))
# print("simple interest:",(p*r*t)/100)


# a=int(input("enter your value"))

# if(a>=5):
#         print("grater")
        
# if(a<5):
#         print("not greater")        
        
 

# a=int(input("enter whethe no"))

# if(a%2==0):
#         print("even")

# else:
#         print("odd")        



        #divisible or not divisible
        
# a=int(input("enter  no"))

# if(a%7==0):
#         print("divisible")
        
# else:
#         print("not divisible")        

     
     
        #greater no:
        
# a=int(input("enter  no1:"))
# b=int(input("enter  no2:"))
# c=int(input("enter  no3:"))

# if(a>b and a>c):
#         print("a is greater")
        
# elif(b>c):
#         print("b is greater")
# elif(a==b==c):
#                 print("equal")
# else:
#         print("c is greater")                        


         #greater no:
         
# a=int(input("enter  no1:"))
# b=int(input("enter  no2:"))
# c=int(input("enter  no3:"))
# d=int(input("enter  no4:"))

# if(a>b and a>c and a>d):
#         print("a is greater")
        
# elif(b>c and b>d):
#         print("b is greater")
# elif(c>d):
#         print("c is greater")
# else:
#         print("d is grater")




# dresscode=input("enter the dresscode:")

# if(dresscode=="western dress"):
#         print("western party")
# elif(dresscode=="traditional dress"):
#         print(dresscode=="traditional party")
# elif(dresscode=="formals"):
#         print("office party")
# else:
#         print("casuals party")
        

# li=[21,34,56,76,87,65,43,23]
# print(str(li[1:7:3]))       

                #append()
                                                                        
# li=[]
# a=input("enter  no")       
# li.append(a)
# b=input("enter  no")       
# li.append(b)
# c=input("enter  no")       
# li.append(c)
# print(li)


        # swaping
# li=[1,2,3,4,5]
# li[2],li[3]=li[3],li[2]
# print(li)


        #no is present or not
# li=[1,2,3,4,5]
# a=int(input("enter your value"))
# if a in li:

#         print("no is present")

# else:

#         print("no is not present")



# li=[23,4,67,98,98,76]
# x=int(input("enter the no"))

# if x in li:
#         print("no is present")
        
# else:
#         print("no is not present")


# li=[23,4,67,98,98,76]
# x=min(li)
# print(x)
# y=max(li)
# print(y)

        #insert name
# li=["yash","jogesh","jalay","tithi","vishwek"]
# li.insert(3,"royal")   
# print(li)

        #remove name
# li=["yash","jogesh","jalay","tithi","vishwek"]
#  li.remove("yash")
# li.pop(0)
# print(li)

        #copy with out copy function
# li=["yash","jogesh","jalay","tithi","vishwek"]
# a=li[0:]
# print(a)

#                 #tup
# tup=(21,34,67,"yash")        
# print(type(tup))
# print(len(tup))



# li="Colonialism led to new forms and systems of   education, including new schools, curricula, examinations, certificates, and degrees, which often served the needs and interests of the colonial administration and economy."
# print(li.count("and"))

# a=float(input("enter the no"))
# b=float(input("enter the no"))
# c=float(input("enter the no"))
# d=(a+b+c)
# print(d/3)

        #reverse
# li=[1,2,3,4]
# li.reverse()
# print(li)


# a=int(input("enter the no"))
# b=a.copy()
# b.reverse()
# print(b)
# if a==b:
#         print("palingrom no")
# else:
#         print("not palindrom")        


# li=[]
# a=input("enter the no")
# li.append(a)
# b=input("enter the no")
# li.append(b)
# print(li)


# tup=(21,34,67,89,56,45.34,32,"yash",34,21.44,89)
# print(tup.index(34))
# print(tup.count(89))
# print(len(tup))


# tup=(21,34,67,89,56,45.34,32,"yash",34,21.44,89)
# print(tup[3])

# tup=(15,25,45,12,75,100)
# print(tup[-4:])
# print(tup[2:6])

# tup=("A,B,C,C,B,C,A,A,B,D,A")
# print(tup.count("A"))         

        #tup to list
# tup=(1,3,5,7,65,43,35)
# a=list(tup)
# print(a)
# print(type(a))

        #list to tup 
# li=[1,3,5,7,65,43,35]
# a=tuple(li)
# print(a)
# print(type(a))

        #"".join
# name=("p,y,t,h,o,n")
# a=" ".join(name)
# print(a)

        #"$".join
# tup=("r","o","y","a","l")
# a="$".join(tup)
# print(a)

        #max or min(tup)
# tup=(1,5,6,2,8,10,1,56)
# print(max(tup))
# print(min(tup))

# tup=("python","java","c","cpp","data science")
# a=" ".join(tup) 
# print(a)


# a=("python","java","c","cpp","data science")
# b=list(a)
# b.remove("c")
# a=tuple(b)
# print(b)

                #or

# a=("python","java","c","cpp","data science")
# b=list(a)
# b.pop(-1)
# a=tuple(b)
# print(b)

# dict={        
# "name":"yash",
# 'age':"21",
# "subjects":["c","cpp","java","python"], 
#         "marks":
#                 {
#                 "phy":89,
#                 "che":98,
#                 "bio":97
#                 }
# }
# print(dict)
# print(len(dict))
# print(type(dict))

# dict["is adult"]=True
# print(dict)


# info={        
# "name":"yash",
# 'age':"21",
# "subjects":["c","cpp","java","python"],
#         "marks":
#                 {
#                 "phy":98,
#                 "che":89,
#                 "bio":90
#                 }
# }
# print(info)
# print(type(dict))



# info={
#     "name":"shraddha",
#     "age":22,
#     "female":True
# }

# d={
#     "sub":[1,2,3,4],
#     "adult":True
# }
# print(d.keys())  #only keys
# print(d.values()) #only values
# print(d.items())     #keys and values both
# print(d.get("age")) #use keys give values
# d.update(d)        #update values
# print(d)



# table={
#         "table":["peice pf furniture","number of multiplication"],
#         "cat":"animal"
#       }
# print(table)



        
        #3 subjects marks input and convert dict to list
# dict={
        
#      }
# a=int(input("enter the marks"))
# dict.update({"phython":a})

# b=int(input("enter the marks"))
# dict.update({"c":b})

# c=int(input("enter the marks"))
# dict.update({"cpp":c})

# print(dict)

# li=[]
# d=dict.items()
# li.append(d)
# print(li)


#wap to generate dictionary in the form of (n: n**4)
# dict={}
# n=int(input("Enter number = "))
# for i in range(1,n+1):
#     dict[i]=i**4
# print(dict)

# li1=["a","b","c"]
# li2=[1,2,3]
# d={}
# for i in li1:
#         for j in li2:
#                 d[i]=j
#                 li2.remove(j)
#                 break
# print(d)        
                