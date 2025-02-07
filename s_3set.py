# set=remove duplication
# s={1,3,5,6,8,9,7,6,5,4,4}
# print(s)
# print(len(s))


# s1={1,3,4,7,9,"yash"}
# s1.add("green")
# s1.remove(3)
# print(s1)

# s1.clear()
# print(s1)


# s1={1,3,4,7,9,"yash"}
# x=s1.copy()
# print(x)

# s1.pop()
# print(s1)


# union and intersection
# s1={1,3,5,6,89,"patel"}
# s2={13,5,4,3,2,1}
# print(s1.union(s2))
# print(s1.intersection(s2))

#difference
# s1={1,3,5,6,89,"patel"}
# s2={13,5,4,3,2,1}
# print(s1.difference(s2))

    #discard(remove)
# s1={1,3,5,6,89,"patel"}
# s2={13,5,4,3,2,1}
# s1.discard(1)
# print(s1)    


# s1={1,2,5,7,8,"mini","pizza","black",23,(15,15)}
# s2={2,4,"mini",87,23,(4,4),"juice","programing",1}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# s1.discard("mini")
# print(s1)

    #symmetric_difference
# s1={1,2,3,4,5}
# s2={2,3,5,6,7}
# s1.symmetric_difference(s2)


    #set len
# set={"tiger","lion","tiger","leapord","tiger","leapord","hippo","lion","hippo","wolf","lion","wolf"}
# print("no of cages:",len(set))

    #print=>8,8.0
# val={"8",8.0}
# val={(8,"int"),8.0}
# print(val)


    #difference
# s1={1,2,3,4,5}
# s2={2,3,5,6,7} 
# print(s1.difference(s2))   

#in set element is present or not
# s1={1,2,3,4,5}
# a=int(input("enter the choice"))
# if a in s1:
#         print("present")
# else:
#         print("not present")    
    
    
    #common elements 
# s1={1,2,3,4,5}
# s2={1,32,43,34,5}        

# if s1.intersection(s2):
#     print("common elements")
# else:
#     print("no common element")    
    
    #average find
# set={154,152,254,785,452}
# a=sum(set)
# b=len(set)
# print(a/b)

# a={1,2,3,4,5}
# b={1,32,43,34,5}        
# if a.issubset(b):
#     print("yes")
# else:
#     print("no")    
  
# set1={1,2,5,6,7,8,8}    
# set2={2,5,10,11,8,9}
# a=(set1.union(set2))
# print(len(a))


    #1
# s={1,3,5,6,8,9,7,6,5,4,4}
# s.add("green")
# print(s)

#     #2
# s={1,3,5,6,8,9,7,6,5,4,4}
# s.remove(4)
# print(s)    

    #3
# set={1,3,54,76,98,43,23,46}
# a=int(input("enter the no"))   
# if a in set:
#     set.remove(a)
#     print(set)
# else: 
#   print("dont remove")     

    #4
# s1={1,3,5,6,89,"patel"}
# s2={13,5,4,3,2,1}
# print(s1.difference(s2))    

    #5
# s1={1,2,3,4,5}
# s2={2,3,5,6,7}
# print(s1.symmetric_difference(s2))    

    #6
# a=int(input("enter the no"))  
# set={1,3,54,76,98,43,23,46} 
# if a in set:
#     print("present")
# else:
#     print("not present")     

    #7
    
# s1={1,2,3,4,5}
# s2={1,32,43,34,5}        

# if s1.intersection(s2):
#     print("common elements")
# else:
#     print("no common element")    

    #any 1 elements delete
# s1={1,2,3,4,5}
# print(s1)
#s1.remove(3)  
# s1.pop()
# print(s1)

    #2 wap to input 10 string from user and store them in set
# s=set()
# for i in range(1,11):
#         str=input("enter the string")  
#         s.add(str)
# print(s)

       #3 wap to check that set is superset of itself as well as of other set
# a={1,2,3,4,5}
# b={1,32,43,34,5}        
# if a.issubset(b):
#     print("yes")
# else:
#     print("no")            

    #4 wap to check that two sets have no common elements
# s1={12,45,87,98,56,43}
# s2={21,45,67,98,34,23,76}
# if s1.intersection(s2)==0:
#     print("no common elements")    
# else:
#     print("common elements")    

    #5 wap to find those element in given set which is not in another set
    
# s1={12,45,87,98,56,43}
# s2={21,45,67,98,34,23,76}
# print(s1.difference(s2))  

    #6 Write a  Python program to find all the unique words and count the frequency of occurrence from a given

# li=["a","c","x","m","f","m","f"]
# print("unique words are : ",set(li))

# d={}
# for i in li:
#     d[i]=li.count(i)

# print(d)    

    #7 remove an element from set it it present , so first check if it is present then remove it.
# s={1,2,4,6,8,"vd"}
# if "vd" in s:
#     s.remove("vd")
# else:
#     print("not present")
# print(s)