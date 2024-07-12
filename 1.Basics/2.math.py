import sys
from typing import List
import math

sys.stdin = open('./input.txt', 'r')
sys.stdout = open('./output.txt', 'w')


def countDigits(n:int)->int:

    #Problem statement: Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.
 
    # Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.
 
    #Time Complexity: O(logn)
    #Space Complexity: O(logn)

    count = 0
    num = n
    digits = []
    while num>0:
        digit = num%10
        num = num//10
        digits.append(digit)
    digits = list(set(digits)) # removing the dupliocate digits

    for digit in digits:
        if digit!= 0 and n % digit == 0:
            count+=1
    return count

#LC7: Reverse Integer
def reverseInteger(n:int)->int:
    #Problem statement: Given a 32-bit signed integer, reverse digits of an integer.

    #Time Complexity: O(logn)
    #Space Complexity: O(1)

    INT_MAX = 2**31 -1
    INT_MIN = -2**31

    isNegative = False
    if n<0:
        isNegative = True
        n = -n
    reversed_num = 0
    while n >0:
        digit = n%10
        reversed_num  = reversed_num*10+ digit
        n = n//10
    
    if isNegative:
        reversed_num = -reversed_num
    
    if reversed_num <INT_MIN or reversed_num >INT_MAX:
        return 0
    
    return reversed_num


#LC9: Palindrome Number

def isPalindrome(n:int)->bool:

    #Problem statement: Given an integer n, return true if n is a palindrome. Otherwise, return false.

    #Time Complexity: O(logn)
    #Space Complexity: O(1)

    num = n
    if num<0:
        return False
    if num == 0:
        return True
    reverse_num = 0
    while num>0:
        digit = num%10
        reverse_num = reverse_num*10+digit
        num = num//10
    
    return reverse_num == n

def isArmStrongNum(n:int)->bool:
    #Problem statement: Given an integer n, return true if n is an Armstrong number. Otherwise, return false.

    num = n
    sum = 0
    while num>0:
        digit = num%10
        sum+=digit**3
        num = num//10
    
    return sum == n

def printAllDivisors(n:int)->List[int]:
   
    #TimeComplexity :O(n)
    #SpaceComplexity: O(n)

    divisors = []

    for i in range(1,n+1):
        if n%i ==0:
            divisors.append(i)
    return divisors 

def printAllDivisorsOptimized(n:int)->List[int]:
    #TimeComplexity: O(sqrt(n))
    divisors = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i ==0:
            divisors.append(i)
            if n//i not in divisors:
                divisors.append(n//i)
    return divisors


def sumOfDivisors(n:int)->int:
    #Problem statement: Given an integer n, return the sum of all divisors of n.

    #Time Complexity: O(n^2)
    #Space Complexity: O(1)

    sum = 0

    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j == 0:
                sum+=j

    return sum

def sumOfDivisorsOptimized(n:int)->int:
    
    #TimeComplexity: O(n)
    sum = 0

    for d in range(1,n+1):
        multiples = n//d
        sum += d*multiples
    
    return sum

def checkPrime(n:int)->bool:

    #TimeComplexity: O(n)
    #SpaceComplexity: O(1)

    counter = 0

    for i in range(1,n+1):
        if n%i ==0:
            counter+=1
            if counter > 2:
                return False
    if counter == 2:
        return True
    return False

def checkPrimeOptimized(n:int)->bool:
    counter = 0
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i == 0:
            counter+=1
            if counter > 2:
                return False
            if n//i != i:
                counter+=1

    return counter == 2

def gcd(a:int,b:int)->int:

    #TimeComplexity: O(min(a,b))

    gcd = 1

    if a > b:
        a,b = b,a

    for i in range(2,a+1):
        if a%i ==0 and b%i ==0:
            gcd = i
    return gcd

def gcd2(a:int,b:int)->int:

    #TimeComplexity: O(min(a,b))

    gcd = 1

    for i in range(min(a,b),0,-1):
        if a%i ==0 and b%i ==0:
            gcd = i
    return gcd

def gcdOptimized(a:int,b:int)->int:
    #TimeComplexity: O(log(min(a,b)))

    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b

def lcm(a:int,b:int)->int:
    
    #TimeComplexity: O(log(min(a,b)))

    return a*b//gcdOptimized(a,b)     





for line in sys.stdin:
    n = int(line.strip())
    # result = countDigits(n) 
    # result = reverseInteger(n)
    # result = isPalindrome(n)
    # result = isArmStrongNum(n)
    # result = sumOfDivisors(n)
    # result = sumOfDivisorsOptimized(n)
    # result = printAllDivisors(n)
    # result = printAllDivisorsOptimized(n)
    # result = checkPrime(n)
    result = checkPrimeOptimized(n)
    print(result)


sys.stdout.close()