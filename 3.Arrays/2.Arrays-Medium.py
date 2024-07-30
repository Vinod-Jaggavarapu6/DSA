
import sys
from typing import List
import math

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# 1. Longest Subarray with sum K
# Given an array of integers, find the length of the longest subarray with sum equals to K.
def longestSubArrayBF(arr:List[int],k:int):

    #Intuition: We generate all subarrays and check if the sum of the subarray is equal to k. We maintain a maxLen to store the maximum length of the subarray.
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

    #Intuition: We generate all subarrays and check if the sum of the subarray is equal to k. We maintain a maxLen to store the maximum length of the subarray.
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

#LC-53: Maximum Subarray

def maxSubArray(nums:List[int])->int:
    #TC:O(n^3)
    #SC:O(1)

    maxSum = -math.inf
    n = len(nums)
    if n ==1:
        return nums[-1]
    
    for i in range(n):
        for j in range(i,n):
            subSum = sum(nums[i:j+1])
            maxSum = max(subSum,maxSum)

    return maxSum

#LC-53: Maximum Subarray
def maxSubArrayBF2(nums:List[int])->int:
    #TC:O(n^2)
    #SC: O(1)

    maxSum = -math.inf
    n = len(nums)

    for i in range(n):
        subSum = 0
        for j in range(i,n):
            subSum += nums[j]
            maxSum = max(maxSum,subSum)

    return maxSum

#LC-53: Maximum Subarray

def maxSubArrayOptimal(nums:List[int])->int:
    maxSum = -math.inf

    subSum = 0

    for num in nums:
        if subSum < 0:
            subSum = 0
        subSum +=num
        maxSum = max(maxSum,subSum)
    
    return maxSum

#maxSubArray Follow-up

def maxSubArray2(nums:List[int])->int:
    maxSum = -math.inf

    subSum = 0

    subStart = 0
    subEnd = 0
    start = 0

    for index,num in enumerate(nums):
            

        if subSum < 0:
            subSum = 0
            start = index

        subSum +=num
        
        if subSum > maxSum:
            maxSum = subSum
            subStart, subEnd = start,index
    
    return nums[subStart:subEnd+1]

#LC-121: Best time to buy and sell stock
def maxProfitBF(prices:List[int])->int:
    #TC:O(n^2)
    #SC:O(1)

    max_profit = 0
    n = len(prices)

    for i in range(n):
        for j in range(i+1,n):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]

    return max_profit

#LC-121: Best time to buy and sell stock

def maxProfitOptimal(prices:List[int]):
    #TC:O(N)
    #SC:O(1)

    profit = 0
    n = len(prices)
    min_buy = prices[0]

    for i in range(1,n):
        cost = prices[i] - min_buy
        profit = max(profit,cost)
        min_buy = min(min_buy,prices[i])

    return profit

#LC-2149: Rearrange Array Elements by Sign

def rearrangeArrayBF(nums:List[int])->List[int]:

    #TC:O(2N) -- 2 passes
    #SC:O(N)

    pos_nums = []
    neg_nums = []
    
    for num in nums:
        if num <0:
            neg_nums.append(num)
        else:
            pos_nums.append(num)
    
    # res = []

    # for i in range(len(pos_nums)):
    #     res.extend([pos_nums[i],neg_nums[i]])
    
    # return res

    for i in range(len(pos_nums)):
        nums[2*i] = pos_nums[i]
        nums[2*i+1] = neg_nums[i]
    
    return nums

#LC-2150: Rearrange Array Elements by Sign

def rearrangeArrayOptimal(nums:List[int])->List[int]:
    pos_index = 0
    neg_index = 1
    res = [None]*len(nums)

    for num in nums:
        if num < 0:
            res[neg_index] = num
            neg_index += 2
        elif num > 0:
            res[pos_index] = num
            pos_index  += 2
    return res

def rearrangeArrayV2(nums:List[int])->list[int]:
    pos_nums = []
    neg_nums = []
    
    for num in nums:
        if num >0 :
            pos_nums.append(num)
        else:
            neg_nums.append(num)
    
    i = 0
    while i<len(pos_nums) and i<len(neg_nums):
        nums[2*i] = pos_nums[i]
        nums[2*i+1] = neg_nums[i]
        i+=1

    j = 2*i
    while i<len(pos_nums):
        nums[j] = pos_nums[i]
        i+=1
        j+=1
    
    while i <len(neg_nums):
        nums[j] = neg_nums[i]
        i+=1
        j+=1

    return nums

