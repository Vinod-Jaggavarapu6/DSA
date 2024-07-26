
import sys
from typing import List
import math

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# 1. Longest Subarray with sum K
# Given an array of integers, find the length of the longest subarray with sum equals to K.
def longestSubArrayBF(arr:List[int],k:int):
    # Brute Force: O(n^3)

    n = len(arr)
    i = 0
    maxLen = 0

    while i<n:
        j = i
        while j<n:
            if sum(arr[i:j+1]) == k:
                maxLen = max(maxLen,j-i+1)
            j+=1
        i+=1

    return maxLen

def longestSubArrayBF2(arr:List[int],k:int):
    # Brute Force: O(n^2)
    n = len(arr)
    i = 0
    maxLen = 0

    while i<n:
        j = i
        sub_sum = 0
        while j<n:
            sub_sum +=arr[j]
            if sub_sum ==k:
                maxLen = max(maxLen,j-i+1)
            j+=1
        i+=1

    return maxLen

def longestSubArray(arr:List[int],k:int):
    # Using Hashing: O(n)
    #Space:O(n)

    n = len(arr)
    prefix_sum = 0
    maxLen = 0
    prefix_map = {}

    for i in range(n):
        prefix_sum +=arr[i]
        if prefix_sum == k:
            maxLen = max(maxLen,i+1)
        
        if prefix_sum - k in prefix_map:
            maxLen = max(maxLen,i-prefix_map[prefix_sum-k])
        
        # Store the first occurence of prefix_sum as it will give the longest subarray (if zeros exists may update the index)
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
        

    return maxLen

def longestSubArrayOptimal(arr:List[int],k:int):
    #Using 2 pointer approach
    #Space:O(1)
    n = len(arr)
    i=j=0
    maxLen = 0
    sub_sum = 0

    while j < n:
        sub_sum +=arr[j]
        if sub_sum == k:
            maxLen = max(maxLen,j-i+1)
        elif sub_sum >k:
            while sub_sum >k:
                sub_sum -= arr[i]
                i+=1
            if sub_sum == k:
                maxLen = max(maxLen,j-i+1)
        j+=1
    
    while i < n:
        sub_sum -= arr[i]
        i+=1
        if sub_sum == k:
            maxLen = max(maxLen,j-i+1)


    return maxLen


#LC-1 :2 Sum

def twoSumBF(nums:List[int],target:int)->List[int]:
    #TC:O(n^2)
    #SC:O(1)
    n = len(nums)

    for i in range(n-1):
        
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]

#LC-1 :2 Sum
#   
def twoSumOptimal(nums:List[int],target:int)->List[int]:
    #Using Hashmap
    #TC: O(N)
    #SC:O(N)

    map = {}

    for index,num in enumerate(nums):
        rem = target-num
        if rem in map:
            return [map[rem],index]
        
        map[num] = index 

#LC-1 :2 Sum
def twoSum(nums:List[int],target:int)->List[int]:
    sorted_nums = [(num,index) for index,num in enumerate(nums)]

    sorted_nums.sort(key = lambda x:x[0])

    n = len(nums)
    left,right = 0,n-1

    while left<right:
        if sorted_nums[left][0]+sorted_nums[right][0] == target:
            return [sorted_nums[left][1],sorted_nums[right][1]]
        elif sorted_nums[left][0]+sorted_nums[right][0] < target:
            left+=1
        else:
            right-=1


#LC-75: Sort Colors
def sortColorsBF(nums:List[int])->List[int]:
    #TC: O(n)
    #SC: O(n)

    map = {0:0,1:0,2:0}

    for num in nums:
        map[num]+=1

    i=0

    for j in range(3):
        while map[j]:
            nums[i] = j
            i+=1
            map[j] -=1
    
    return nums

#LC-75: Sort Colors
def sortColors(nums:List[int])->List[int]:
    #Dutch National Flag Algorithm
    #Intuition: We maintain 3 pointers red,white,blue. Red points to 0, white points to 1 and blue points to 2, we swap the elements based on the pointers. red and white are incremented and blue is decremented. 

    #TC:O(n)
    #SC:O(1)

    red,white,blue = 0,0,len(nums)-1

    while white <= blue:
        if nums[white] == 0:
            #swap with red and increment red
            nums[red],nums[white] = nums[white],nums[red]
            red +=1
            white+=1
        elif nums[white] == 2:
            nums[blue],nums[white] = nums[white],nums[blue]
            blue-=1
            #at blue it can be either 0,1,2 so we check again white => no increment of white
       
        else:
            white+=1

    return nums

#LC-169: Majority Element
def majorityElementBF1(nums:List[int])->int:
    #TC:O(n^2)
    #SC:O(n)

    n = len(nums)
    seen = set()

    for i in range(n):
        num = nums[i]
        if num not in seen:
            count = 0
            for j in range(n):
                if nums[j] == num:
                    count+=1
            if count > n//2:
                return num
        seen.add(num)
        
#LC-169: Majority Element

def majorityElementBF(nums:List[int])->int:
    #TC:O(n)
    #SC:O(n)

    n = len(nums)
    count_map = {}

    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num]+=1

    for key in count_map:
        if count_map[key] > n//2:
            return key

#LC-169: Majority Element

def majorityElement(nums:List[int])->int:
    #Boyer Moore Voting Algorithm - Intuition: We maintain a candidate and count. If count is 0 we update the candidate to the current element. If the element is same as candidate we increment the count else we decrement the count. We then iterate the array again to check if the candidate is the majority element.

    #TC:O(n)
    #SC:O(1)

    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count+=1
        elif num == candidate:
            count+=1
        else:
            count-=1
    count = 0
    for num in nums:
        if num  == candidate:
            count+=1
    
    if count > len(nums)//2:
        return candidate
    
    return None


for line in sys.stdin:
    arr = list(map(int,line.split(',')))
    # k = int(input())
    # print(longestSubArrayBF(arr,k))
    # print(longestSubArrayBF2(arr,k))
    # print(longestSubArray(arr,k))
    # print(longestSubArrayOptimal(arr,k))
    # print(twoSumBF(arr,k))
    # print(twoSumOptimal(arr,k))
    # print(twoSum(arr,k))
    # print(sortColorsBF(arr))
    # print(sortColors(arr))
    # print(majorityElementBF(arr))
    # print(majorityElementBF1(arr))
    print(majorityElement(arr))
sys.stdout.close()