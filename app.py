
import csv
import sys

def print3largest(arr, arr_size):
 
    if (arr_size < 3):
     
        print("There are only two food items in the data ")
        return
     
    third = first = second = -sys.maxsize
    t=f=s=""
    for i in arr:
     

        if (arr[i] > first):
         
            third = second
            t = s
            second = first
            s = f
            first = arr[i]
            f = i
         
        elif (arr[i] > second):
         
            third = second
            t = s
            second = arr[i]
            s = i
         
        elif (arr[i] > third):
            third = arr[i]
            t = i
     
    print("top three most eaten food are\n1.",
                  f,"->",first,"\n2.", s,"->",second,"\n3.", t,"->",third)

def TopFoodFunc(filename):
    file = open(filename)
    myarray = csv.reader(file)
    err = {}
    food = {}
    for row in myarray:
        if(row[0] in err):
            print("error!!! eater_id is not unique",row[0])
            return
        else:
            err[row[0]] = 1
 #   for row in myarray:
        if(row[1] in food):
            food[row[1]] = food[row[1]] + 1
          #  print(food[row[1]])
        else:
            food[row[1]] = 1
    #print((food),"\n")
    print3largest(food,len(food))
    
print("\ntest case 1: \n")    
TopFoodFunc("test1.csv")
print("\ntest case 2: \n")  
TopFoodFunc("test2.csv")
print("\ntest case 3: \n")  
TopFoodFunc("test3.csv")
z= input()