def findAllPermutations(nums:List[int])->List[List[int]]:

    #Intuition: We use backtracking to find all permutations
    #TC:O(n!)
    #SC:O(n!)

    result = []
    def helper(permutation=[],map={}):
        if len(permutation) == len(nums):
            result.append(permutation[:])
            return
        
        for i in range(len(nums)):
            if i not in map:
                permutation.append(nums[i])
                map[i] = 1
                helper(permutation,map)
                permutation.pop()
                del map[i]
                
    helper()

    return result

def findAllPermutationsOptimal(nums:List[int])->List[List[int]]:
    #Intitution: We swap the elements and backtrack to find all permutations
    #TC:O(n!)
    #SC:O(n!)

    permutations = []
    def helper(index=0):

        if index == len(nums):
            permutations.append(nums[:])
            return

        for i in range(index,len(nums)):
            nums[i],nums[index] = nums[index],nums[i]
            helper(index+1)
            nums[i],nums[index] = nums[index],nums[i]

    helper()
    return permutations


#LC-31: Next Permutation

def nextPermutation(nums:List[int]):
    #Brute Force: Find all permutations and return the next permutation
    #TC:O(n!)
    #SC:O(n!)
    permutations = findAllPermutationsOptimal(nums)
    permutations.sort()

    for index,p in enumerate(permutations):
        if p == nums:
            return permutations[(index+1)%len(permutations)]
        
#LC-31: Next Permutation

def nextPermutation2(nums:List[int]):
    #INtution: We find the first decreasing element from the right and swap it with the next greater element from the right. We then reverse the array from the next element of the first decreasing element to the end of the array.
    #TC:O(n)
    #SC:O(1)

    n = len(nums)

    index = -1

    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            index = i
            break
    
    if index == -1:
        return nums[::-1]
    
    for j in range(n-1,index-1,-1):
        if nums[j] > nums[index]:
            nums[index],nums[j] = nums[j],nums[index]
            break

    i = index+1
    j = n-1

    while i < j:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j-=1
    
    return nums


def leaders(nums:list[int])->List[int]:
    leaders_list = []
    n = len(nums)

    for index,num in enumerate(nums):
        isLeader = True
        for right in range(index+1,n):
            if nums[right] > num:
                isLeader = False
                break
        if isLeader:
            leaders_list.append(num)

    return leaders_list

def leadersOptimal(nums:List[int])->List[int]:
    n = len(nums)
    max = -math.inf
    leader_list = []

    for i in range(n-1,-1,-1):
        if nums[i] >= max:
            leader_list.append(nums[i])
            max = nums[i]
    
    leader_list.sort(reverse=True)

    return leader_list

#LC-128: Longest Consecutive Sequence
def longestConsecutiveBF(nums:List[int]):

    #TC:O(N^2)
    #SC:O(1)

    n = len(nums)
    longest = 0

    if n ==0:
        return 0

    sub_length = 0

    for i in range(n):
        x = nums[i]
        sub_length = 1

        while True:
            if x+1 in nums:
                x = x+1
                sub_length +=1
            else:
                longest = max(longest,sub_length)
                sub_length = 1
                break
    return longest


def longestConsecutive(nums:List[int]):
    #TC: O(nlogn)
    #SC:O(1)

    n = len(nums)

    if n ==0:
        return 0
    
    max_sub_length = 1

    nums.sort()

    sub_length = 1

    for i in range(n):
        
        if nums[i] == nums[i-1]+1:
            sub_length +=1
        elif nums[i] == nums[i-1]:
            continue

        else:
            max_sub_length = max(max_sub_length,sub_length)
            sub_length = 1
    
    max_sub_length = max(max_sub_length,sub_length)

    return  max_sub_length

def longestConsecutiveOptimal(nums:List[int])->int:
    n = len(nums)
    if n ==0:
        return 0
    
    longest = 0

    s = set()

    for num in nums:
        s.add(num)

    counter = 0

    for el in s:
        if el-1 in s:
            continue
        else:
            counter +=1
            x = el+1
            while x in s:
                counter +=1
                x+=1
            longest = max(longest,counter)

        counter = 0

    return longest

#LC: 73 Set Matrix Zeros 
def setZeorsBF1(matrix:List[List[int]]):
    #TC:O(mn(m+n))

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:

                counter = 0

                while counter < n:
                    if matrix[i][counter] != 0:
                        matrix[i][counter] = None
                    counter+=1

                counter = 0

                while counter < m:
                    if matrix[counter][j] != 0:
                        matrix[counter][j] = None
                    counter +=1
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == None:
                matrix[i][j] = 0

    return matrix
            




def setZerosBF(matrix:List[List[int]]):
    #TC:O(mn)
    #SC:O(m+n)

    m = len(matrix)
    n = len(matrix[0])

    row_zeros = set()
    col_zeros = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
               row_zeros.add(i)
               col_zeros.add(j)
    
    for i in range(m):
        for j in range(n):
            if i in row_zeros or j in col_zeros:
                matrix[i][j]= 0


    return matrix


