    #traversing

# tup=("potatoe","tomato","cabbage")
# for i in tup:    
#     print(i)
    
    #print 1 to 30
# for i in range(1,31):
#     print(i)    
    
   #print 25 to 51
# for i in range(25,51):
#     print(i)        


    #1 to 10 squares
# for i in range(1,11):
#     print(i*i)
    
    
    #print a table of no    
# a=int(input("enter the no"))    
# for i in range(1,11):
#     print(a*i)    

    #print with power 4 from 1-5 
# for i in range(1,6):
#     print(i**4)


    #print with 12
# for i in range(1,21):
#     print(i)
#     if i==12:
#         break
    
    #print with out 12
# for i in range(1,21):
#     if i==12:
#         break
#     print(i)
    
    
       # 20-40 print 30 
# for i in range(20,40):
#     print(i)
#     if i==30:
#         break 
   
    #11-20 skip 16
# for i in range(11,21):
#     if i==16:
#         continue
#     print(i)   
    
    #print even no
# for i in range(1,21):
#     if i%2==0:
#         print(i) 

    #skip even no print odd no
# for i in range(1,21):
#     if i%2==0:
#         continue
#     print(i)        


# for i in range(20,41):
#     if i%5:
#         print(i)
#     else:
#         print("yash")     
        
   
    # Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700
# for i in range (1600,2700):
#         if(i%7==0) and (i%5==0):
#             print(i)

  
  #print even count 1-30                      
# ceven=0
# for i in range(1,31):
#     if i%2==0:
#         ceven+=1    
# print("even:",ceven)        

        #wap to multiply all the elements in the list
        
# li=[1,5,4,7,8]                    #1*5*4*7*1120
# prod=1
# for i in li:
#     prod*=i
# print(prod)    

    #wap to average all the elements in the list
# li=[1,5,4,7,8] 
# sum=1
# for i in li:
#     sum+=i
# a=len(li)     
# print(sum/a)

    #wap to differece of two list
# li1=[1,3,5,67,89,98]
# li2=[3,5,89,76,87,76]
# diff=set(li1).difference(set(li2))
# print(list(diff))
    
    #calculate the number of alphabet,digit,special symbol in string
# str="yashpatel@8262#"
# alpha=digit=symb=0
# for i in str:
#     if i.isalpha():
#         alpha+=1  
#     elif i.isdigit():
#         digit+=1
#     else:
#         symb+=1
# print("alpha:","digit:","symb:",alpha,digit,symb)   

    #wap a program to dictionary by input  a number from 1-n in the form  of {n:n*n}
    
# d1={}
# n=int(input("enter the no"))
# for i in range (1,n+1):
#     d1[i]=i*i   
# print(d1)    

    # even no print in range of (1500-2500)
# for i in range(1500,2500):  
#     if  i%2==0: 
#         print(i)  


    #sum of all the keys  and sum of all the values  in a dictionary
    
# d1={
#     1:4,
#     16:25
# }
# print(sum(d1.keys()))        
# print(sum(d1.values()))        

    #all the values of dictionary are same or not
 
# d1={
#     1:4,
#     16:25
# }  
# a=int(input("enter the no"))
# for i in d1.values():
#     if i==a:
#         print("same") 
#     else:
#         print("not same")                      

 
        #statswith 
# str=input("enter the string:")
# if str.startswith("ya"):
#         print("yes")
# else:
#         print("no")

    #wap to remove emply list from tuple
# tup=([],"a",1)
# li=list(tup)
# li.remove([])
# print(tuple(li))
                                                    
    #remove brackets() 
# li=[(),(1,2),(),(),(4,5,6)]
# for i in li:
#     if (i!=()):
#         print(i)
    
    #convert ascending order
# d1={
#     1:"a",
#     5:"b",
#     2:"c"
# }
# d1=dict(sorted(d1.items()))
# print(d1)   



    
    