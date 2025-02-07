        #1 tect.file  (data.txt)
        
        
# f=open("data.txt","r")
# data=f.read()       #read file
# print(data)
# f.close()

# f=open("data.txt","r")
# data=f.readline(10)       #readline id read 10 characters
# print(f.readable())         #this file readble true or false 
# f.readlines()          #readlines   
# data=f.read
# print(data)
# f.close()


# f=open("data.txt","w")   #write means overwrite
# f.write("yash\n")        #only write 1 line
# f.writelines(["patel\n","yash"])#write multiple lines
# print(f.writable())

# f=open("data.txt","a")  #append
# f.write(" \t royal")
# f.writelines(["\n yash", "\n vrutik", "\n jalay", "\n tithi"])

# f.close()


# f=open("data.txt","r+")    #this mode is allows read and write
# f.write("abc is alphabets")
# data=f.read()
# print(data)

# f.write("jalp")
# f.close()


# f=open("data.txt","w+")  #it allows  us to overwrite  adn read 
# f.write("royal technosoft")
# f.seek(2)              #it moves the pointer
# print(f.read())
# f.close()

# f=open("data.txt","a+")         #it allows  us to append and read
# f.write("\n python batch")
# f.seek(10)
# print(f.read()) 


# f=open("data.txt","r")
# for i in f:
#         print(i)  

###########################################################
# ___________________________________----
# make a new file "newfile.txt"

# add these lines in same order
# We are learning python
# python is best language
# universe is blessing me
# we thank to universe

# read all data in using for loop

# append in next line
# Nature is good.


# f=open("data.txt","a+")
# f.writelines(["\n We are learning python","\n python is best language"," \n universe is blessing me"," \n we thank to universe"])
# f.write("\n nature is good")
# for i in f:
#         print(i)
# f.close()

##############################################################


# f=open("yash.txt","w")  #file open
# f.close()               #file close
# import os               #file delete      
# os.remove("yash.txt")

# p=os.start("data.txt")
# print(p)

# import os
# size= os.path.getsize("data.txt")  #size info
# print(size)


##___________________________1-> read first n lines  of the file________________________##

# f=open("data.txt",'r')
# n=int(input("enter the no"))
# line=f.readlines()
# for i in line[ :n]:
#         print(i)
# f.writelines(["\n We are learning python","\n python is best language"," \n universe is blessing me"," \n we thank to universe"])
# f.close() 

##______________________________________________________________________________________##

##___________________________2-> read last n lines  of the file________________________##
# f=open("data.txt",'r')
# n=int(input("enter the no"))
# line=f.readlines()
# for i in line[n: ]:
#         print(i)
# f.writelines(["\n We are learning python","\n python is best language"," \n universe is blessing me"," \n we thank to universe"])
# f.close() 

##______________________________________________________________________________________##

##_________________________3 -> replace "python" with  "robotics" in life__________________ ##
# f=open("data.txt",'r')
# data=f.read()
# new=data.replace("python","robotics")
# f=open("data.txt",'w')
# f.write(new)
##__________________________________________________________________________________________##
 
##_____________________search if 'easy' present in file or not_____________________________##

# f=open("data.txt","r")
# data=f.read()
# a="robotics"

# if a in data:
#     print("easy")
# else:
#     print("not easy")

##__________________________________________________________________________________________##

##_____________________________count any word in file _______________________________________##

# f=open("data.txt","r")
# data=f.read()
# new=data.count("robotics")
# print(new)

##_____________________copy the data  of first file into second file ______________________##

# f=open("data.txt","r")
# data=f.read()
# f=open("data2.txt","a")
# f.write(data)
# f.close()

##__________________________________________________________________________________________##


##_____________________print even number from the file ______________________##

# f=open("data2.txt","r")
# data=f.read()
# no=data.split(",")
# for i in no:
#         if(int(i)%2==0):
#                 print(i)               
##___________________________________________________________________________________________##
                
##_____________________print even number from the file ______________________##
                
# f=open("data2.txt","r")
# data=f.read()
# no=data.split(",")
# for i in no:
#         if(int(i)%2!=0):
#                 print(i)                
##__________________________________________________________________________________________##
                
##_____________________print even number count from the file ______________________##
# f=open("data2.txt","r")
# data=f.read()
# no=data.split(",")
# count=0
# for i in no:
#         if(int(i)%2==0):
#                 count+=1
#                 print(i)
# print("no count:",count)
                  
##__________________________________________________________________________________________##
           
##__________write a python program to read of file line by line  and store it in a list_________##
           
# f=open("data.txt","r")
# data=f.readlines()
# print(data)

##__________________________________________________________________________________________##


##____________________________add li=["hi","everyone"] in the file____________________________##

# f=open("data.txt","w")
# li=["hi","everyone"]
# for i in li:
#         f.write(i)
##__________________________________________________________________________________________##
        
##____________________________length of file____________________________##

# f=open("data.txt","r")
# import os
# size= os.path.getsize("data.txt")  #size info
# print(size)
##__________________________________________________________________________________________##