def setZerosOptimal(matrix:List[List[int]]):

    #Intuition: We use the first row and first column to store the zeros. We use extra variable col0 to store the zeros in the first column. We iterate the matrix and store the zeros in the first row and first column. We then iterate the matrix and set the zeros based on the first row and first column. We then set the zeros in the first row and first column based on the col0.

    #TC:O(mn)
    #SC:O(1)
    m = len(matrix)
    n = len(matrix[0])

    col0 = 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j == 0:
                    col0 = 0
                else:
                    matrix[0][j] = 0

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0

    if col0 == 0:
        for j in range(m):
            matrix[j][0] = 0

    return matrix

#LC-48: Rotate Image

def rotateImageBF(matrix:List[List[int]]):
    new_matrix = []
    m = len(matrix)
    n = len(matrix[0])

    for j in range(n):
        new_row = []
        for i in range(m-1,-1,-1):
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)

    return new_matrix

def rotateImageBF1(matrix:List[List[int]]):
    #TC:O(N^2)
    #SC:O(N^2)
    n = len(matrix)
    new_matrix = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_matrix[j][n-1-i] = matrix[i][j]
    return new_matrix

def rotateImageOptimal(matrix:List[List[int]]):

    #TC:O(n^2)
    #SC:O(1)

    n = len(matrix)

    for i in range(n-1):
        for j in range(i+1,n):
            if i != j:
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()

    return matrix

def spiralOrder(matrix:List[List[int]]):

    #TC: O(MN)
    #SC:O(MN)

    top = 0 
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0])-1

    res = []
    while left <= right and top <=bottom:
        for i in range(left,right+1):
            res.append(matrix[top][i])
        
        top +=1
 
        for j in range(top,bottom+1):
            res.append(matrix[j][right])
        
        right -=1

        if top <=bottom:
            for k in range(right,left-1,-1):
                res.append(matrix[bottom][k])

            bottom -=1

        if left <= right:
            for l in range(bottom,top-1,-1):
                res.append(matrix[l][left])
            left +=1
    return res

def subarraySum(nums:List[int],k:int)->int:
    #TC:O(n^2)
    #SC:O(1)
    #Intuition: We generate all subarrays and check if the sum of the subarray is equal to k. We maintain a total to store the total number of subarrays.

    n = len(nums)

    total = 0

    i = 0

    while i < n:
        j = i
        while j<n:
            if sum(nums[i:j+1]) == k:
                total +=1
            j+=1
        i+=1

    return total

def subarraySum2(nums:List[int],k:int)->int:
    #TC:O(n^2)
    #SC:O(1)

    n = len(nums)

    total = 0

    i = 0

    while i < n:
        j = i
        sub_sum = 0
        while j<n:
            sub_sum += nums[j]
            if sub_sum == k:
                total +=1
            j+=1
        i+=1

    return total

def subarraySumOptimal(nums:List[int],k)->int:
    #TC:O(N)
    #SC:O(N)
    
    prefix_map = {0:1}
    prefix_sum = 0
    total = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            total += prefix_map[prefix_sum-k]
        
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] +=1
        else:
            prefix_map[prefix_sum] =1

    return total


# arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(setZerosBF(arr))
# print(setZeorsBF1(arr))
# print(setZerosOptimal(arr))

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# print(rotateImageBF(arr))
# print(rotateImageBF1(arr))
# print(rotateImageOptimal(arr))

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(spiralOrder(arr))

for line in sys.stdin:
    arr = list(map(int,line.split(',')))
    k = int(input())
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
    # print(majorityElement(arr))
    # print(maxSubArray(arr))
    # print(maxSubArray2(arr))
    # print(maxSubArrayOptimal(arr))
    # print(maxSubArray2(arr))
    # print(maxProfitBF(arr))
    # print(maxProfitOptimal(arr))
    # print(rearrangeArrayBF(arr))
    # print(rearrangeArrayOptimal(arr))
    # print(rearrangeArrayV2(arr))
    # print(findAllPermutations(arr))
    # print(findAllPermutationsOptimal(arr))
    # print(nextPermutation(arr))
    # print(nextPermutation2(arr))
    # print(leaders(arr))
    # print(leadersOptimal(arr))
    # print(longestConsecutive(arr))
    # print(longestConsecutiveBF(arr))
    # print(longestConsecutiveOptimal(arr))
    # print(subarraySum(arr,k))
    # print(subarraySum2(arr,k))
    print(subarraySumOptimal(arr,k))
    pass

sys.stdout.close()