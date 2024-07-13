import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

def printNos(n:int)->None:
    if n == 0:
        return
    printNos(n-1)
    print(n,end=" ")

def printRevNos(n:int)->None:
    if n ==0:
        return
    print(n,end=" ")
    printRevNos(n-1)

def sumOfSeries(n:int,sum=0)->int:
    if n == 0:
        return sum
    sum += n**3
    return sumOfSeries(n-1,sum)
    
def factorialNumbers(n:int)->int:
    if n == 0:
        return 1
    return n*factorialNumbers(n-1)

def factorialNumbers2(n:int)->None:
    for i in range(1,n+1):
        f = factorialNumbers(i)
        if f > n:
            break
        print(f,end=" ")

def reverseArray(arr:list[int]) -> list[int]:
    n = len(arr)
    def helper(arr,i):
        if i >= n//2:
            return
        arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
        helper(arr,i+1)
    
    helper(arr,0)

    return arr

#LC-125 
def isPalindrome(s:str)->bool:
    alnum_str =''

    for char in s:
        if char.isalnum():
            alnum_str+=char.lower()
    
    left = 0
    right = len(alnum_str)-1

    while left < right:
        if alnum_str[left] != alnum_str[right]:
            return False
        left +=1
        right -=1

    return True

def isPalindromeRecursive(s:str)->bool:
    alnum_str = ''

    for char in s:
        if char.isalnum():
            alnum_str+= char.lower()

    start = 0
    end = len(alnum_str)-1
    
    def helper(alnum_str,start,end):
        if start >= end:
            return True
        if alnum_str[start] != alnum_str[end]:
            return False
        
        return helper(alnum_str,start+1,end-1)
    
    return helper(alnum_str,start,end)
        
#LC-509 (recursive)
def fibonacciNumberRecursive(n:int)->int:
    if n == 0 or n==1:
        return n
    return fibonacciNumberRecursive(n-1)+fibonacciNumberRecursive(n-2)

#LC-509 (Iterative)
def fibonacciNumber(n:int)->int:

    fib_arr = [0,1]
    if n == 0 or n == 1:
        return fib_arr[n]

    for i in range(2,n+1):
        fib_arr.append(fib_arr[i-1]+fib_arr[i-2])
    
    return fib_arr[-1]

#LC-509 (Memoized)
def fibonacciNumberMemo(n:int)->int:
    memo = {0:0,1:1}

    def helper(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = helper(n-1)+helper(n-2)

        return memo[n]
        
    return helper(n)
        






for line in sys.stdin:
    n = int(line.strip())
    # printNos(n)
    # print()
    # printRevNos(n)
    # print()
    # print(sumOfSeries(n))
    # print(factorialNumbers(n))
    # factorialNumbers2(n)
    # arr = list(map(int,line.strip().split(" ")))
    # print(reverseArray(arr))
    # s = line.strip()
    # print(isPalindromeRecursive(s))
    # print(fibonacciNumberRecursive(n))
    # print(fibonacciNumber(n))
    print(fibonacciNumberMemo(n))
    
sys.stdout.close()
