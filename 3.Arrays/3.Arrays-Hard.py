import sys
from typing import List
import math

sys.stdin = open("input.txt",'r')

sys.stdout = open("output.txt",'w')

def factorial(n:int)->int:
    res = 1
    for i in range(n,1,-1):
        res *= i
    return res

def nCr(n:int,r:int)->int:
    res = 1
    res *= factorial(n)
    res /= (factorial(n-r)*factorial(r))
    
    return int(res)

def nCrV2(n:int,r:int)->int:
    res = 1

    for i in range(r):
        res *= (n-i)
        res /= (i+1)
    return int(res)


def pascalTriangleV1(row:int,col:int)->int:

    return nCrV2(row-1,col-1)



def pascalTriangle(numRows:int)->List[List[int]]:
    output = [[1 for j in range(i) ] for i in range(1,numRows+1)]

    for i in range(2,numRows):
        j = 1
        p1 = 0
        p2 = 1

        while j < i:
            output[i][j] = output[i-1][p1] + output[i-1][p2]
            j+=1
            p1+=1
            p2+=1

    return output

def pascalNthRowV1(row:int)->List[int]:
    res = []
    for col in range(row):
        ncr = nCrV2(row-1,col)
        res.append(ncr)
    return res

def pascalNthRowV2(rows:int)->List[int]:
    nth_row = []
    ans = 1
    nth_row.append(ans)

    for col in range(1,rows):
        ans *= (rows-col)
        ans /= col
        nth_row.append(int(ans))
    
    return nth_row

def generatePascalTriangle(numRows:int)->List[List[int]]:
    res = []
    for row in range(1,numRows+1):
        res.append(pascalNthRowV2(row))

    return res

def majorityElement(nums:List[int])->List[int]:
    res = []
    n = len(nums)

    for i in range(n):
        if nums[i] not in res:
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count+=1
            
            if count > math.floor(n/3):
                res.append(nums[i])

    return res


def majorityElementHashing(nums:List[int])->List[int]:
    res = []
    count_map = {}
    n = len(nums)

    for num in nums:
        if num in count_map:
            count_map[num]+=1
        else:
            count_map[num] = 1

    for num in count_map.keys():
        if count_map[num] > math.floor(n/3):
            res.append(num)
    
    return res

def majorityElementHashingV2(nums:List[int])->List[int]:
    res = []
    n = len(nums)
    target_count = math.floor(n/3)
    count_map = {}

    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num]+=1

        if count_map[num] > target_count and num not in res:
            res.append(num)

    return res
    
def majorityElementOptimal(nums:List[int])->List[int]:
    
    min_count = math.floor(len(nums)/3)
    cnt1 = cnt2 = 0
    el1=el2 = None

    for num in nums:
        if cnt1 == 0 and num != el2:
            el1 = num
            cnt1 = 1
        elif cnt2 == 0 and num != el1:
            el2 = num
            cnt2 = 1
        elif num == el1:
            cnt1+=1
        elif num == el2:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    
    cnt1 = 0
    cnt2 = 0

    for num in nums:
        if num == el1:
            cnt1+=1
        elif num == el2:
            cnt2+=1

    res = []
    if cnt1 > min_count:
        res.append(el1)

    if cnt2 > min_count:
        res.append(el2)
    
    return res







for line in sys.stdin:
    arr = list(map(int,line.split(',')))
    # k = int(line)
    # res = line.strip().split(',')
    # row = int(res[0])
    # col = int(res[1])
    # print(pascalTriangleV1(row,col))
    # print(pascalTriangle(k))
    # print(pascalNthRowV1(k))
    # print(pascalNthRowV2(k))
    # print(generatePascalTriangle(k))
    # print(majorityElement(arr))
    # print(majorityElementHashing(arr))
    # print(majorityElementHashingV2(arr))
    print(majorityElementOptimal(arr))

sys.stdout.close()