#pandas is a library which is used to work with data sets
#its main function is to analyze data, clean data, explore data and manipulate data
#pandas -> 'panel data' or "python data analysis" in 2008 , wes mcKinney
# to handle large data set
# max, min , min , co-relation
#Dataframe in pandas -> dimensions -> vertically- horizontally arrange

##_______________________________________________________________##
# import pandas as pd
# a=[1,2,3,4]

# var=pd.Series(a)
# print(var)
# print(var[2])

# b=["a","b","c","def"]
# var1=pd.Series(b)
# var1=pd.Series(b,index=['a','b','c','d'])
# print(var1)
##_______________________________________________________________##

# import pandas as pd
# calorie={"day1":200,"day2":200,"day3":300}
# var=pd.Series(calorie)
# print(var)
##_______________________________________________________________##
    ##data frame in pandas ==>multi dimensional table is df(more than 1 column)
# import pandas as pd
# calorie={"day1":[100,200,300],
#          "day2":[400,500,600],
#          "day3":[700,800,900]
#         }
# df=pd.DataFrame(calorie,index=["day1","day2","day3"])
# print(df)

##_______________________________________________________________##
# import pandas as pd
# calorie={"day1":[100,200,300],
#          "day2":[400,500,600],
#          "day3":[700,800,900]
#         }
# df=pd.DataFrame(calorie)
# print(df)
##_______________________________________________________________##
    ##locate row or column
# import pandas as pd
# calorie={"day1":[100,200,300],
#          "day2":[400,500,600],
#          "day3":[700,800,900]
#         }
# df=pd.DataFrame(calorie)
# print(df.loc[0])
# print(df.loc[[0,1]])
##_______________________________________________________________##

# import pandas as pd
# calorie={"day1":[100,200,300],
#          "day2":[400,500,600],
#          "day3":[700,800,900]
#         }
# df=pd.DataFrame(calorie,index=["day1","day2","day3"])
# print(df.loc["day2"])
##_______________________________________________________________##
# import pandas as pd
# calorie={"day1":[100,200,300],
#          "day2":[400,500,600],
#          "day3":[700,800,900]
#         }
# df=pd.DataFrame(calorie)
# print(df)
##_______________________________________________________________##
# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df)       #print only first 5 rows and last 5 rows
# print(df.to_string())  #print all data

##_______________________________________________________________##
    # max rows you need
    
# import pandas as pd
# pd.options.display.max_rows=999
# df=pd.read_csv('data.csv')
# print(df)
##_______________________________________________________________##

# import pandas as pd
# from pandas import json_normalize
# import json

# with open ('sample1.json') as f:
#     data=json.load(f)
# df=json_normalize(data)
# print(df)
##_______________________________________________________________##
# import pandas as pd
# pd.options.display.max_rows=999
# df=pd.read_csv('data.csv')
# # print(df.to_string())
# # print(df.head())    #only print first 5 rows
# print(df.head(100))    #only print first rows(0-100) 
# print(df.tail())    #only print last 5 rows(164-168)
# print(df.tail(20))  #only print last 20 rows(149-168)
 
##_______________________________________________________________##

# CLEANING OF DATA ,
# NULL values -> empty cells
# data in wrong format
# wrong data
# duplicate values


# import pandas as pd
# df=pd.read_csv('data.csv')
# # new_df=df.dropna()      #returns new dataset
# # print(new_df.to_string())

# df.dropna(inplace=True)
# print(df.to_string)
##_______________________________________________________________##
# import pandas as pd
# df=pd.read_csv('data.csv')
# df.fillna(6700,inplace=True)
# print(df.to_string())

# df["pulse"].fillna(345678,inplace=True)
# print(df.to_string())
##_______________________________________________________________##
##replace values mean by mean(),mode(),median()

# import pandas as pd
# df=pd.read_csv('data.csv')

# x=df["Pulse"].mean()
# df["Pulse"].fillna(x,inplace=True)
# print(df.to_string)

# y=df["Calories"].median()
# df["Calories"].fillna(x,inplace=True)
# print(df.to_string)

##_______________________________________________________________##

#--to handle wrong data
#-wrong data can ve handle by replacing with correct value
# import pandas as pd
# df=pd.read_csv('data.csv')
# # df.loc[79,'Duration']=50        #--change at particular position
# # for i in df.index:                #--change in all index containg wrong data
# #     if df.loc[i,'Duration'] > 100:
# #         df.loc[i,'Duration'] = 20

# for i in df.index:
#     if df.loc[i,'Duration'] > 100:
#         df.drop(i,inplace=True)
# print(df.to_string())
##_______________________________________________________________##

#--remove duplicate data
# import pandas as pd
# df=pd.read_csv('data.csv')
# # print(df.duplicated().to_string())
# df.drop_duplicates(inplace=True)
# print(df.to_string())

##_______________________________________________________________##
#wap to read a csv file and remove duplicate row

# import pandas as pd
# df=pd.read_csv('data.csv')
# # print(df.duplicated().to_string())
# df.drop_duplicates(inplace=True)
# print(df.to_string())

##_______________________________________________________________##

#wap to read a csv file and fill null values in any row with 55555

# import pandas as pd
# df=pd.read_csv('data.csv')
# df.fillna(55555,inplace=True)
# print(df.to_string())