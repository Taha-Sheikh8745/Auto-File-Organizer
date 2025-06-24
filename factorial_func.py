# def factorial(n):

#     if(n == 1 or n == 0):

#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter any number: "))
# print(f"The factorial of this number is: {factorial(n)}")


# Greatest Number

# def greatest(a,b,c):

#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a = 5
# b = 55
# c = 20



#Farhenheit To Celsius

def f_to_c(f):
        return 5*(f-32)/9

f = int(input("Enter Temperature in F: "))
c= f_to_c(f)

print(f"{round(c , 2)}°C")
 
