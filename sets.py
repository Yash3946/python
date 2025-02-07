# s={1,2,3,4,"mini","programming",2,4}
# print(s)
# print(len(s))

# set element must be immutable but set is mutable

# s={1,2,3,4,"royall",(1,2)}

# s1={1,2,3,4,5}
# s1.add("blue")     #it add element
# s1.remove(2)       #remove element
# s1.clear()         #make set empty

#x=s.copy()          #copy set
# s1.pop()            #remove asc first digit value from set
# print(s1)

# se={1,2,4,5,2,2,27,"mini",(1,"abc")}
# s=set()
# print(type(s))

        
        #unique elements collection 
        #unordered
        # set is mutable but their elements are immutable


# s1={1,2,3,4,"mini"}
# s2={4,2,7,8,"abc"}
# print(s1.union(s2))          #returns all elements of both set
# print(s1.intersection(s2))   #returns common element from both sets


        #difference

# s1={1,2,3,4,"mini"}
# s2={4,2,7,8,"abc"}
# print(s1.difference(s2))     #returns element of first set from which we are substracting except common elements
# s1.discard(3)               #discard or removes elements
# print(s1)



# s1={1,2,5,7,8,"mini","pizza","black",23,(15,15)}
# s2={2,4,"mini",87,23,(4,4),"juice","programming",1}

#symmetric difference         #return all elements discarding common elements
# s1={1,2,3,4}
# s2={4,1,5,6,8}                        #s1 symmwtric diff= {2,3,5,6,8}
# print(s1.symmetric_difference(s2))

# Subset

# a={'m','i','a','b'}
# b={'i','a'}           #if all set of el b is in set a then set b is subset of set a
# print(b.issubset(a))   #it returns boolean value that first set is subset of another or not
# print(a.issubset(b))



# a={1,2,3,4}
# b={1,2,3,4,5,6,7}
# print(a.issuperset(b))
# print(b.issuperset(a))
# print(a.issubset(b))
# print(b.issubset(a))









































































