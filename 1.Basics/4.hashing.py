import sys
import math

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


#LC-217 Contains Duplicate
def containsDuplicate(nums:list[int])->bool:
    #TimeComplexity: O(n^2)
    #SpaceComplexity: O(1)

    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] ==nums[j]:
                return True
    return False

def containsDuplicates2(nums:list[int])->bool:
    #sort the array and check if adjacent elements are same
    #TimeComplexity: O(nlogn)
    #SpaceComplexity: O(1)
    nums.sort()

    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return True
    
    return False

def containsDuplicatesHashMap(nums:list[int])->bool:
    #TimeComplexity: O(n)
    #SpaceComplexity: O(n)

    hashmap= {}

    for ele in nums:
        if ele in hashmap:
            return True
        hashmap[ele] = 1
    return False

#LC-1 Two Sum (Brute Force)
def twoSum(nums:list[int],target:int)->list[int]:
    #TimeComplexity:O(n^2)
    #SpaceComplexity: O(1)
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]

#LC-1 Two Sum (HashMap)     
def twoSumHashMap(nums:list[int],target:int)->list[int]:
    #TimeComplexity: O(n)
    #SpaceComplexity: O(n)

    hashmap = {}

    for index,ele in enumerate(nums):
        diff = target - ele
        if diff in hashmap:
            return [hashmap[diff],index]
        hashmap[ele] = index

#LC-146 LRU Cache
class Node:
    def __init__(self,key:int,value:int):
        self.key =key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self,capacity:int) -> None:
        self.capacity = capacity
        self.hashmap = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self,node:Node)->None:
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next
    
    def _add(self,node:Node)->None:
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next= node


    def get(self,key:int)->int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)

            return self.hashmap[key]
        
        return -1

    
    def put(self,key:int,value:int)->None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        
        new_node = Node(key,value)
        self._add(new_node)
        self.hashmap[key] = new_node

        if len(self.hashmap) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.hashmap[lru.key]

        
# Hashmap Implementation

class Pair:
    def __init__(self,key,value):
        self.key = key
        self.value = value


class Hashmap:

    def __init__(self,capacity):
        self.capacity = capacity

        self.slots = capacity
        self.map = [None]*self.capacity

    def _hash(self,key)->int:
        index = 0
        for char in key:
            index += ord(char)

        return index%self.capacity

    def _computeCapacity(self)->int:
        start = self.capacity*2
        isPrime = True
        while True:
            isPrime = True
            for i in range(2,int(math.sqrt(start))+1):
                if start%i == 0:
                    isPrime = False
                    break

            if isPrime:
                return start
            start+=1
                
        
    def _rehash(self)->None:
        self.capacity = self._computeCapacity()
        print(f'rehash capacity - {self.capacity}')

        newMap = [None]*self.capacity

        oldMap = self.map
       
        self.map = newMap
        self.slots = self.capacity

        for pair in oldMap:
            if pair is not None:
                self.put(pair.key,pair.value)
        pass

    def get(self,key)->int:
        index = self._hash(key)

        while self.map[index] !=None:

            if self.map[index].key == key:
                return self.map[index].value

            index+=1    

            index = index%self.capacity
        
        return -1
        

    def put(self,key,value)->None:
        index = self._hash(key)
        print(key)

        # 2 scenerios 
            # - Open Slot
            # - Already exists
                    # - same key
                    # - different key
        while True:            
            if self.map[index] == None:
                self.map[index] = Pair(key,value)
                self.slots -=1

                if self.slots <= self.capacity//2:
                    self._rehash()
                return

            elif self.map[index].key == key:
                self.map[index].value = value
                return
            
            index+=1
            index = index%self.capacity


# hashmap = Hashmap(2)

# hashmap.put('vinod',1)
# print(hashmap.map)
# hashmap.put('ash',2)
# print(hashmap.map)
# print(hashmap.get('ash'))
# print(hashmap.get('veeru'))
# hashmap.put('veeru',3)
# print(hashmap.map)
# print(hashmap.get('veeru'))


def countFreq(arr:list[int]):
    freq = []
    seen = set()
    for index,ele in enumerate(arr):
        count = 1
        if ele not in seen:
            for j in range(index+1,len(arr)):
                if arr[j] == ele:
                    count+=1
            seen.add(ele)
            freq.append(count)
    print(freq)


def maxAndMinFrequency(arr:list[int]):
    seen = set()
    max_freq = 0
    max_ele = None
    min_freq = 0
    min_ele = None

    for index,ele in enumerate(arr):
        count = 1
        if ele not in seen:
            for i in range(index+1,len(arr)):
                if arr[i] == ele:
                    count+=1
            seen.add(ele)
            if max_ele is None:
                max_freq = count
                max_ele = ele
            else:
                if count>max_freq:
                    max_ele = ele
                max_freq = max(max_freq,count)
                
            
            if min_ele is None:
                min_freq = count
                min_ele = ele
            else:
                if count < min_freq:
                    min_ele = ele
                min_freq = min(min_freq,count)

    return [max_ele,min_ele]
    
def maxAndMinFrequencyHashMap(arr:int)->list[int]:

    freq = {}

    max_freq = None
    min_freq = None

    for ele in arr:
        if ele not in freq:
            freq[ele] = 1
        else:
            freq[ele]+=1
    
    for key in freq:
        if max_freq is None or freq[key] > freq[max_freq]:
            max_freq = key
        if min_freq is None or freq[key] < freq[min_freq]:
            min_freq = key

    return [min_freq,max_freq]
    



# input_data = sys.stdin.read().splitlines()

# for i in range(0, len(input_data), 2):
#     arr = list(map(int, input_data[i].strip().split(',')))
#     target = int(input_data[i + 1].strip())
#     # result = twoSum(arr, target)
#     result = twoSumHashMap(arr, target)
#     print(result)

for line in sys.stdin:
    arr = list(map(int,line.strip().split(',')))
    # target = int(input())
    # print(containsDuplicate(arr))
    # print(containsDuplicatesHashMap(arr))
    # print(containsDuplicates2(arr))
    # countFreq(arr)
    # print(maxAndMinFrequency(arr))
    print(maxAndMinFrequencyHashMap(arr))
    
sys.stdout.close()