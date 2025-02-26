# a)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# b)
# 1
# 3
# 5
# 7
# 9
# 11

# c)
# 43
# 40
# 37
# 34

# d)
# 0 0 0 0
# 0 1 2 3
# 0 2 4 6
# 0 3 6 9

# e)

# 0 1
# 0 2
# 0 3
# 0 4
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 4 

# f)

# 2,4,6,8
# 4,6,8
# 6,8
# 8

# g)

# 0
# 0 2
# 0 2 4
# 0 2 4 6


# Problem 2:
# highest_number=0
# number_of_val=int(input("Enter the number of values: "))
# for i in range(1,number_of_val+1):
#     new_number=int(input("Enter your values:"))
#     highest_number=max(highest_number,new_number)
# print("The highest number is",highest_number)


# Problem 3:
# user_string=input("Enter a string to be printed (in the format [text]-[text]...)")
# for char in user_string:
#     if char=="-":
#         print()
#     else:
#         print(char,end="")




# Problem 4:
# arrowhead

# user_input=int(input("Enter the number of lines for pattern: "))
# for i in range(1,user_input*2):
#     if i<=user_input:
#         print("*"*i)
#     else:
#         print(("*"*(user_input*2-i)))


# Problem 5:
symbol=''
width=int(input("Python needs to tell you a secret. How many characters wide can it's messag be?"))
for i in range(1,width*3+1):
    for j in range(1,width+1):

        if i<=width or i>width*2:
            symbol="X"
            for z in range (i,width+2-i):
                print(" "*(i-1),end="")
                if z==i or z==width+1-1:
                    print(symbol,end="")
                else:
                    print(" ",end="")
            print()
        else:
            symbol="o"
            for z in range (i,width+2-i):
                if z==i or z==width+1-1:
                    print(symbol,end="")
                else:
                    print(" ",end="")
    print()
print()
print("- From Python")
