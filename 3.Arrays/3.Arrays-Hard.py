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

#LC: 118. Pascal's Triangle
def pascalTriangleV1(row:int,col:int)->int:
    return nCrV2(row-1,col-1)


#LC: 118. Pascal's Triangle
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

#LC: 118. Pascal's Triangle
def pascalNthRowV1(row:int)->List[int]:
    res = []
    for col in range(row):
        ncr = nCrV2(row-1,col)
        res.append(ncr)
    return res

#LC: 118. Pascal's Triangle
def pascalNthRowV2(rows:int)->List[int]:
    nth_row = []
    ans = 1
    nth_row.append(ans)

    for col in range(1,rows):
        ans *= (rows-col)
        ans /= col
        nth_row.append(int(ans))
    
    return nth_row

#LC: 118. Pascal's Triangle
def generatePascalTriangle(numRows:int)->List[List[int]]:
    res = []
    for row in range(1,numRows+1):
        res.append(pascalNthRowV2(row))

    return res

#LC: 229. Majority Element II
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

#LC: 229. Majority Element II
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

#LC: 229. Majority Element II

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
    
#LC: 229. Majority Element II

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

#LC: 15 3Sum

def threeSum(nums:List[int])->List[List[int]]:
    #TC:O(N^3)
    triplets = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] == 0:
                    print(i,j,k)
                    sorted_triplet = tuple(sorted([i,j,k]))
                    triplets.add(sorted_triplet)

    return [list(item) for item in triplets]

def threeSumHashing(nums:List[int])->List[List[int]]:
    triplets = set()
    n = len(nums)

    for i in range(n):
        hash_map = {}
        for j in range(i+1,n):
            k_val = -(nums[i]+nums[j])

            if k_val in hash_map:
                triplet = tuple(sorted([i,j,hash_map[k_val]]))
                triplets.add(triplet)

            hash_map[nums[j]] = j
                

    return [list(triplet) for triplet in triplets]

def threeSum2Pointer(nums:List[int])->List[List[int]]:
    n = len(nums)
    triplets = []

    nums.sort()

    for i in range(n):
        if i == 0 or nums[i] != nums[i-1]:
            j = i+1
            k = n-1

            while j < k:
                sum = nums[i]+nums[j]+nums[k]

                if  sum == 0:
                    triplets.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif sum < 0:
                    j+=1
                elif sum > 0:
                    k-=1

    return triplets

#LC: 18 4Sum
def fourSumBF(nums:List[int],target:int)->List[List[int]]:
    #TC:O(N^4)
    #SC:O(No of quadruplets)

    n= len(nums)
    res=set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l] == target:
                        t = tuple(sorted([nums[i],nums[j],nums[k],nums[l]]))
                        res.add(t)
    
    return [list(t)  for t in res]

def fourSumHashing(nums:List[int],target:int)->List[List[int]]:
    #TC:O(N^3)
    #SC:O(no.of quadruplets)

    n = len(nums)
    res = set()

    for i in range(n):
        for j in range(i+1,n):
            hash_set = set()
            for k in range(j+1,n):
                l_val = target - (nums[i]+nums[j]+nums[k])

                if l_val in hash_set:
                    t = tuple(sorted([nums[i],nums[j],nums[k],l_val]))
                    res.add(t)
                
                hash_set.add(nums[k])
    
    return [list(t) for t in res]

def fourSum2Pointer(nums:List[int],target:int)->List[List[int]]:
    n = len(nums)
    nums.sort()
    res = []
    i = 0
    while i < n:

        if i > 0 and nums[i] == nums[i-1]:
            i+=1
            continue

        j = i+1

        while j < n:

            if j > i+1 and nums[j] == nums[j-1]: 
                j+=1
                continue

            k = j+1
            l = n-1

            while k < l:

                sum = nums[i]+nums[j]+nums[k]+nums[l]

                if sum > target:
                    l-=1

                elif sum < target:
                    k+=1

                else:
                    res.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k < l  and nums[k] == nums[k-1]:
                        k+=1
                    
                    while k < l  and nums[l] == nums[l+1]:
                        l-=1
            j+=1
        i+=1
                    

    return res
                    
