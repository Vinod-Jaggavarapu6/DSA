import sys
from typing import List
import math

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

#LC-26 : Remove Duplicates from Sorted Array

def removeDuplicatesBruteForce(nums:List[int])->int:
    s = set()
    for ele in nums:
        s.add(ele)
    
    index = 0

    for ele in s:
         nums[index] = ele
         index+=1
    
    return index

def removeDuplicates(nums: List[int]) -> int:
        
        #Intuition: we keep two pointer one(right) for iterating from index 1 to n and the other(left) for keeping track of the index where we can place the unique element

        #TimeComplexity:O(n)
        #SpaceComplexity:O(1)

        n = len(nums)
        left = 1

        for right in range(1,n):
              if nums[right] != nums[right-1]:
                    nums[left] = nums[right]
                    left+=1
        return left

#LC-27 : Remove Element
def removeElement(nums: List[int], val: int) -> int:
        #Intuition: we keep two pointer one(right) for iterating from index 0 to n and the other(left) for keeping track of the index where we can place the unique element

        #TimeComplexity:O(n)
        #SpaceComplexity:O(1)
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left+=1
        return left
        
#LC-1929 : Concatenation of Array
def getConcatenation(nums: List[int]) -> List[int]:
    #Intuition: we append the same array to the original array
    #TimeComplexity:O(n)
    #SpaceComplexity:O(1)

    n = len(nums)

    for i in range(n):
        nums.append(nums[i])
    return nums


def largestBruteForce(nums:List[int])->int:
    #TimeComplexity:O(nlogn)
    # SpaceComplexity:O(1) 
     nums.sort()
     return nums[-1]

def largest(nums:List[int])->int:
    #TimeComplexity:O(n)
    # SpaceComplexity:O(1)
     
    max_num = nums[0]

    for i in range(1,len(nums)):
         if nums[i] > max_num:
              max_num = nums[i]
    return max_num


def secondLargestBruteForce(nums:List[int])->int:
    #TimeComplexity:O(nlogn)
    #SpaceComplexity:O(1)
    nums.sort()
     
    largest = nums[-1]

    n = len(nums)-2

    while n >= 0 and nums[n] == largest:
        n -=1

    if nums[n] != largest:
        return nums[n]
    else:
        return -1


def secondLargestBetter(nums:List[int])->int:
    largest = nums[1]

    n = len(nums)
    
    for i in range(1,n):
         if nums[i] > largest:
              largest = nums[i]

    second_largest = -1

    for i in range(n):
         if nums[i] > second_largest and nums[i] != second_largest:
              second_largest = nums[i]

    return second_largest  



