# num = int(input("Enter any number"))

# for i in range(1,11):
#     print(f"{num} x {i} = {num*i} ")


# l = ["Taha", "Ali", "Tahir","Bilal","Tommy"]

# for name in l:
#     if(name.startswith("T")):
#         print(f"Hello {name}")



# num = int(input("Enter any number"))

# i = 1
# while(i<11):
#     print(f"{num} x {i} = {num*i} ")
#     i+=1



num = int(input("Enter any number "))

for i in range(2,num):
    if(num%i) == 0:
        print("Number is not Prime")
        break

else:   
    print("Number is Prime")     