#https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?category%5B%5D=Hash&company%5B%5D=Amazon&page=1&query=category%5B%5DHashcompany%5B%5DAmazonpage1company%5B%5DAmazoncategory%5B%5DHash&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-subarray-with-0-sum

# Largest subarray with 0 sum

def maxLenBF(nums:List[int])->int:
    #TC:O(n^3)
    #SC:O(1)

    n = len(nums)
    max_len = 0

    for i in range(n):
        for j in range(n):
            sub_arr = nums[i:j+1]
            if sum(sub_arr) == 0:
                max_len = max(max_len,len(sub_arr))
    
    return max_len

def maxLenBF1(nums:List[int])->int:
    #TC: O(N^2)
    #SC: O(1)

    n = len(nums)
    max_len = 0

    for i in range(n):
        sub_sum = 0
        for j in range(i,n):
            sub_sum += nums[j]

            if sub_sum == 0:
                max_len = max(max_len,j-i+1)

    return max_len


def maxLenOptimal(nums:List[int])->int:
    #TC:O(N)
    #SC:O(N)

    n = len(nums)
    max_len = 0

    prefix_sum = 0

    prefix_map = {}

    for i in range(n):
        prefix_sum +=nums[i]

        if prefix_sum == 0:
            max_len = i+1
        else:
            if prefix_sum in prefix_map:
                sub_len = i  - prefix_map[prefix_sum]
                max_len = max(max_len,sub_len)

            else:
                prefix_map[prefix_sum] = i

    return max_len


def subArraysWithXOR(nums:List[int],k:int)->int:
    #TC:O(N^2)
    #SC:O(1)

    n = len(nums)
    count = 0

    for i in range(n):
        curr = 0
        for j in range(i,n):
            curr ^= nums[j]
            if curr == k:
                count +=1
    
    return count
            
def subArrayWithXOROptimal(nums:List[int],k:int)->int:
    n = len(nums)
    count = 0

    xor_map = {0:1}

    curr_xor = 0

    for i in range(n):
        curr_xor ^= nums[i]

        if curr_xor^k in xor_map:
            count+=xor_map[curr_xor^k]

        if curr_xor in xor_map:
            xor_map[curr_xor] += 1
        else:
            xor_map[curr_xor] = 1

    return count

#LC:56 Merge Intervals
def mergeIntervals(intervals:List[List[int]])->List[List[int]]:
    #TC: O(NlogN+2N)
    #SC:O(N)

    n = len(intervals)
    intervals.sort(key= lambda x:x[0])

    res = []

    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]

        if len(res) > 0  and end <= res[-1][1]:
            continue

        for j in range(i+1,n):

            if intervals[j][0] <=end:
                end = max(end,intervals[j][1])
            else:
                break
        
        res.append([start,end])
   
    return res

#LC:56 Merge Intervals
def mergeIntervalsOptimal(intervals:List[List[int]])->List[List[int]]:
    #TC:O(NlogN+N)
    #SC:O(N)

    n = len(intervals)
    intervals.sort()

    res = []

    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]

        if len(res) == 0 or start > res[-1][1]:
            res.append([start,end])
            continue
    
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1],end)


    return res





# arr = [[1,3],[2,6],[8,9],[9,11],
#        [8,10],[2,4],[15,18],[16,17]]

# print(mergeIntervalsOptimal(arr))

for line in sys.stdin:
    # arr = list(map(int,line.split(',')))
    # k = int(input())
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
    # print(majorityElementOptimal(arr))
    # print(threeSum(arr))
    # print(threeSumHashing(arr))
    # print(threeSum2Pointer(arr))
    # print(fourSumBF(arr,k))
    # print(fourSumHashing(arr,k))
    # print(fourSum2Pointer(arr,k))
    # print(maxLenBF(arr))
    # print(maxLenBF1(arr))
    # print(maxLenOptimal(arr))
    # print(subArraysWithXOR(arr,k))
    # print(subArrayWithXOROptimal(arr,k))
    pass

sys.stdout.close()