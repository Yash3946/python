# It is a low level graph library , created by Johm D hunter , open source and free
# It is created in python , some segments from C , js
# import matplotlib
# print(matplotlib.__version__)

##_______________________________________________##
# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([0,6])
# y=np.array([0,250])

# #to plot graph we use ploy()
# plt.plot(x,y)

# #to show graph ina new tab we use show()
# plt.show()
##_______________________________________________##
# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([0,6,7,9,10])
# y=np.array([0,43,87,234,250])

# #to plot graph we use ploy()
# plt.plot(x,y,'o')
# plt.plot(x,y,'r')
# plt.plot(x,y,'black')

# #to show graph ina new tab we use show()
# plt.show()

##_______________________________________________##

# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([0,6,7,9,10])
# y=np.array([0,43,87,234,250])

# #to plot graph we use ploy()
# plt.plot(x,y,'o')
# plt.plot(x,y,'r')
# plt.plot(x,y,'black')
# plt.plot(x,y,marker="o")
# #to show graph ina new tab we use show()
# plt.show()

        ##_______________________________________________##
                
                    # myplotlib line
        ##_______________________________________________##

# import matplotlib.pyplot as plt
# import numpy as np

# y=np.array([3,15,6,12])
# plt.plot(y,linestyle='dotted')
# plt.show()

# y=np.array([3,15,6,12])
# plt.plot(y,ls=':')
# plt.show()

# y=np.array([3,15,6,12])
# plt.plot(y,linewidth='3.9')
# plt.show()

# y1=np.array([4,6,27,12,67])
# y2=np.array([2,6,48,18,76])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

##_______________________________________________##

# wap to make a line graph in such a way that x axis take year from 2000 -2024 and at y axis take students marks and draw a line graph

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([2004,2008,2020,2022])
# y=np.array([45,67,73,98])
# plt.plot(x,y)
# plt.title("average  marks of students per year",loc="left")
# plt.xlabel("year",color='red',size=12)
# plt.ylabel("marks of student",color='green')
# plt.grid(axis="y",color='red',linewidth=2)
# plt.show()



##_______________________________________________##
#WAP to make a graph marks of 4 students in year 2021, 2022, 2023,2024
# data of students is as such
# marks1=[80,90,85,92] -> draw first student marks in green -> solid line
# marks2=[90,80,75,62] -> draw second student marks in red  -> dashed line
# marks3=[60,70,80,92] -> draw third student marks in blue  -> solid line
# marks4=[80,85,85,89] -> draw ffourth student marks in pink -> dotted line
# Take marks on y axis and years on x axis

# import matplotlib.pyplot as plt

# years = [2021, 2022, 2023, 2024]
# marks1 = [80, 90, 85, 92]
# marks2 = [90, 80, 75, 62]
# marks3 = [60, 70, 80, 92]
# marks4 = [80, 85, 85, 89]


# plt.plot(years, marks1, color='green', linestyle='solid')
# plt.plot(years, marks2, color='red', linestyle='dashed')
# plt.plot(years, marks3, color='blue', linestyle='solid')
# plt.plot(years, marks4, color='pink', linestyle=':')

# plt.title('Student Marks Trend (2021-2024)')
# plt.xlabel('Year',size='6')
# plt.ylabel('Marks',size='8')
# plt.grid(True)
# plt.legend()

# plt.show()

##_______________________________________________##

# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([2,4,6,5])
# y=np.array([12,24,26,15])

# #plot1
# plt.title("sales")
# plt.subplot(1,2,1)      # 3 arguments -> rows,cols,index
# plt.plot(x,y)

# x=np.array([1,5,6,2])
# y=np.array([2,4,6,11])

# #plot2
# plt.title("year")
# plt.subplot(1,2,2)      #3 arguments -> rows,cols,index
# plt.plot(x,y)

# plt.suptitle("my bussiness")
# plt.show()

##_______________________________________________##
    #SCATTER GRAPH
# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array([2,4,6,5,6,7,10,12,15,12])
# y=np.array([12,24,26,15,12,13,11,10,18,17])

# plt.scatter(x,y)

# x=np.array([2,4,6,5,6,7,10,12,15,12])
# y=np.array([11,4,6,15,2,3,12,1,8,7])

# plt.scatter(x,y)

# plt.show()
##_______________________________________________##

# import matplotlib.pyplot as plt
# import numpy as np 

# x=np.array([2,4,6,5,6,7,10,12,15,12])
# y=np.array([12,24,26,15,12,13,11,10,18,7])

# plt.scatter(x,y)

# # x=np.array([1,2,6,5,6,7,10,1,1,10])
# # y=np.array([2,4,26,5,2,3,1,10,18,7])
# # plt.scatter(x,y)


# x=np.array([1,2,6,5,6])
# y=np.array([2,4,26,5,2])
# colors=np.array(["yellow","red","green","blue","pink"])
# plt.scatter(x,y,c=colors)
# plt.show()

##_______________________________________________##

# import matplotlib.pyplot as plt
# import numpy as np 
# x=np.array(["student1","student2","student3","student4"])
# y=np.array([60,70,80,90])
# # plt.bar(x,y)
# # plt.barh(x,y)
# # plt.barh(x,y,color="green")
# plt.bar(x,y,width=0.2)
# plt.show()

##_______________________________________________##

# import matplotlib.pyplot as plt
# import numpy as np 
# student=np.array(["student1","student2","student3","student4"])
# plt.pie(y,labels=student)
# plt.show()
##_______________________________________________##

# import matplotlib.pyplot as plt
# import numpy as np 

# y=np.array([30,40,60,80])
# student=np.array(["student1","student2","student3","student4"])
# col=["black","yellow","green","pink"]
# plt.pie(y,labels=student,colors=col)
# plt.legend(title="4 students")
# plt.show()
##_______________________________________________##
#  Write a  Python programming to create a pie chart of the popularity of
# programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# add legends with title


# import matplotlib.pyplot as plt
# import numpy as np 

# y=np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
# language=np.array(["java","python","php","javascript","c","c++"])
# plt.pie(y,labels=language)
# plt.legend(title="languages")
# plt.show()
##_______________________________________________##

# Write a Python program to draw a scatter plot comparing two subject marks of
# Mathematics and Science. Use marks of 10 students.
# Sample data:
# Test Data:
# math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
# science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
# marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# import matplotlib.pyplot as plt
# import numpy as np

# marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
# science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

# plt.scatter(marks_range,math_marks,color="red")
# plt.scatter(marks_range,math_marks,color="green")


# plt.show()
##_______________________________________________## 