def secondLargest(nums:List[int])->int:
    largest = nums[0]
    second_largest = -1
   
    for i in range(1,len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
             second_largest = nums[i]
    
    return second_largest

        
#LC-1752: Check If Array is Sorted and Rotated

# def checkIfSortedBruteForce( nums: List[int]) -> bool:
#      pass


#LC-189 : Rotate Array

def rotate(nums,k)->int:
    #Intuition: We rotate the array k times by shifting the elements to the right.

    #TimeComplexity:O(n*k)
    #SpaceComplexity:O(1)

    n = len(nums)
    i  = 0
    while k > i:
        ele = nums[-1]
        for j in range(n-2,-1,-1):
            nums[j+1] = nums[j]
        nums[0] = ele
        i+=1
        print(nums)
    return nums

def rotateOptimal(nums,k):
     
    def reverse(nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
              
    n = len(nums)

    k = k%n

    reverse(nums,0,n-k-1)
    reverse(nums,n-k,n-1)
    reverse(nums,0,n-1)

    return nums

def rotateOptimal2(nums,k):
    n = len(nums)
    k = k%n
        
    temp = nums[:n-k]

    for i in range(n-k,n):
        nums[i-(n-k)] = nums[i]
    
    for j in range(n-k):
        nums[j+k] = temp[j]
        
        
    return nums


def leftRotateBruteForce(nums,k):
    n = len(nums)

    k= k%n

    i  = 1
    while i<=k:
        temp = nums[0]
        for j in range(1,n):
            nums[j-1] = nums[j]
        nums[-1] = temp
        i+=1
    return nums


def leftRotateOptimal(nums,k):
     
    def reverse(nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        print(nums)
    n = len(nums)

    k = k%n

    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    reverse(nums,0,n-1)

    return nums

def leftRotateOptimal2(nums,k):
    n = len(nums)
    k = k%n

    temp = nums[:k]

    for i in range(k,n):
         nums[i-k] =  nums[i]
    
    for j in range(n-k,n):
         nums[j] = temp[j-(n-k)]
    
    return nums
    

#LC-283 : Move Zeroes

def moveZerosBruteForce(nums):
    #Intuition: We keep two arrays one for storing the non-zero elements and the other for storing the zero elements. We then append the zero elements to the non-zero elements.
    #TimeComplexity:O(n)
    #SpaceComplexity:O(n)
    n = len(nums)
    temp = []
    zeros_count = 0

    for ele in nums:
        if ele != 0:
            temp.append(ele)
        else:
            zeros_count+=1
   
    for i in range(len(temp)):
        nums[i] = temp[i]

    for j in range(zeros_count):
        nums[n-zeros_count+j] = 0
    
    return nums


def moveZeros(nums):

    #Intuition: We keep two pointers one for keeping track of the leftmost zero element and the other for iterating through the array. We swap the non-zero element with the zero element.
    #TimeComplexity:O(n)
    #SpaceComplexity:O(1)
    n = len(nums)
    left = 0

    for right in range(n):
        if nums[right] !=0:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
    return nums

def moveZerosOptimal(nums):
    #Intuition: We keep two pointers one for keeping track of the leftmost zero element and the other for iterating through the array. We swap the non-zero element with the zero element.
    #TimeComplexity:O(n)
    #SpaceComplexity:O(1)
    n = len(nums)
    left = 0

    while left < n and nums[left] != 0:
        left +=1

    if left ==n:
        return nums

    for right in range(left+1,n):
        if nums[right] != 0:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
    return nums


def unionOfArrays(nums1:List[int],nums2:list[int])->list[int]:
    s = set()
    for ele in nums1:
        s.add(ele)
    for ele in nums2:
        s.add(ele)
    union_list = list(s)
    return union_list 

def unionOfArraysOptimal(nums1:List[int],nums2:list[int])->list[int]:
    n1 = len(nums1)
    n2 = len(nums2)

    i,j,k = 0,0,-1

    union_list = []

    while i < n1 and j < n2:
        if nums1[i] <= nums2[j]:
            if k==-1 or union_list[k] != nums1[i]:
                union_list.append(nums1[i])
            i+=1
        elif nums1[i] > nums2[j]:
            if k==-1 or union_list[k] != nums2[j]:
                union_list.append(nums2[j])
            j+=1
        k+=1

    while i < n1:
        if union_list[k] != nums1[i]:
            union_list.append(nums1[i])
        i+=1
    
    while j < n2:
        if union_list[k] != nums2[j]:
            union_list.append(nums2[j])
        j+=1
    
    return union_list

#LC-349 : Intersection of Two Arrays

def intersectionOfArrays(nums1:List[int],nums2:list[int])->list[int]:
    #Intuition: We keep two pointers one for iterating through the first array and the other for iterating through the second array. We compare the elements and if they are equal we add them to the intersection list.
    #TimeComplexity:O(n1+n2)
    #SpaceComplexity:O(min(n1,n2)

    n1 = len(nums1)
    n2 = len(nums2)

    i,j = 0,0

    intersection_list = []
 
    while i< n1 and j < n2:
        print(i,j)
        if nums1[i] == nums2[j] and (len(intersection_list)==0 or (intersection_list[-1] != nums1[i])):
            intersection_list.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] < nums2[j]:
            i+=1
        else:
            j+=1
    return intersection_list

def intersectionOfArraysBF(nums1:List[int],nums2:list[int])->list[int]:
   
    #TimeComplexity:O(n1*n2)
    #SpaceComplexity:O(min(n1,n2))
    n2 = len(nums2)

    intersection_list = []

    is_visited = [False]*n2

    for ele in nums1:
        for j in range(n2):
            if ele == nums2[j] and  is_visited[j] == False and (len(intersection_list) == 0 or intersection_list[-1] != ele):
                intersection_list.append(ele)
                is_visited[j] = True
                break
    return intersection_list


#LC - 268 : Missing Number

def missingNumberBruteForce(nums):
    #TimeComplexity:O(nlogn)
    #SpaceComplexity:O(1)

    n = len(nums)
    nums.sort()

    for i in range(n+1):
        if i ==n or nums[i] != i:
            return i

def missingNumber1(nums):
    n = len(nums)
    sum_of_n = n*(n+1)//2

    sum_of_nums = 0
    for i in range(n):
        sum_of_nums += nums[i]

    return sum_of_n - sum_of_nums

def missingNumber2(nums):

    xor1 = 0
    xor2 = 0

    for i,num in enumerate(nums):
        xor1 ^= (i+1)
        xor2 ^= num
    
    return xor1^xor2

#LC-485 : Max Consecutive Ones

def maxConsecutiveOnes(nums):
    #TimeComplexity:O(n)
    #SpaceComplexity:O(1)
   
    max_count = 0
    count = 0

    for num in nums:
        if num == 1:
            count+=1
        else:
            max_count = max(max_count,count)
            count = 0

    return max(max_count,count)

#LC-136 : Single Number

def singleNumber(nums):
    num_count = {}

    for num in nums:
        if num in num_count:
            num_count[num]+=1
        else:
            num_count[num] = 1   

    for key in num_count:
        if num_count[key] == 1:
            return key

def singleNumberOptimal(nums):
    xor = 0

    for num in nums:
        xor ^=num
    
    return xor

for line in sys.stdin:
    
    nums = list(map(int, line.split(',')))
    # val = int(input())
    # k = int(input())
    # print(removeDuplicates(nums))
    # print(removeDuplicatesBruteForce(nums))
    # print(removeElement(nums,val))
    # print(getConcatenation(nums))
    # print(largestBruteForce(nums))
    # print(largest(nums))
    # print(secondLargest(nums))
    # print(secondLargestBruteForce(nums))
    # print(secondLargestBetter(nums))

    # print(rotate(nums,k))
    # print(rotateOptimal2(nums,k))
    # print(leftRotateBruteForce(nums,k))
    # print(leftRotateOptimal(nums,k))
    # print(leftRotateOptimal2(nums,k))
    # print(moveZerosBruteForce(nums))
    # print(moveZeros(nums))
    # print(moveZerosOptimal(nums))

    # print(missingNumberBruteForce(nums))
    # print(missingNumber1(nums))

    # print(missingNumber2(nums))
    # print(maxConsecutiveOnes(nums))

    # print(singleNumber(nums))
    print(singleNumberOptimal(nums))

# nums1 = [1, 2, 2, 4, 5, 6]
# nums2 = [2, 3, 5, 7]
# print(unionOfArrays(nums1,nums2))

# nums1 = [1,2,2,1]
# nums2 = [2,2]
# print(intersectionOfArrays(nums1,nums2))
# print(intersectionOfArraysBF(nums1,nums2))

sys.stdout.close()