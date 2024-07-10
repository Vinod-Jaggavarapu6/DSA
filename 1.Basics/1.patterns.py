import sys

sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def print_pattern1(n:int) -> None:
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

def print_pattern2(n:int) -> None:
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()

def print_pattern3(n:int)->None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()

def print_pattern4(n:int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")
        print()

def print_pattern5(n:int) -> None:
    for i in range(n):
        for j in range(n-i,0,-1):
            print("*",end="")
        print()
    
def print_pattern6(n:int)->None:
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end="")
        print()

def print_pattern7(n: int) -> None:
    for i in range(n):
        s =''
        for j in range(n-i-1):
            s+=" "
        for j in  range(2*i+1):
            s+="*"
        for j in range(n-i-1):
            s+=" "
        print(s,end='\n')

def print_pattern8(n:int) ->None:
    for i in range(n):
        for j in range(i):
            print(" ",end='')
        for j in range((n-i)*2-1):
            print("*",end="")
        for j in range(i):
            print(" ",end='')
        print()

def print_pattern9(n:int)->None:
    for i in range(2*n-1):
        stars = 0
        if i<n:
            stars = i+1
        else:
            stars = 2*n-i-1
        
        for j in range(stars):
            print("*",end='')
    
        print()

# def print_pattern10(n:int) ->None:
#     for i in range(1,n+1):
#         c =''
#         if i%2 == 0:
#             c = '0'
#         else:
#             c = '1'

#         for j in range(i):
#             print(c,end=" ")

#             if c == '0':
#                 c = '1'
#             else:
#                 c = '0'
#         print()

def print_pattern10(n:int) ->None:
    for i in range(1,n+1):
        c = 0
        if i%2 != 0:
            c = 1

        for j in range(i):
            print(c,end=" ")
            c = 1-c

        print()

def print_pattern11(n:int)->None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for k in range(2*(n-i)):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()


def print_pattern12(n:int)->None:
    start = 1
    for i in range(1,n+1):
        for j in range(i):
            print(start,end=" ")
            start+=1
        print()


def print_pattern13(n:int)-> None:
    

    for i in range(1,n+1):
        ch = 'A'
        for j in range(i):
            print(ch,end="")
            ch = chr(ord(ch)+1)
        print()


def print_pattern14(n:int)->None:
    for i in range(n,0,-1):
        ch = 'A'
        for j in range(i):
            print(ch,end="")
            ch = chr(ord(ch)+1)
        print()

def print_pattern15(n:int)->None:
    ch = 'A'
    for i in range(1,n+1):

        for j in range(i):
            print(ch,end="")
        print()
        ch = chr(ord(ch)+1)

def print_pattern16(n:int)->None:
    for i in range(1,n+1):
        for j in range(n-i-1):
            print(" ",end="")
        ch = 'A'
        for k in range(i):
            print(ch,end="")
            ch = chr(ord(ch)+1)
        ch = 'A'
        for l in range(i-1):
            print(ch,end='')
            ch = chr(ord(ch)+1)
        for m in range(n-i-1):
            print(" ",end="")
        print()


def print_pattern17(n:int) -> None:
     ch = 'E'
     for i in range(1,n+1):
        c = ch
        for j in range(i):
            print(c,end ='')
            c = chr(ord(c)+1)
        print()
        ch = chr(ord(ch)-1)


# def  print_pattern18(n:int) -> None:
#     for i in range(1,2*n+1):
#         if i <=n:
#             for j in range(n-i+1):
#                 print("*",end='')
#             for k in range((i-1)*2):
#                 print(" ",end="")
#             for j in range(n-i+1):
#                 print("*",end='')
#         else:
#             for j in range(i-n):
#                 print("*",end='')
#             for k in range((2*n-i)*2):
#                 print(" ",end="")
#             for j in range(i-n):
#                 print("*",end='')
#         print()

def  print_pattern18(n:int) -> None:
    for i in range(1,2*n+1):

        if i <=n:
            stars = n-i+1
            spaces = 2*(i-1)
        else:
            stars = i-n
            spaces = 2*(2*n-i)
           
        print("*"*stars+" "*spaces+"*"*stars+'\n')


# def print_pattern19(n:int)->None:
#     for i in range(1,2*n):
#         if i <=n:
#             for j in range(i):
#                 print('*',end='')
#             for k in range(2*(n-i)):
#                 print(" ",end="")
#             for j in range(i):
#                 print('*',end='')

#         else:
#             for j in range(2*n-i):
#                 print('*',end='')
#             for k in range(2*(i-n)):
#                 print(" ",end="")
#             for j in range(2*n-i):
#                 print('*',end='')
#         print()

def print_pattern19(n:int)->None:
    for i in range(1,2*n):
        if i <=n:
            stars = i
            spaces = 2*(n-i)

        else:
            stars = 2*n-i
            spaces = 2*(i-n)
        
        print("*"*stars+" "*spaces+"*"*stars+'\n')

        
            
def print_pattern20(n:int)->None:
    for i in range(n):
        for j in range(n):
            if i ==0 or i==n-1 or j==0 or j==n-1:
                print('*',end='')
            else:
                print(" ",end='')
        print()

def print_pattern21(n:int) -> None:
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            bottom = (2*n-2)-j
            left = j
            right = (2*n-2)-j

            print(n - min(top,bottom,left,right),end=" ")
        print()
             
 

        

        







input_n = int(input().strip())

# print_pattern1(input_n)

# print_pattern2(input_n)

# print_pattern3(input_n)

# print_pattern4(input_n)

# print_pattern5(input_n)

# print_pattern6(input_n)

# print_pattern7(input_n)

# print_pattern8(input_n)

# print_pattern9(input_n)

# print_pattern10(input_n)

# print_pattern11(input_n)

# print_pattern12(input_n)

# print_pattern13(input_n)

# print_pattern14(input_n)

# print_pattern15(input_n)

# print_pattern16(input_n)

# print_pattern17(input_n)

print_pattern18(input_n)

# print_pattern19(input_n)

# print_pattern20(input_n)

# print_pattern21(input_n)

sys.stdout.close()

