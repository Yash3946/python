a=10
try:
 b=12
except IndentationError:
    print("not possible")
try:    
    print(a+c)
except NameError:
    print("name error")